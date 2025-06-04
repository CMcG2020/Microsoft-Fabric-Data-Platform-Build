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
# META       "environmentId": "xxx,
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

# MARKDOWN ********************

# ###### **<u>Step 2: Define Parameters</u>**
# The following cell is noted as a Parameter cell; default values can be overwritten when the notebook is executed either via DAG calls or Data Factory Pipelines. To 'parameterize' a code cell, click on the `...` 'more command' button on the right as you hover your cursor over the cell and click `[@] Toggle parameter cell`

# PARAMETERS CELL ********************

trigger_time = "xxx"
table_name = "sys_user_group"

from_date = "xxx"
to_date = "xxx"

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
source_configs = globals()['service_now']
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
# - extract API token for ServiceNow system stored in environment based Azure Key Vault
# - initiate ServiceNow reader class and query
# - retrieve records from table specified from parameter cell
# - write records as to Sourced Lakehouse

# CELL ********************

# check if 'historical' ingest type. For delta load, calculate from and to dates
mode = 'historical' if from_date and to_date and trigger_time else None

load_type = "delta"

if mode:
    print(f'Historical load for table: {table_name}')
elif load_type == 'delta':
    print(f'Delta load for table: {table_name}')
    from_date = (datetime.strptime(trigger_time, '%Y-%m-%dT%H:%M:%SZ') - timedelta(days=table_configs['delta_days'])).strftime('%Y-%m-%dT00:00:00Z')
    to_date = (datetime.strptime(trigger_time, '%Y-%m-%dT%H:%M:%SZ') - timedelta(days=1)).strftime('%Y-%m-%dT23:59:59Z')
elif load_type == 'full':
    print(f'Full load for table: {table_name}')
    from_date = to_date = None
else: 
    raise Exception(f"Unknown load type: {load_type}")

# retrieve credentials
user_name = extract_secret(source_configs['kv_user_name'])
password = extract_secret(source_configs['kv_password_name'])

# initiate Service Now reader class
service_now_reader = ServiceNowTestReader(user_name, password, table_name, load_type, mode)

# extract paginated data
paged_data = service_now_reader.get_data_paged(from_date, to_date)
paged_data = [x for x in paged_data if isinstance(x, dict)]

# write data to Sourced Lakehouse
if paged_data:
   write_parquet_to_lakehouse(
       paged_data, 
       global_configs['sourced_lh_name'], 
       source_configs['name'], 
       table_name, 
       table_configs['schema_version'], 
       trigger_time, 
       'append' if mode else 'overwrite'
       )
else:
   print(f"No records retrieved for table {table_name} for dates between {from_date} and {to_date}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_helpers_automated_dlm_schema_generator

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
