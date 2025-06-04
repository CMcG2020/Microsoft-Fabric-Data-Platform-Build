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
# META       "environmentId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
# META       "workspaceId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
# META     }
# META   }
# META }

# MARKDOWN ********************

# #### Generate Cleansed - Example Data Source
# ---
# Generic notebook to perform cleansing / enriching activities for example data source derived from the `Sourced` Lakehouse, before storing the cleansed / enriched data within the `Cleansed` Lakehouse as parquet format.
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

%run nb_schema_sourced_example_data_source

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
source_configs = globals()['example_data_source']
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

# Will need to be investigated
spark.conf.set("spark.sql.legacy.timeParserPolicy", "LEGACY")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# read data from the Sourced Lakehouse
cleansed_df = read_dataframe(global_configs['sourced_lh_name'], source_configs['name'], table_name, table_config['schema_version'], trigger_time)
if cleansed_df.count() == 0:
   print(f'No sourced data found for table {table_name}, ending notebook')
else:
    
  # Get list of timestamp fields from schema
  timestamp_fields = [row['from'] for row in schema if isinstance(row['dataType'], TimestampType)]
  personal = [*[row['from'] for row in schema if row['personal']]]
  
  # Process each column
  for col in cleansed_df.columns:
      if col in timestamp_fields:
          # For timestamp fields, always get display_value
          cleansed_df = cleansed_df.withColumn(
              col, 
              F.coalesce(F.get_json_object(F.col(col), "$.display_value"), F.lit(None))
          )
      else:
          # For non-timestamp fields, use the original logic
          value = 'value' if (col in personal and not col.startswith('sys_')) else 'display_value'
          
          # Add edge case for specific customer field column
          if col == "u_customer_field":
            value = 'display_value'
        
          cleansed_df = cleansed_df.withColumn(
              col, 
              F.coalesce(F.get_json_object(F.col(col), f"$.{value}"), F.lit(None))
          )

  for k in schema:
      # add fields not present in df
      if k['from'] not in cleansed_df.columns:
          cleansed_df = cleansed_df.withColumn(k['from'], F.lit(None))
          print(f"'{k['from']}' required column not found for table {table_name}. Adding within Cleansed layer")
      # split out array fields by ',' delimiter - if empty string return None
      if k['dataType'] == ArrayType(StringType()):
          cleansed_df = cleansed_df.withColumn(
              k['from'], 
              F.when(F.col(k['from']) == '', F.lit(None)).otherwise(F.split(k['from'], ','))
          )

  # select relevant fields / rename to Pascal / cast to datatypes / add metadata
  cleansed_df = cleansed_df \
  .transform(lambda cleansed_df: cleansed_type_conversion(cleansed_df, schema, 'from')) \
  .select([F.col(c['from']).alias(c['to']).cast(c['dataType']) for c in schema]) \
  .transform(lambda cleansed_df: add_pipeline_metadata(cleansed_df, trigger_time, trigger_time, source_configs['name'], table_name)) \
  .transform(lambda cleansed_df: cap_timestamp_fields(cleansed_df))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ###### **Running Data Quality Checks**
# 
# ---
# - [Check the Data Quality Checks Wiki for info on running DQ checks](https://example-company.visualstudio.com/Example%20Project/_wiki/wikis/Example-Project.wiki/38/Running-Data-Quality-Checks).


# CELL ********************

%run nb_helper_functions_data_quality

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Execute write if df is not empty
if cleansed_df is not None and cleansed_df.head(1):
    execute_write_to_lakehouse_with_dq_checks(df=cleansed_df, layer='Cleansed', write_mode_cleansed = None)
else: 
    print("No sourced data found for table {table_name}, no dq checks executed")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
