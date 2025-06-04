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

# #### Generate Conformed - Dim Application Map
# ---
# Notebook to perform the creation of Dim Application Map, storing the table in the `Conformed` Lakehouse as delta format
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

table_name = 'dim_application_map'
conformed_layer = 'dimensions'

global_configs = globals()['global_configs']
target_table_configs = globals()[conformed_layer][table_name]
target_schema = globals()[f"schema_{table_name}_v{target_table_configs['schema_version']}"]

primary_key = target_table_configs['primary_key']
attributes_key = target_table_configs['attributes_key']
metadata_fields = global_configs['metadata_fields']

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Main Code Block
# ---
# ###### **<u>Step 3: Perform ETL</u>**
# Extract, transform and load data.


# CELL ********************

##### START EXTRACT #####
df_dicts = read_all_required_dataframes(target_table_configs['required_tables'], target_schema, trigger_time, True)

delta_path = f"{get_lakehouse_abfs_path(global_configs['conformed_lh_name'])}/Tables/{target_table_configs['name']}_sv_{target_table_configs['schema_version']}"
# table already exists
if DeltaTable.isDeltaTable(spark, delta_path):
    df_map = read_dataframe(
        lakehouse_name = global_configs['conformed_lh_name'], 
        schema_version = target_table_configs['schema_version'], 
        table_name = target_table_configs['name']
        )
else:
    # first run
    df_map = None
##### END EXTRACT #####


##### START TRANSFORMATION #####
# leanix transformation
df_application = df_dicts['Application'] \
    .filter((F.col('Name').isNotNull()) | (F.col('Name') != '')) \
    .transform(lambda df_application: add_hash_key(df_application, primary_key, ['Name'], globals()['lean_ix']['name'])) \
    .dropDuplicates()

# snow - application transformation - PK deduplicated due to known issue at source, can be removed once resolved
df_cmdb_ci_appl = df_dicts['cmdb_ci_appl'] \
    .filter((F.col('Name').isNotNull()) | (F.col('Name') != '')) \
    .transform(lambda df: deduplicate_by_keys(df, ['Name'], ['SysUpdatedOn'])) \
    .transform(lambda df_cmdb_ci_appl: add_hash_key(df_cmdb_ci_appl, primary_key, ['Name'], globals()['service_now']['name'])) \

# union both dataframes and get rid of duplicate ApplicationKeys
union_df = df_application.unionByName(df_cmdb_ci_appl, allowMissingColumns=True)
df = union_df.where(~(union_df.ApplicationKey.isin([-849862343517725175, 5896695335020484737])))

if df_map:
    # split df_map into mastered and not mastered
    df_map_mastered = df_map.filter(F.col('IsMastered'))
    df_map_not_mastered = df_map.filter(~F.col('IsMastered')).select('ApplicationKey')
    
    # inner join with df to only keep not mastered records and populate with attributes
    df = df \
        .join(df_map_not_mastered, 'ApplicationKey', 'inner') \
        .withColumn('IsMastered', F.lit(False)) \
        .withColumn('ApplicationMasterKey', F.lit(None)) \
        .withColumn('MasteredBy', F.lit(None)) \
        .withColumn('MasteredDate', F.lit(None)) \
        .withColumn('MasteredMethod', F.lit(None)) \
        .select(*[F.col(f['field']).cast(f['dataType']) for f in target_schema]) \
        .transform(lambda df: add_hash_key(df, attributes_key, ['ApplicationMasterKey', 'IsMastered', 'MasteredBy', 'MasteredMethod']))
    
    # union unmastered with mastered (ensures no overwrites of existing attributes)
    df = df.union(df_map_mastered)

else:
    # occurs first run only
    df = df \
        .withColumn('IsMastered', F.lit(False)) \
        .withColumn('ApplicationMasterKey', F.lit(None)) \
        .withColumn('MasteredBy', F.lit(None)) \
        .withColumn('MasteredDate', F.lit(None)) \
        .withColumn('MasteredMethod', F.lit(None)) \
        .select(*[F.col(f['field']).cast(f['dataType']) for f in target_schema]) \
        .transform(lambda df: add_hash_key(df, attributes_key, ['ApplicationMasterKey', 'IsMastered', 'MasteredBy', 'MasteredMethod']))
##### END TRANSFORMATION #####


##### START PRIVACY #####
# Note: masking only happens at the harmonisation stage
##### END PRIVACY #####

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ###### **Running Data Quality Checks**
# 
# ---
# - [Check the Data Quality Checks Wiki for info on running DQ checks](https://informaeds.visualstudio.com/Global%20Support/_wiki/wikis/Global-Support.wiki/38/Running-Data-Quality-Checks).


# CELL ********************

%run nb_helper_functions_data_quality

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Variable to store error data from runs (if any)
errors = []

try:
    #Non PII Data
    execute_write_to_lakehouse_with_dq_checks(df=df, layer='Conformed', write_mode_cleansed=None, partition_by = None, pii_enabled = False)
except Exception as e:
    errors.append(f"Non-PII Data Check failed: {str(e)}")

# Raise error if any checks failed
if errors:
    raise Exception("One or more data quality checks failed:\n" + "\n".join(errors))
else:
    print("Both Non-PII and PII Data Quality Checks completed successfully.")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
