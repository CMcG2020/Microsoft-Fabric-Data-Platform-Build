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

# #### Generate Conformed - Dim Ticket
# ---
# Notebook to perform the creation of Dim Ticket, storing the table in the `Conformed` Lakehouse as delta format
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

%run nb_schema_dim_ticket

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

table_name = 'dim_ticket'
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
df_dicts = read_all_required_dataframes(target_table_configs['required_tables'], target_schema, trigger_time)
##### END EXTRACT #####

##### START VALIDATE COUNTS #####
total_count = df_dicts['incident'].count() + df_dicts['u_inf_generic_request'].count() + df_dicts['sc_req_item'].count() + df_dicts['sc_task'].count()
if total_count == 0:
    print(f'No ticket raised in the last 24 hours, ending notebook')
    sys.exit(0)
##### END VALIDATE COUNTS #####


##### START TRANSFORMATION #####
# retrieve smaller subset of sys user
df_sys_user = df_dicts['sys_user'].select(*['SysId', 'Email'])

# retrieve personal schemas
excluded_keys = [primary_key, 'ApplicationKey', 'UserAssignmentGroupKey', 'SupplierKey', 'ChildServiceKey', 'WorkNotesListKey']
incident_personal_schema = [x for x in target_schema if x['field'].endswith('Key') and x['field'] not in excluded_keys and 'incident' in x['from'].keys()]
u_inf_generic_request_personal_schema = [x for x in target_schema if x['field'].endswith('Key') and x['field'] not in excluded_keys and 'u_inf_generic_request' in x['from'].keys()]
sc_req_item_personal_schema = [x for x in target_schema if x['field'].endswith('Key') and x['field'] not in excluded_keys and 'sc_req_item' in x['from'].keys()]
sc_task_personal_schema = [x for x in target_schema if x['field'].endswith('Key') and x['field'] not in excluded_keys and 'sc_task' in x['from'].keys()]

# set duration fields
duration_fields = ['BusinessDuration']

# convert duration strings to second integers (done here ahead of casting to integers), rename fields, pull user
df_incident = df_dicts['incident'] \
    .transform(lambda df: duration_to_seconds(df, duration_fields)) \
    .transform(lambda df: conformed_select_alias_and_cast(df, target_schema, 'incident', 'before')) \
    .transform(lambda df: retrieve_user_email_hash(df, df_sys_user, incident_personal_schema, 'incident')) \
    .withColumnRenamed('UCustomer', 'CustomerName')

df_u_inf_generic_request = df_dicts['u_inf_generic_request'] \
    .transform(lambda df: duration_to_seconds(df, duration_fields)) \
    .transform(lambda df_u_inf_generic_request: conformed_select_alias_and_cast(df_u_inf_generic_request, target_schema, 'u_inf_generic_request', 'before')) \
    .transform(lambda df: retrieve_user_email_hash(df, df_sys_user, u_inf_generic_request_personal_schema, 'u_inf_generic_request')) \
    .withColumnRenamed('UVendor', 'Vendor') \
    .withColumnRenamed('UCustomer', 'CustomerName')

df_sc_req_item = df_dicts['sc_req_item'] \
    .transform(lambda df: duration_to_seconds(df, duration_fields)) \
    .transform(lambda df_sc_req_item: conformed_select_alias_and_cast(df_sc_req_item, target_schema, 'sc_req_item', 'before')) \
    .transform(lambda df: retrieve_user_email_hash(df, df_sys_user, sc_req_item_personal_schema, 'sc_req_item')) \
    .withColumnRenamed('UCustomer', 'CustomerName')

df_sc_task = df_dicts['sc_task'] \
    .transform(lambda df: duration_to_seconds(df, duration_fields)) \
    .transform(lambda df_sc_task: conformed_select_alias_and_cast(df_sc_task, target_schema, 'sc_task', 'before')) \
    .transform(lambda df: retrieve_user_email_hash(df, df_sys_user, sc_task_personal_schema, 'sc_task')) \
    .withColumnRenamed('UCustomer', 'CustomerName')

