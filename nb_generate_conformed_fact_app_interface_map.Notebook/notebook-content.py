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

# #### Generate Conformed - Fact App Interface Map
# ---
# Notebook to perform the creation of Fact App Interface Map, storing the table in the `Conformed` Lakehouse as delta format
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

%run nb_schema_fact_app_interface_map

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

table_name = 'fact_app_interface_map'
conformed_layer = 'facts'

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
df_dicts = read_all_required_dataframes(target_table_configs['required_tables'], target_schema, trigger_time)
##### END EXTRACT #####


##### START TRANSFORMATION #####
# explode consumer application into individual rows and add foreign keys
df = df_dicts['Interface'] \
    .withColumn('RelInterfaceToConsumerApplication', F.explode('RelInterfaceToConsumerApplication')) \
    .transform(lambda df: add_hash_key(df, 'AppInterfaceKey', ['Name'], globals()['lean_ix']['name'])) \
    .transform(lambda df: add_hash_key(df, 'ApplicationProviderKey', ['RelInterfaceToProviderApplication'], globals()['lean_ix']['name'])) \
    .transform(lambda df: add_hash_key(df, 'ApplicationConsumerKey', ['RelInterfaceToConsumerApplication'], globals()['lean_ix']['name'])) \
    .transform(lambda df: conformed_select_alias_and_cast(df, target_schema, 'Interface'))
##### END TRANSFORMATION #####


##### START PRIVACY #####
df, df_privacy = handle_personal_and_sensitive_fields(df, target_schema, primary_key)
##### END PRIVACY ######  


##### START WRITE #####
# conformed
delta_writer(
    df = df, 
    lakehouse_name = global_configs['conformed_lh_name'], 
    table = target_table_configs['name'], 
    schema_version = target_table_configs['schema_version'], 
    write_type = target_table_configs['write_type']
    )

# privacy
if df_privacy:
    delta_writer(
        df = df_privacy, 
        lakehouse_name = global_configs['conformed_pii_lh_name'], 
        table = f"{target_table_configs['name']}_pii", 
        schema_version = target_table_configs['schema_version'], 
        write_type = target_table_configs['write_type']
        )
##### END WRITE #####

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
