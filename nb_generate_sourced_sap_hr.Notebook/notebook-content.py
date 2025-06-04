# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "environment": {
# META       "environmentId": "894291a9-f8d5-4ea0-8d4d-a41d3d9b7541",
# META       "workspaceId": "00000000-0000-0000-0000-000000000000"
# META     }
# META   }
# META }

# MARKDOWN ********************

# ### Generate Sourced - SAP HR
# ---
# Generic notebook to extract records via API from SAP HR tables, before storing the raw data within the `Sourced` Lakehouse as parquet format.
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

%run nb_schema_sourced_sap_hr

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
# - Extract table schema defined in `notebooks/schemas/<source> or <target/<facts> or <dimension>>/

# CELL ********************

global_configs = globals()['global_configs']
source_configs = globals()['sap_hr']

table_configs = source_configs['source_tables'][table_name]
source_schema = globals()[f"schema_{table_name}_v{table_configs['schema_version']}"]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Main Code Block
# ---
# ###### **<u>Step 4: Perform ETL</u>**
# - extract API token for SAP HR system stored in environment based Azure Key Vault
# - initiate SAP HR reader class and query
# - retrieve records from table specified from parameter cell
# - write records as to Sourced Lakehouse

# CELL ********************

# Extract secrets
api_username = extract_secret(source_configs['kv_username'])
api_password = extract_secret(source_configs['kv_password'])
api_base_url = extract_secret(source_configs['api_base_url'])

# Initialize SapHrReader
reader = SapHrReader(
  username=api_username,
  password=api_password,
  api_base_url=api_base_url,
)

# Get data
data = reader.get_data()

# Write to lakehouse
write_parquet_to_lakehouse(
  data,
  global_configs['sourced_lh_name'],
  source_configs['name'],
  table_name,
  table_configs['schema_version'],
  trigger_time
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
