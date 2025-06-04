# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse_name": "",
# META       "default_lakehouse_workspace_id": ""
# META     },
# META     "environment": {
# META       "environmentId": "894291a9-f8d5-4ea0-8d4d-a41d3d9b7541",
# META       "workspaceId": "00000000-0000-0000-0000-000000000000"
# META     }
# META   }
# META }

# MARKDOWN ********************

# #### Generate Harmonisation - Application
# ---
# Notebook to perform the harmonisation for applications from LeanIX and ServiceNow
# 
# 
# ###### **<u>Step 1: Import common libraries and helper functions</u>**
# 
# - Import any required public libraries and custom functions via `%run` magic command. 
# - Custom functions are defined and stored within other notebooks within `notebooks/utilities/nb_helper_functions_<action>.py`.

# CELL ********************

%run nb_helper_functions_parent_caller

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_schema_dim_application_source

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_schema_dim_application

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_schema_dim_application_map

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ###### **<u>Step 2: Define Parameters</u>**
# - The following cell is noted as a Parameter cell; default values can be overwritten when the notebook is executed either via DAG calls or Data Factory Pipelines. 
# - To 'parameterize' a code cell, click on the `...` 'more command' button on the right as you hover your cursor over the cell and click `[@] Toggle parameter cell`

# PARAMETERS CELL ********************

trigger_time = None

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ###### **<u>Step 3: Extract configurations and table schema</u>**
# - Extract global configuration and table specific configuration defined in `notebooks/nb_configs.py`. 
# - Extract table schema defined in `notebooks/schemas/<source> or <target/<facts> or <dimension>>/`

# CELL ********************

global_configs = globals()['global_configs']
harmonized_configs = globals()['harmonized']['application']

lean_ix_name = globals()['lean_ix']['name']
service_now_name = globals()['service_now']['name']

primary_key = harmonized_configs['primary_key']
attributes_key = harmonized_configs['attributes_key']


tables = list(harmonized_configs['required_tables']['conformed']['dimensions'].keys())
source_target_schema = globals()[f"schema_{tables[0]}_v{harmonized_configs['required_tables']['conformed']['dimensions'][tables[0]]['schema_version']}"]
main_target_schema = globals()[f"schema_{tables[1]}_v{harmonized_configs['required_tables']['conformed']['dimensions'][tables[1]]['schema_version']}"]
map_target_schema = globals()[f"schema_{tables[2]}_v{harmonized_configs['required_tables']['conformed']['dimensions'][tables[2]]['schema_version']}"]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Main Code Block
# ---
# ###### **<u>Step 4: Perform Harmonization</u>**
# Harmonize data.


# CELL ********************

##### START EXTRACT #####
df_dicts = read_all_required_dataframes(harmonized_configs['required_tables'], None, None)
##### END EXTRACT #####


##### START MAP PROCESS - master snow records in map table #####
# this converts Name column to lower case, removes spaces and any special characters within it - enabling higher chances of matching
regex_pattern = r'[\s./,]'
df_source = df_dicts['dim_application_source'].withColumn('NormalizedName', F.lower(F.regexp_replace(F.regexp_replace('Name', regex_pattern, ''), ' ', '')))

# select and alias only relevant columns for matching
df_source_snow = df_source.filter(F.col('SourceSystem') == service_now_name).select(primary_key, F.col('UniqueIdentifier').alias('LeanIXExternalID'), 'NormalizedName')
df_source_leanix = df_source.filter(F.col('SourceSystem') == lean_ix_name).select(F.col(primary_key).alias('LIXApplicationKey'), 'LeanIXExternalID', 'NormalizedName')

# inner join 1 -> match on External ID
# inner join 2 -> match on Normalized Name
df_common_id = df_source_snow.join(df_source_leanix, 'LeanIXExternalID', 'inner').withColumn('NewMasteredMethod', F.lit('id')).drop(*['LeanIXExternalID', 'NormalizedName'])
df_common_name = df_source_snow.join(df_source_leanix, 'NormalizedName', 'inner').withColumn('NewMasteredMethod', F.lit('name')).drop(*['LeanIXExternalID', 'NormalizedName'])

# remove duplicate match - ranking outlined in nb_configs (ie. id match outmatches name match)
rank_expr = F.create_map([F.lit(x) for x in chain(*harmonized_configs['method_ranking'].items())])
df_common = df_common_id \
    .unionByName(df_common_name) \
    .withColumn('Rank', F.coalesce(rank_expr.getItem(F.col('NewMasteredMethod')), F.lit(None))) \
    .transform(lambda df_common: deduplicate_by_keys(df_common, [primary_key], ['Rank'], 'asc')) \
    .drop('Rank')

# split df_map into mastered and not mastered
df_map_mastered = df_dicts['dim_application_map'].filter(F.col('IsMastered'))
df_map_unmastered = df_dicts['dim_application_map'].filter(~F.col('IsMastered'))

# master unmastered records (leanix self maps)
condition_1 = (F.col('LIXApplicationKey').isNotNull())
condition_2 = (F.col('SourceSystem') == lean_ix_name)
condition_3 = (F.col('ApplicationMasterKey').isNotNull())

