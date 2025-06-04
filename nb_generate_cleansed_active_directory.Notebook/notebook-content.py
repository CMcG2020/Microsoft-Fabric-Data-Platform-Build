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

# #### Generate Cleansed - Azure Active Directory
# ---
# Generic notebook to perform cleansing / enriching activities for AAD data derived from the `Sourced` Lakehouse, before storing the cleansed / enriched data within the `Cleansed` Lakehouse as parquet format
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

%run nb_schema_sourced_active_directory

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
# - Extract nested schema

# CELL ********************

global_configs = globals()['global_configs']  
source_configs = globals()['active_directory']  
table_config = source_configs['source_tables'][table_name]  
schema_version = table_config['schema_version']  # Get schema version number  
schema = globals()[f"schema_{table_name}_v{schema_version}"]  # Get schema object 

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ###### **<u>Step 4: Define functions specifically for Active Directory cleansing</u>**

# CELL ********************

def clean_user_principal_name(df: DataFrame) -> DataFrame:
    """Function to clean UserPrincipalName by removing entries ending with specific pattern. Guest Accounts not required"""
    return df.filter(~F.col('userPrincipalName').endswith('#EXT#@company.onmicrosoft.com'))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Main Code Block
# ---
# ###### **<u>Step 5: Perform ETL</u>**
# - read parquet files as dataframe
# - flatten out nested fields
# - select fields, rename to PascalCase and cast to datatypes defined within DLM
# - add metadata fields
# - write to Cleansed Lakehouse

# CELL ********************

# Read data from the Sourced Lakehouse  
cleansed_df = read_dataframe_batches(  
    lakehouse_name=global_configs['sourced_lh_name'],  
    data_provider=source_configs['name'],  
    data_feed=table_name,  
    schema_version=schema_version,  
    trigger_time=trigger_time  
)

# Create new df with required fields    
required_fields = extact_required_fields(schema, table_name, 'from')   
cleansed_df = cleansed_df.select(*required_fields)    

# Add missing fields    
for field in schema:    
    if field['from'] not in cleansed_df.columns:    
        cleansed_df = cleansed_df.withColumn(field['from'], F.lit(None))       

# Clean UserPrincipalName for both users and groups    
cleansed_df = clean_user_principal_name(cleansed_df)    

# Transform dataframe: rename columns to Pascal case, cast to correct datatypes, add metadata    
cleansed_df = cleansed_df \
    .select([F.col(c['from']).alias(c['to']).cast(c['dataType']) for c in schema]) \
    .transform(lambda cleansed_df: cap_timestamp_fields(cleansed_df)) \
    .transform(lambda cleansed_df: cleansed_type_conversion(cleansed_df, schema, 'to')) \
    .transform(lambda cleansed_df: add_pipeline_metadata(cleansed_df, trigger_time, trigger_time, source_configs['name'], table_name))  

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ###### **Running Data Quality Checks**
# 
# ---
# - [Check the Data Quality Checks Wiki for info on running DQ checks](https://company.visualstudio.com/Project/_wiki/wikis/Project.wiki/38/Running-Data-Quality-Checks).

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
