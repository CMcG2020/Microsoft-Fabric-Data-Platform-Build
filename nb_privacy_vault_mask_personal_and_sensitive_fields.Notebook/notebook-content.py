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

# #### Privacy Vault Activities - Masking
# ---
# Notebook to perform the data masking for personal and sensitive fields across all tables across the Sourced and Conformed layers. Personal and Sensitive fields are defined within individual schema notebooks.
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

%run nb_schema_sourced_service_now

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_schema_sourced_lean_ix

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_schema_sourced_coupa

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_schema_sourced_push_euc_asset

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

# #### Main Code Block
# ---
# ###### **<u>Step 3: Perform Masking Activities</u>**
# Mask data.


# CELL ********************

source_system = ['service_now', 'lean_ix', 'coupa', 'euc']

for source in source_system:
    for table in globals()[source]['source_tables']:
        
        live = globals()[source]['source_tables'][table]['live']
        
        if live:
            provider = globals()[source]['name']
            schema_version = globals()[source]['source_tables'][table]['schema_version']
            schema = globals()[f'schema_{table}_v{schema_version}']
            sourced_lakehouse = globals()['global_configs']['sourced_lh_name']
            cleansed_lakehouse = globals()['global_configs']['cleansed_lh_name']
            
            # sourced
            sourced_df = read_dataframe(
                lakehouse_name = sourced_lakehouse,
                data_provider = provider,
                data_feed = table,
                table_name = None,
                schema_version = schema_version,
                trigger_time = trigger_time,
                required_fields = None
            )
            sourced_df.cache().count()
            
            # cleansed
            cleansed_df = read_dataframe(
                lakehouse_name = cleansed_lakehouse,
                data_provider = provider,
                data_feed = table,
                table_name = None,
                schema_version = schema_version,
                trigger_time = trigger_time,
                required_fields = None
            )
            cleansed_df.cache().count()
            
            mask_personal_and_sensitive_fields(sourced_df, sourced_lakehouse, provider, table, schema, schema_version, trigger_time)
            mask_personal_and_sensitive_fields(cleansed_df, cleansed_lakehouse, provider, table, schema, schema_version, trigger_time)
            
            # add sleep to avoid hitting Fabric api rest call limit
            time.sleep(10)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
