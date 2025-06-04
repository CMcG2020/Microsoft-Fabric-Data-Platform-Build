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

# #### Generate Harmonisation - Supplier
# ---
# Notebook to perform the harmonisation for suppliers from Coupa, LeanIX and ServiceNow.
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

%run nb_schema_dim_supplier_source

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_schema_dim_supplier

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_schema_dim_supplier_map

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
harmonized_configs = globals()['harmonized']['supplier']

coupa_name = globals()['coupa']['name']
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

# read in all required dataframes
df_dicts = read_all_required_dataframes(harmonized_configs['required_tables'], None, None)

##### START MAP PROCESS - master coupa records in map table #####
# Normalize the 'SupplierName' column for better matching
# Matches any space (\s), period (.), slash (/), or comma (,). Keeps other non-latin characters untouched (Chinese / Korean / etc.)
regex_pattern = r'[\s./,]'
df_source = df_dicts['dim_supplier_source'].withColumn('NormalizedSupplierName', F.lower(F.regexp_replace('SupplierName', regex_pattern, '')))

# Select and alias only relevant columns for matching from each source system
# de-dupe master coupa data by LastUpdatedDateTime
df_source_coupa = df_source \
    .filter(F.col('SourceSystem') == coupa_name) \
    .select(F.col(primary_key).alias('CoupaSupplierKey'), 'NormalizedSupplierName', 'LastUpdatedDateTime') \
    .transform(lambda df: deduplicate_by_keys(df, ['NormalizedSupplierName'], ['LastUpdatedDateTime'])) \
    .drop('LastUpdatedDateTime')
df_source_snow = df_source.filter(F.col('SourceSystem') == service_now_name).select(F.col(primary_key).alias('SnowSupplierKey'), 'NormalizedSupplierName')
df_source_leanix = df_source.filter(F.col('SourceSystem') == lean_ix_name).select(F.col(primary_key).alias('LeanIXSupplierKey'), 'NormalizedSupplierName')

# Start with Coupa as the master and try to find matches in ServiceNow and LeanIX
df_common_name_coupa_snow = df_source_coupa.join(df_source_snow, 'NormalizedSupplierName', 'inner').withColumn('NewMasteredMethod', F.lit('name')).withColumn('LeanIXSupplierKey', F.lit(None).cast(StringType()))
df_common_name_coupa_leanix = df_source_coupa.join(df_source_leanix, 'NormalizedSupplierName', 'inner').withColumn('NewMasteredMethod', F.lit('name')).withColumn('SnowSupplierKey', F.lit(None).cast(StringType()))

# Combine matches from both ServiceNow and LeanIX
df_common_name = df_common_name_coupa_snow \
    .select('CoupaSupplierKey', 'SnowSupplierKey', 'LeanIXSupplierKey', 'NormalizedSupplierName', 'NewMasteredMethod') \
    .unionByName(df_common_name_coupa_leanix.select('CoupaSupplierKey', 'SnowSupplierKey', 'LeanIXSupplierKey', 'NormalizedSupplierName', 'NewMasteredMethod'))

# Remove duplicate match - ranking outlined in nb_configs
rank_expr = F.create_map([F.lit(x) for x in chain(*harmonized_configs['method_ranking'].items())])
df_common = df_common_name \
    .withColumn('Rank', F.coalesce(rank_expr[F.col('NewMasteredMethod')], F.lit(None))) \
    .transform(lambda df_common: deduplicate_by_keys(df_common, ['CoupaSupplierKey'], ['Rank'], 'asc')) \
    .drop('Rank')

# Split df_map into mastered and not mastered
df_map_mastered = df_dicts['dim_supplier_map'].filter(F.col('IsMastered'))
df_map_unmastered = df_dicts['dim_supplier_map'].filter(~F.col('IsMastered'))

# Add NormalizedSupplierName to df_map_unmastered
df_map_unmastered_with_names = df_map_unmastered.join(df_source.select(primary_key, 'NormalizedSupplierName'), primary_key, 'left')

# Master unmastered records
condition_1 = (F.col('CoupaSupplierKey').isNotNull())
condition_2 = (F.col('SourceSystem') == coupa_name)
condition_3 = (F.col('SupplierMasterKey').isNotNull())

df_map_newly_mastered = df_map_unmastered_with_names \
    .join(df_common, 'NormalizedSupplierName', 'left') \
    .withColumn('SupplierMasterKey', F.when(condition_2, F.col(primary_key)).when(condition_1, F.col('CoupaSupplierKey')).otherwise(F.col('SupplierMasterKey'))) \
    .withColumn('IsMastered', F.when(condition_3, F.lit(True)).otherwise(F.col('IsMastered'))) \
    .withColumn('MasteredBy', F.when(condition_3, F.lit('Automatic')).otherwise(F.col('MasteredBy'))) \
    .withColumn('MasteredDateTime', F.when(condition_3, F.to_date(F.lit(trigger_time))).otherwise(F.col('MasteredDateTime'))) \
    .drop(*['SnowSupplierKey', 'LeanIXSupplierKey', 'CoupaSupplierKey', 'NewMasteredMethod', 'NormalizedSupplierName'])  

# Union back previously mastered record to newly mastered record
# Recalculate AttributesKey for merge
df_map = df_map_mastered \
    .unionByName(df_map_newly_mastered.select(*df_map_mastered.columns)) \
    .transform(lambda df: add_hash_key(df, attributes_key, ['SupplierMasterKey', 'IsMastered', 'MasteredBy']))
##### END MAP PROCESS #####


##### START MAIN PROCESS - master supplier records in main table #####
df_main_mastered = df_dicts['dim_supplier'].filter(F.col('IsMaster'))
df_main_unmastered = df_dicts['dim_supplier'].filter(~F.col('IsMaster')).select(*global_configs['metadata_fields'] + [primary_key, 'IsMaster'])

# Join unmastered supplier field with subset of df_map
df_main_unmastered = df_main_unmastered.join(df_map.select(primary_key, 'SupplierMasterKey'), primary_key, 'left')

# Subset mastered coupa data with only relevant attributes
df_main_mastered_trimmed = df_main_mastered.drop(*global_configs['metadata_fields'] + ['IsMaster']).withColumnRenamed(primary_key, 'SupplierMasterKey')

# Join unmastered supplier df on 'SupplierMasterKey', bringing in all coupa attributes
df_main_unmastered = df_main_unmastered.join(df_main_mastered_trimmed, 'SupplierMasterKey', 'left')

# Union back both mastered and newly mastered records
df_main = df_main_mastered.unionByName(df_main_unmastered.select(*df_main_mastered.columns))
##### END MAIN PROCESS #####


##### START PRIVACY #####
df_source, df_privacy_source = handle_personal_and_sensitive_fields(df_source, source_target_schema, primary_key)
df_main, df_privacy_main = handle_personal_and_sensitive_fields(df_main, main_target_schema, primary_key)
df_map, df_privacy_map = handle_personal_and_sensitive_fields(df_map, map_target_schema, primary_key)
##### END PRIVACY ######


##### START WRITE #####
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
    df = df_source.drop('NormalizedSupplierName'), 
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
