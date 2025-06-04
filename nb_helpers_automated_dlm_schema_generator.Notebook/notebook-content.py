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
# META       "environmentId": "xxx",
# META       "workspaceId": "00000000-0000-0000-0000-000000000000"
# META     }
# META   }
# META }

# MARKDOWN ********************

# #### Generate Sourced - ServiceNow
# ---
# Generic notebook to extract records via REST API from ServiceNow's tables, before storing the raw data within the `Sourced` Lakehouse as parquet format.
# 
# 
# ###### **<u>Step 1: Import common libraries and helper functions</u>**
# 
# - Import any required public libraries and custom functions via `%run` magic command. 
# - For custom functions, import the `nb_helper_functions_parent_caller.py` notebook to collectively bring in all the required custom functions.

# MARKDOWN ********************

# <!-- ###### **<u>Step 2: Define Parameters</u>**
# The following cell is noted as a Parameter cell; default values can be overwritten when the notebook is executed either via DAG calls or Data Factory Pipelines. To 'parameterize' a code cell, click on the `...` 'more command' button on the right as you hover your cursor over the cell and click `[@] Toggle parameter cell` -->

# MARKDOWN ********************

# ###### **<u>Step 2: Extract configurations and table schema</u>**
# - Extract global configuration and table specific configuration defined in `notebooks/nb_configs.py`. 
# - Extract table schema defined in `notebooks/schemas/<source> or <target/<facts> or <dimension>>/`

# CELL ********************

source_dlm_file_name = table_configs["source_dlm_file_name"]
source_dlm_sheet_name = table_configs["source_dlm_sheet_name"]
schema_version = table_configs["schema_version"]
source_dlm_versioned_file_name = f"{source_dlm_file_name}_{schema_version}.xlxs"
api_paged_data_format = table_configs["paged_data"]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Main Code Block
# ---
# ###### **<u>Step 3: Perform ETL</u>**
# - extract API token for ServiceNow system stored in environment based Azure Key Vault
# - initiate ServiceNow reader class and query
# - retrieve records from table specified from parameter cell
# - write records as to Sourced Lakehouse

# CELL ********************

dlm_column_values = {
    "filled_cols": {
        "Filename": lit(source_dlm_file_name),
        "Sheetname": lit(source_dlm_sheet_name),
        "Example": "col(Field_Example_1)",
        "Example2": "col(Field_Example_2)",
        "Example3": "col(Field_Example_3)",
        "Example4": "col(Field_Example_4)"
    },
    "empty_cols": {
        "Definition": "",
        "DataType": "",  
        "Security": "",  
        "Notes": "",     
        "Source": "",    
        "Target": "",    
        "ForeignKey": "",
        "Sourced_DLM_Name": "",
        "CleansedFieldTarget": "",
        "Cleansed_Table_Name": "" 
    }
}

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Handle Paged/NonPaged API Formats
if api_paged_data_format == True:
    df = flatten_data(paged_data)
    df = spark.createDataFrame(df)

    for column in df.columns:
        df = df.withColumn(column, df[column].cast(StringType()))

    df = invert_columns_to_rows(df)
    df = process_dlm_columns_from_config(df, dlm_column_values)
    display(df)

else: 
    for column in df.columns:
        df = df.withColumn(column, df[column].cast(StringType()))
    df = invert_columns_to_rows(df)
    df = process_dlm_columns_from_config(df, dlm_column_values)
    display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
