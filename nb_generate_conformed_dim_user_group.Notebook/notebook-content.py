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

# #### Generate Conformed - Dim User Group
# ---
# Notebook to perform the creation of Dim User Group, storing the table in the `Conformed` Lakehouse as delta format
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

%run nb_schema_dim_user_group

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

table_name = 'dim_user_group'
conformed_layer = 'dimensions'

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
df_dicts = read_all_required_dataframes(target_table_configs['required_tables'], target_schema, trigger_time, False)
##### END EXTRACT #####

##### START TRANSFORMATION #####
# Transform ServiceNow data
df_servicenow = df_dicts['sys_user_group'] \
  .withColumn('UserGroupType', F.col('SourceSystem')) \
  .transform(lambda df: conformed_select_alias_and_cast(df, target_schema, 'sys_user_group', 'before')) \
  .transform(lambda df: add_hash_key(df, 'UserGroupKey', ['UserGroupName'], globals()['service_now']['name'])) \

# Transform AAD data
df_aad = df_dicts['groups'] \
  .withColumn('UserGroupType', F.col('SourceSystem')) \
  .transform(lambda df: conformed_select_alias_and_cast(df, target_schema, 'groups', 'before')) \
  .transform(lambda df: add_hash_key(df, 'UserGroupKey', ['UserGroupName'], globals()['active_directory']['name'])) \

# Union the dataframes
df = df_servicenow.unionByName(df_aad, allowMissingColumns=True)

# Add attributes hash key
attributes = [f['field'] for f in target_schema if f['field'] not in metadata_fields + [primary_key]]
df = df.transform(lambda df: add_hash_key(df, attributes_key, attributes))

# Drop both NULLs (known issue at source to be reomved once resolved) and duplicates in UserGroupKey column as only require one instance to match
df = df.filter(F.col('UserGroupKey').isNotNull()) \
       .dropDuplicates(['UserGroupKey'])

##### START PRIVACY #####
df, df_privacy = handle_personal_and_sensitive_fields(df, target_schema, primary_key)
##### END PRIVACY ######     

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ###### **Running Data Quality Checks**
# 
# ---
# - [Check the Data Quality Checks Wiki for info on running DQ checks](https://informaeds.visualstudio.com/Global%20Support/_wiki/wikis/Global-Support.wiki/38/Running-Data-Quality-Checks).

# CELL ********************

%run nb_helper_functions_data_quality

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Variable to store error data from runs (if any)
errors = []

##### START WRITE #####
try:
    #Non PII Data
    execute_write_to_lakehouse_with_dq_checks(df=df, layer='Conformed', write_mode_cleansed=None, partition_by = None, pii_enabled = False)
except Exception as e:
    errors.append(f"Non-PII Data Check failed: {str(e)}")

#PII Data
if df_privacy:
    try:
        execute_write_to_lakehouse_with_dq_checks(df=df_privacy, layer='Conformed', write_mode_cleansed=None, partition_by = None, pii_enabled = True)
    except Exception as e:
        errors.append(f"PII Data Check failed: {str(e)}")
##### END WRITE #####

# Raise error if any checks failed
if errors:
    raise Exception("One or more data quality checks failed:\n" + "\n".join(errors))
else:
    print("Both Non-PII and PII Data Quality Checks completed successfully.")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
