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

# #### Generate Conformed - Dim Application Source
# ---
# Notebook to perform the creation of Dim Application Source, storing the table in the `Conformed` Lakehouse as delta format
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

%run nb_schema_dim_application_source

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

table_name = 'dim_application_source'
conformed_layer = 'dimensions'

global_configs = globals()['global_configs']
target_table_configs = globals()[conformed_layer][table_name]
target_schema = globals()[f"schema_{table_name}_v{target_table_configs['schema_version']}"]

primary_key = target_table_configs['primary_key']
attributes_key = target_table_configs['attributes_key']
supplier_key = target_table_configs['supplier_key']
domain_key = target_table_configs['domain_key']
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
# read in all required dataframes
df_dicts = read_all_required_dataframes(target_table_configs['required_tables'], target_schema, trigger_time, False)
##### END EXTRACT #####


##### START TRANSFORMATION #####
# leanix - application transformations
df_application = df_dicts['Application'] \
    .filter((F.col('Name').isNotNull()) | (F.col('Name') != '')) \
    .withColumn('IsActive', F.when(F.col('Status') == 'ACTIVE', F.lit(True)).otherwise(F.lit(False))) \
    .withColumn('BusinessCriticality', F.initcap(F.regexp_replace("BusinessCriticality", "(?=[A-Z])", " "))) \
    .transform(lambda df_application: conformed_select_alias_and_cast(df_application, target_schema, 'Application', 'before')) \
    .transform(lambda df_application: add_hash_key(df_application, primary_key, ['Name'], globals()['lean_ix']['name']))

# servicenow - cmdb_ci_appl transformations - PK deduplicated due to known issue at source, can be removed once resolved
df_cmdb_ci_appl = df_dicts['cmdb_ci_appl'] \
    .filter((F.col('Name').isNotNull()) | (F.col('Name') != '')) \
    .transform(lambda df_cmdb_ci_appl: duration_to_seconds(df_cmdb_ci_appl, ['USystemRpo', 'USystemRto'])) \
    .transform(lambda df_cmdb_ci_appl: conformed_select_alias_and_cast(df_cmdb_ci_appl, target_schema, 'cmdb_ci_appl', 'before')) \
    .transform(lambda df_cmdb_ci_appl: add_hash_key(df_cmdb_ci_appl, primary_key, ['Name'], globals()['service_now']['name'])) \
    .transform(lambda df_cmdb_ci_appl: add_hash_key(df_cmdb_ci_appl, supplier_key, ['Vendor'], globals()['service_now']['name'])) \
    .transform(lambda df_cmdb_ci_appl: add_hash_key(df_cmdb_ci_appl, domain_key, ['Fqdn'])) \
    .transform(lambda df: deduplicate_by_keys(df, ['Name'], ['LastUpdatedOnDateTime']))

# servicenow - create personal related foreign keys - only extract fields ending with 'Key' from servicenow
personal_schema = [x for x in target_schema if x['field'].endswith('Key') and x['field'] != primary_key and 'cmdb_ci_appl' in x['from'].keys()]
df_cmdb_ci_appl = retrieve_user_email_hash(df_cmdb_ci_appl, df_dicts['sys_user'].select(*['SysId', 'Email']), personal_schema, 'cmdb_ci_appl')

# union both dataframes, re-order fields and remove key value identified as causing duplicates
attributes = [f['field'] for f in target_schema if f['field'] not in metadata_fields + [primary_key]]
union_df = df_application \
    .unionByName(df_cmdb_ci_appl, allowMissingColumns=True) \
    .select(*[F.col(f['field']) for f in target_schema]) \
    .transform(lambda df: add_hash_key(df, attributes_key, attributes))
df = union_df.where(~(union_df.ApplicationKey.isin([-849862343517725175, 5896695335020484737])))
##### END TRANSFORMATION #####


##### START PRIVACY #####
# Note: masking only happens at the harmonisation stage
##### END PRIVACY #####

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

try:
    #Non PII Data
    execute_write_to_lakehouse_with_dq_checks(df=df, layer='Conformed', write_mode_cleansed=None, partition_by = None, pii_enabled = False)
except Exception as e:
    errors.append(f"Non-PII Data Check failed: {str(e)}")

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