df_map_newly_mastered = df_map_unmastered.join(df_common, primary_key, 'left') \
    .withColumn('ApplicationMasterKey', F.when(condition_1, F.col('LIXApplicationKey')).when(condition_2, F.col(primary_key)).otherwise(F.col('ApplicationMasterKey'))) \
    .withColumn('IsMastered', F.when(condition_3, F.lit(True)).otherwise(F.col('IsMastered'))) \
    .withColumn('MasteredBy', F.when(condition_3, F.lit('Automatic')).otherwise(F.col('MasteredBy'))) \
    .withColumn('MasteredDate', F.when(condition_3, F.to_date(F.lit(trigger_time))).otherwise(F.col('MasteredDate'))) \
    .withColumn('MasteredMethod', F.when(condition_2, F.lit('own')).when(condition_3, F.coalesce(F.col('NewMasteredMethod'), F.lit(None))).otherwise(F.col('MasteredMethod'))) \
    .drop(*['LIXApplicationKey', 'NewMasteredMethod'])

# union back previously mastered record to newly mastered record
df_map = df_map_mastered \
    .unionByName(df_map_newly_mastered) \
    .transform(lambda df: add_hash_key(df, attributes_key, ['ApplicationMasterKey', 'IsMastered', 'MasteredBy', 'MasteredMethod']))
##### END MAP PROCESS #####


##### START MAIN PROCESS - master snow records in main table #####
df_main_mastered = df_dicts['dim_application'].filter(F.col('IsMaster'))
df_main_unmastered = df_dicts['dim_application'].filter(~F.col('IsMaster')).select(*global_configs['metadata_fields'] + [primary_key, 'IsMaster'])

# join unmastered snow field with subset of df_map
df_main_unmastered = df_main_unmastered.join(df_map.select(primary_key, 'ApplicationMasterKey'), primary_key, 'left')

# subset mastered leanix data with only relevant attributes
df_main_mastered_trimmed = df_main_mastered.drop(*global_configs['metadata_fields'] + ['IsMaster']).withColumnRenamed(primary_key, 'ApplicationMasterKey')

# join unmastered snow df with mastered leanix df on 'ApplicationMasterKey', bringing in all leanix attributes
df_main_unmastered = df_main_unmastered.join(df_main_mastered_trimmed, 'ApplicationMasterKey', 'left')

# union back both mastered and newly mastered records
df_main = df_main_mastered.unionByName(df_main_unmastered.drop('ApplicationMasterKey'))
##### END MAIN PROCESS #####


##### START PRIVACY #####
df_source, df_privacy_source = handle_personal_and_sensitive_fields(df_source, source_target_schema, primary_key)
df_main, df_privacy_main = handle_personal_and_sensitive_fields(df_main, main_target_schema, primary_key)
df_map, df_privacy_map = handle_personal_and_sensitive_fields(df_map, map_target_schema, primary_key)
##### END PRIVACY ######


# ##### START WRITE #####
# privacy - sourced
if df_privacy_source:
    delta_writer(
        df = df_privacy_source, 
        lakehouse_name = global_configs['conformed_pii_lh_name'], 
        table = f"{tables[0]}_pii", 
        schema_version = harmonized_configs['required_tables']['conformed']['dimensions'][tables[0]]['schema_version'], 
        write_type = globals()['dimensions'][f"{tables[0]}"]['write_type'], 
        )

# privacy - main
if df_privacy_main:
    delta_writer(
        df = df_privacy_main, 
        lakehouse_name = global_configs['conformed_pii_lh_name'], 
        table = f"{tables[1]}_pii", 
        schema_version = harmonized_configs['required_tables']['conformed']['dimensions'][tables[1]]['schema_version'], 
        write_type = globals()['dimensions'][f"{tables[1]}"]['write_type'], 
        )

# privacy - map
if df_privacy_map:
    delta_writer(
        df = df_privacy_map, 
        lakehouse_name = global_configs['conformed_pii_lh_name'], 
        table = f"{tables[2]}_pii", 
        schema_version = harmonized_configs['required_tables']['conformed']['dimensions'][tables[2]]['schema_version'], 
        write_type = globals()['dimensions'][f"{tables[2]}"]['write_type'], 
        primary_key = primary_key,
        attributes_key = attributes_key
        )

# conformed - sourced
delta_writer(
    df = df_source.drop('NormalizedName'), 
    lakehouse_name = global_configs['conformed_lh_name'], 
    table = tables[0], 
    schema_version = harmonized_configs['required_tables']['conformed']['dimensions'][tables[0]]['schema_version'], 
    write_type = globals()['dimensions'][f"{tables[0]}"]['write_type'], 
    )

# conformed - main
delta_writer(
    df = df_main, 
    lakehouse_name = global_configs['conformed_lh_name'], 
    table = tables[1], 
    schema_version = harmonized_configs['required_tables']['conformed']['dimensions'][tables[1]]['schema_version'], 
    write_type = globals()['dimensions'][f"{tables[1]}"]['write_type'], 
    )

# conformed - map
delta_writer(
    df = df_map, 
    lakehouse_name = global_configs['conformed_lh_name'], 
    table = tables[2], 
    schema_version = harmonized_configs['required_tables']['conformed']['dimensions'][tables[2]]['schema_version'], 
    write_type = globals()['dimensions'][f"{tables[2]}"]['write_type'], 
    primary_key = primary_key,
    attributes_key = attributes_key
    )

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
