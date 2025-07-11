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

# #### Generate Conformed - Fact User Device Map
# ---
# Notebook to perform the creation of Fact Device Map, storing the table in the `Conformed` Lakehouse as delta format
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

%run nb_schema_fact_user_device_map

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

table_name = 'fact_user_device_map'
conformed_layer = 'facts'

global_configs = globals()['global_configs']
env = globals()['global_configs']['env']
current_date = datetime.strptime(trigger_time, "%Y-%m-%dT%H:%M:%SZ").strftime("%m/%d/%Y")
target_table_configs = globals()[conformed_layer][table_name]
target_schema = globals()[f"schema_{table_name}_v{target_table_configs['schema_version']}"]
table_identifier = f"{target_table_configs['name']}_v{target_table_configs['schema_version']}"
table_path = f"abfss://gs_tdm_{globals()['global_configs']['env']}@onelake.dfs.fabric.microsoft.com/lh_conformed.Lakehouse/Tables/{table_identifier}"

primary_key = target_table_configs['primary_key']
attributes_key = target_table_configs['attributes_key']
user_key = target_table_configs['user_key']
data_key = target_table_configs['data_key']
metadata_fields = global_configs['metadata_fields']

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

table_exists = check_table_exists(table_path)
target_schema_field_values = collect_field_values(target_schema)
create_new_empty_table(target_schema_field_values, table_path)

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
df_conformed = df_dicts['fact_user_device_map']
df_cleansed = df_dicts['push_euc_asset']
##### END EXTRACT #####

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_cleansed = df_cleansed \
    .transform(lambda df_cleansed: add_hash_key(df_cleansed, user_key, ['CurrentUser'])) \
    .transform(lambda df_cleansed: add_hash_key(df_cleansed, primary_key, ['SerialNumber'])) \
    .transform(lambda df_cleansed: remove_null_or_empty_records(df_cleansed, "UserKey")) \
    .transform(lambda df_cleansed: generate_AssignedDate_and_ReleasedDate(df_cleansed, "DeviceKey", "UserKey")) \
    .transform(lambda df_cleansed: add_hash_key(df_cleansed, data_key, ['AssignedDate'], ['ReleaseDate'])) \
    .select(target_schema_field_values)


df = reallocate_device_based_on_user(df_conformed, df_cleansed, "DeviceKey", "UserKey", "AssignedDate", "ReleasedDate")

attributes = [f['field'] for f in target_schema if f['field'] not in metadata_fields + [primary_key]]

df = df \
    .select(*[F.col(f['field']).cast(f['dataType']) for f in target_schema]) \
    .transform(lambda df: add_hash_key(df, attributes_key, attributes))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

delta_writer(
    df = df, 
    lakehouse_name = global_configs['conformed_lh_name'], 
    table = target_table_configs['name'], 
    schema_version = target_table_configs['schema_version'], 
    write_type = target_table_configs['write_type'], 
    primary_key = primary_key, 
    attributes_key = attributes_key
    )

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
