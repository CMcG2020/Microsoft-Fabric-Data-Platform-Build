# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "environment": {
# META       "environmentId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
# META       "workspaceId": "yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy"
# META     }
# META   }
# META }

# MARKDOWN ********************

# #### Generate Sourced - ExampleSystem
# ---
# Generic notebook to extract records via REST API from ExampleSystem tables, before storing the raw data within the `Sourced` Lakehouse as parquet format.
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
source_configs = globals()['example_system']
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
# - extract API token for Example system stored in environment based Azure Key Vault
# - initiate Example system reader class and query
# - retrieve records from table specified from parameter cell
# - write records as to Sourced Lakehouse

# CELL ********************

# extract api token
client_id = extract_secret(source_configs['kv_user_name'])
api_token = extract_secret(source_configs['kv_password_name'])

# Create ExampleSystemReader instance - only pass the required parameters
example_client = ExampleSystemReader(
    client_id=client_id,
    api_token=api_token,
    table_name=table_name
)

try:
  response_data = example_client.make_api_call()

  # Process the response data
  if isinstance(response_data, dict):
      # If the response is a dictionary, look for a key that matches the table name
      # or a key that contains a list of records
      data_key = next((key for key in response_data.keys() if key.lower() == table_name.lower() or isinstance(response_data[key], list)), None)
      
      if data_key:
          table_data = response_data[data_key]
      else:
          table_data = [response_data]  # Wrap the entire response in a list if no suitable key is found
  elif isinstance(response_data, list):
      # If the response is already a list, use it directly
      table_data = response_data
  else:
      raise ValueError(f"Unexpected response format for table {table_name}")

  # write to sourced lakehouse
  write_parquet_to_lakehouse(
      table_data, global_configs['sourced_lh_name'],
      source_configs['name'], table_name,
      table_configs['schema_version'], trigger_time)

  print(f"Successfully retrieved and stored data for {len(table_data)} records from {table_name}.")

except Exception as e:
  print(f"An error occurred while processing {table_name}: {str(e)}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
