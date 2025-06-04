# Fabric notebook source# NOTE: This is an anonymized example with client data and IDs replaced with placeholder values
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

# #### Generate Cleansed - Sample HR System
# ---
# Generic notebook to perform cleansing / enriching activities for HR data derived from the `Sourced` Lakehouse, before storing the cleansed / enriched data within the `Cleansed` Lakehouse as parquet format.
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

%run nb_schema_sourced_sample_hr

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
source_configs = globals()['sample_hr']
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
# ###### **<u>Perform ETL</u>**
# - read parquet files as dataframe
# - add fields not present in DLM schema (can occur when working across various environments)
# - extract value field from nested columns
# - de-duplicate rows
# - select fields, rename to PascalCase and cast to datatypes defined within DLM
# - add metadata fields
# - Perform DQ Checks
# - write to Cleansed Lakehouse if DQ Checks Succeed

# CELL ********************

# read data from the Sourced Lakehouse
cleansed_df = read_dataframe(global_configs['sourced_lh_name'], source_configs['name'], table_name, table_config['schema_version'], trigger_time)

# create new df with required fields
cleansed_df = cleansed_df.select(*extact_required_fields(schema, table_name, 'from'))

# add missing fields
for field in schema:
    if field['from'] not in cleansed_df.columns:
        cleansed_df = cleansed_df.withColumn(field['from'], F.lit(None))
        print(f"Field {field['from']} not found. Adding to df")

# select relevant fields / rename to Pascal / cast to datatypes / add metadata
cleansed_df = cleansed_df \
    .select([F.col(c['from']).alias(c['to']).cast(c['dataType']) for c in schema]) \
    .transform(lambda cleansed_df: add_pipeline_metadata(cleansed_df, trigger_time, trigger_time, source_configs['name'], table_name)) \
    .transform(lambda cleansed_df: cap_timestamp_fields(cleansed_df)) \
    .transform(lambda cleansed_df: cleansed_type_conversion(cleansed_df, schema, 'to'))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ###### **Running Data Quality Checks**
# 
# ---
# - Check the Data Quality Checks documentation for info on running DQ checks.

# CELL ********************

%run nb_helper_functions_data_quality

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#execute write if df is not empty
if cleansed_df is not None and cleansed_df.head(1):
    execute_write_to_lakehouse_with_dq_checks(df=cleansed_df, layer='Cleansed', write_mode_cleansed = None)
else: 
    print("No sourced data found for table {table_name}, no dq checks executed")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