df_asmt_assessment_instance = df_dicts['asmt_assessment_instance'] \
                              .select("TakenOn", "TaskId", "Number") \
                              .withColumnRenamed("TakenOn", "CsatCompletedDateTime") \
                              .withColumnRenamed("Number", "NumberAlias")

df_asmt_assessment_instance_question = df_dicts['asmt_assessment_instance_question'] \
                                      .select('Instance', 'Category', 'Value') \
                                      .withColumnRenamed("Value", "CsatScore").filter(col("Value") > 0)

df_asmt_assessment = df_asmt_assessment_instance_question.join(
    df_asmt_assessment_instance,
    df_asmt_assessment_instance['NumberAlias'] == df_asmt_assessment_instance_question['Instance'],
    how='left') \
    .transform(lambda df_asmt_assessment: filter_by_column_names(df_asmt_assessment, 'Category', [
    'Informa Service Desk Incident Satisfaction Survey',
    'Informa Service Desk Request Satisfaction Survey']))\
    .transform(lambda df: add_hash_key(df, 'CsatKey', ['TaskId'], globals()['service_now']['name'])) \

# union all ticket dataframes
df = df_incident \
    .unionByName(df_u_inf_generic_request, allowMissingColumns = True) \
    .unionByName(df_sc_req_item, allowMissingColumns = True) \
    .unionByName(df_sc_task, allowMissingColumns = True)

# deduplicate and add non 'personal' related primary and foreign keys
df = df \
    .transform(lambda df: deduplicate_by_keys(df, ['TicketNumber'], ['SysModCount'])) \
    .transform(lambda df: add_hash_key(df, primary_key, ['TicketNumber'], globals()['service_now']['name'])) \
    .transform(lambda df: add_hash_key(df, 'ApplicationKey', ['UApplication'], globals()['service_now']['name'])) \
    .transform(lambda df: add_hash_key(df, 'UserAssignmentGroupKey', ['AssignmentGroup'], globals()['service_now']['name'])) \
    .transform(lambda df: add_hash_key(df, 'SupplierKey', ['Vendor'], globals()['service_now']['name'])) \
    .transform(lambda df: add_hash_key(df, 'ChildServiceKey', ['UService'], globals()['service_now']['name']))


df = df.join(
    df_asmt_assessment,
    df['TicketKey'] == df_asmt_assessment['CsatKey'], how='left') \
    .transform(lambda df: get_most_recent_value(df, "TicketNumber", "CsatCompletedDateTime"))

# re-order, cast, add attributes key and partition columns
attributes = [f['field'] for f in target_schema if f['field'] not in metadata_fields + [primary_key]]
df = df\
    .select(*[F.col(f['field']).cast(f['dataType']) for f in target_schema]) \
    .transform(lambda df: add_hash_key(df, attributes_key, attributes)) \
    .withColumns({"Year": F.year('SysCreatedOn'), "Month": F.month('SysCreatedOn'), "Day": F.dayofmonth('SysCreatedOn')})

##### END TRANSFORMATION #####


# ##### START PRIVACY #####
df, df_privacy = handle_personal_and_sensitive_fields(df, target_schema, primary_key, target_table_configs['partition_by'])
# ##### END PRIVACY ###### 

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
    execute_write_to_lakehouse_with_dq_checks(df=df, layer='Conformed', write_mode_cleansed=None, partition_by = target_table_configs['partition_by'], pii_enabled = False)
except Exception as e:
    errors.append(f"Non-PII Data Check failed: {str(e)}")

#PII Data
if df_privacy:
    try:
        execute_write_to_lakehouse_with_dq_checks(df=df_privacy, layer='Conformed', write_mode_cleansed=None, partition_by = target_table_configs['partition_by'], pii_enabled = True)
    except Exception as e:
        errors.append(f"PII Data Check failed: {str(e)}")

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
