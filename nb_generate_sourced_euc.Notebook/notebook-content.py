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
# META       "workspaceId": "yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy"
# META     }
# META   }
# META }

# MARKDOWN ********************

# #### Generate Sourced - Client System
# ---
# Generic notebook to extract records via REST API from Client System's tables, before storing the raw data within the `Sourced` Lakehouse as parquet format.
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

# MARKDOWN ********************

# ###### **<u>Step 2: Define Parameters</u>**
# The following cell is noted as a Parameter cell; default values can be overwritten when the notebook is executed either via DAG calls or Data Factory Pipelines. To 'parameterize' a code cell, click on the `...` 'more command' button on the right as you hover your cursor over the cell and click `[@] Toggle parameter cell`

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
source_configs = globals()['client_system']
table_configs = source_configs['source_tables'][table_name]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Main Code Block
# ---
# ###### **<u>Step 4: Perform ETL</u>**
# - extract API token for external system stored in environment based Azure Key Vault
# - initiate external system reader class and query
# - retrieve records from table specified from parameter cell
# - write records as to Sourced Lakehouse

# CELL ********************

df = read_csv_from_abfs(globals()['global_configs']['abfs_path'], source_configs['folder_path'])
write_parquet_to_lakehouse(df, global_configs['sourced_lh_name'], source_configs['name'], table_name, table_configs['schema_version'], trigger_time)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
