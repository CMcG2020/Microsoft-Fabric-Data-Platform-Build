# Fabric notebook source# NOTE: This is an anonymized example with client data and IDs replaced with generic placeholders
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
# META       "environmentId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
# META       "workspaceId": "yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy"
# META     }
# META   }
# META }

# MARKDOWN ********************

# #### Generate Cleansed - Data Source
# ---
# Generic notebook to perform cleansing / enriching activities for source data derived from the `Sourced` Lakehouse, before storing the cleansed / enriched data within the `Cleansed` Lakehouse as parquet format.
# 
# 
# ###### **<u>Step 1: Import common libraries and helper functions</u>**
# 
# - Import any required public libraries and custom functions via `%run` magic command. 
# - For custom functions, import the `nb_helper_functions_parent_caller.py` notebook to collectively bring in all the required custom functions.

# CELL ********************

%run nb_helper_functions_parent_caller

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_schema_sourced_push_data_source

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
table_name = None

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
source_configs = globals()['data_source']
table_config = source_configs['source_tables'][table_name]

schema = globals()[f"schema_{table_name}_v{table_config['schema_version']}"]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Main Code Block
# ---
# ###### **<u>Step 3: Perform ETL</u>**
# - read parquet files as dataframe
# - add fields not present in DLM schema (can occur when working across various environments)
# - extract value field from nested columns
# - de-duplicate rows
# - select fields, rename to PascalCase and cast to datatypes defined within DLM
# - add metadata fields
# - write to Cleansed Lakehouse


# CELL ********************

# read data from the Sourced Lakehouse
sourced_df = read_dataframe(global_configs['sourced_lh_name'], source_configs['name'], table_name, table_config['schema_version'], trigger_time)

# create new df in the event no missing fields are added
cleansed_df = sourced_df

# add fields not present in df
for k in schema:
    if k['from'] not in cleansed_df.columns:
        cleansed_df = cleansed_df.withColumn(k['from'], F.lit(None))
        print(f"'{k['from']}' required column not found for table {table_name}. Adding within Cleansed layer")   

# select relevant fields / rename to Pascal / cast to datatypes / add metadata
cleansed_df = cleansed_df \
    .select([F.col(c['from']).alias(c['to']).cast(c['dataType']) for c in schema]) \
    .transform(lambda cleansed_df: add_pipeline_metadata(cleansed_df, trigger_time, trigger_time, source_configs['name'], table_name)) \
    .transform(lambda cleansed_df: cap_timestamp_fields(cleansed_df)) \
    .transform(lambda cleansed_df: cleansed_type_conversion(cleansed_df, schema, 'to'))

# write data to the Cleansed Lakehouse
write_parquet_to_lakehouse(cleansed_df, global_configs['cleansed_lh_name'], source_configs['name'], table_name, table_config['schema_version'], trigger_time)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
