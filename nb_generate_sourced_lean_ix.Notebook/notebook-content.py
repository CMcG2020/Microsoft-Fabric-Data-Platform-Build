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

# #### Generate Sourced - External API
# ---
# Generic notebook to extract records via GraphQL from an external API's fact sheets, before storing the data within the `Sourced` Lakehouse as parquet format.
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

%run nb_schema_sourced_external_api

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
source_configs = globals()['external_api']
table_configs = source_configs['source_tables'][table_name]
schema = globals()[f"schema_{table_name}_v{table_configs['schema_version']}"]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Main Code Block
# ---
# ###### **<u>Step 4: Perform ETL</u>**
# 
# - extract API token for external API system stored in environment based Azure Key Vault
# - generate graphql query based on schema
# - initiate external API reader class and query
# - retrieve records from fact sheet specified from parameter cell
# - write records as to Sourced Lakehouse

# CELL ********************

# retrieve api token
api_token = extract_secret(source_configs['kv_password_name'])

# generate graphql query
graphql_query = generate_graphql_query(table_name, schema)

# initiate external api reader class
external_api_reader = GraphQLAPIClient(api_token, graphql_query)

# extract data
response = external_api_reader.execute_graphql_query()
if response is None:
    raise ValueError("The response from the GraphQL query is None.")
df = external_api_reader.extract_edges_to_spark_dataframe(response)

# write to lakehouse
write_parquet_to_lakehouse(
    df, global_configs['sourced_lh_name'],
    source_configs['name'], table_name,
    table_configs['schema_version'], trigger_time)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
