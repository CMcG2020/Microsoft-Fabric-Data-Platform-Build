# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "xxx",
# META       "default_lakehouse_name": "lh_cleansed",
# META       "default_lakehouse_workspace_id": "xxx"
# META     },
# META     "environment": {
# META       "environmentId": "xxx",
# META       "workspaceId": "00000000-0000-0000-0000-000000000000"
# META     }
# META   }
# META }

# MARKDOWN ********************

# #### System Integration Tests (SIT)
# ---
# This process involves executing system integration tests (SIT) to test the end to end ETL process from ingestion data via API within the `Sourced` Lakehouse to the final fact and dimension tables within the `Conformed` Lakehouse. These tests are orchestrated through a Directed Acyclic Graph (DAG), allowing multiple notebooks to run within a single session. 
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

# MARKDOWN ********************

# ###### **<u>Step 2: Clear down lakehouses</u>**
# 
# Before commencing SIT, it is imperative to ensure a clean state. This involves systematically clearing all previously generated parquet files in the Sourced and Cleansed and removing any tables created in the Conformed layer from previous runs. 

# CELL ********************

#clear_down_lakehouses()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ###### **<u>Step 3: Extract configurations</u>**
# - Extract integration test configurations

# CELL ********************

global_configs = globals()['global_configs']
sourced_nb = global_configs['sourced_nb_name']
cleansed_nb = global_configs['cleansed_nb_name']
conformed_nb = global_configs['conformed_nb_name']
harmonized_nb = global_configs['harmonised_nb_name']

dag_configs = globals()['orchestration_configs']['dag']['integration_test']
activity_configs = globals()['orchestration_configs']['activity']['integration_test']

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ###### **<u>Step 4: Define conformed dependency</u>**
# ---
# Define the dependencies for conformed layer

# CELL ********************

# application dependencies
application_dependency = [
    f"{cleansed_nb.format('lean_ix')}_Application",
    f"{cleansed_nb.format('service_now')}_cmdb_ci_appl",
    f"{cleansed_nb.format('service_now')}_sys_user"
]
application_map_dependency = [
    conformed_nb.format('dim_application_source'),
    conformed_nb.format('dim_application')
]
application_harmonisation_dependency = [
    conformed_nb.format('dim_application_source'),
    conformed_nb.format('dim_application'),
    conformed_nb.format('dim_application_map')]

# supplier dependencies
supplier_dependency = [f"{cleansed_nb.format('service_now')}_core_company", f"{cleansed_nb.format('lean_ix')}_Provider", f"{cleansed_nb.format('coupa')}_suppliers"]
supplier_map_dependency = [conformed_nb.format('dim_supplier_source'), conformed_nb.format('dim_supplier')]
supplier_harmonisation_dependency = [conformed_nb.format('dim_supplier_source'), conformed_nb.format('dim_supplier'), conformed_nb.format('dim_supplier_map')]

# dim ticket dependency
dim_ticket_dependency = [
    f"{cleansed_nb.format('service_now')}_incident", 
    f"{cleansed_nb.format('service_now')}_u_inf_generic_request", 
    f"{cleansed_nb.format('service_now')}_sc_req_item", 
    f"{cleansed_nb.format('service_now')}_sc_task", 
    f"{cleansed_nb.format('service_now')}_sys_user", 
    f"{cleansed_nb.format('service_now')}_asmt_assessment_instance", 
    f"{cleansed_nb.format('service_now')}_asmt_assessment_instance_question", 
]

# dim service dependency
dim_service_dependency = [f"{cleansed_nb.format('service_now')}_cmdb_ci_service", f"{cleansed_nb.format('service_now')}_cmdb_rel_ci"]

# fact ticket event dependency
fact_ticket_event_dependecy = [f"{cleansed_nb.format('service_now')}_task_sla"]

# fact outage dependency
fact_outage_dependecy = [f"{cleansed_nb.format('service_now')}_cmdb_ci_outage"]

# fact user device map dependency
fact_user_device_map_dependency = [f"{cleansed_nb.format('euc')}_push_euc_asset"]

# dim device dependency
dim_device_dependency = [f"{cleansed_nb.format('euc')}_push_euc_asset"]

# dim device history dependency
dim_device_history_dependency = [f"{cleansed_nb.format('euc')}_push_euc_asset"]

# dim app interface dependency
dim_app_interface_dependency = [f"{cleansed_nb.format('lean_ix')}_Interface"]

# dim domain interface dependency
dim_domain_dependency = [f"{cleansed_nb.format('csc')}_push_csc_domain_name"]

# fact app interface dependency
fact_app_interface_map_dependency = [f"{cleansed_nb.format('lean_ix')}_Interface"]

# fact contract dependency
fact_contract_dependency = [f"{cleansed_nb.format('coupa')}_contracts"]

# dim app classiciation dependency
dim_app_classiciation_dependency = [
    f"{cleansed_nb.format('lean_ix')}_BusinessCapability",
    f"{cleansed_nb.format('lean_ix')}_DataObject",
    f"{cleansed_nb.format('lean_ix')}_ITComponent"
    ]

# fact app classiciation dependency
fact_app_classiciation_map_dependency = [
    f"{cleansed_nb.format('lean_ix')}_BusinessCapability",
    f"{cleansed_nb.format('lean_ix')}_DataObject",
    f"{cleansed_nb.format('lean_ix')}_ITComponent"
    ]

# dim user group dependency
dim_user_group_dependency = [
    f"{cleansed_nb.format('active_directory')}_users",
    f"{cleansed_nb.format('service_now')}_sys_user_group"
    ]

# fact user group map dependency
fact_user_group__map_dependency = [
    f"{cleansed_nb.format('active_directory')}_users",
    f"{cleansed_nb.format('service_now')}_sys_user_grmember"
    ]

# dim user dependency
dim_user_dependency = [
    f"{cleansed_nb.format('sap_hr')}_sap_employee",
    f"{cleansed_nb.format('oracle_hr')}_Employee",
    f"{cleansed_nb.format('active_directory')}_users"
    ]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ###### **<u>Step 5: Build the DAG</u>**
# ---
# To add tests, add an activity (using the `generate_activity` helper function) according to its medallion layer below. 

# CELL ********************

trigger_time = '2024-01-01T00:00:00Z'
activity_type = 'integration_test'

# add sourced activites
sourced = [
    generate_activity(sourced_nb.format('lean_ix'), {'trigger_time': trigger_time, 'table_name': 'Interface'}, activity_type),
    generate_activity(sourced_nb.format('lean_ix'), {'trigger_time': trigger_time, 'table_name': 'Provider'}, activity_type),
    generate_activity(sourced_nb.format('lean_ix'), {'trigger_time': trigger_time, 'table_name': 'BusinessCapability'}, activity_type),
    generate_activity(sourced_nb.format('lean_ix'), {'trigger_time': trigger_time, 'table_name': 'DataObject'}, activity_type),
    generate_activity(sourced_nb.format('lean_ix'), {'trigger_time': trigger_time, 'table_name': 'ITComponent'}, activity_type),
    generate_activity(sourced_nb.format('lean_ix'), {'trigger_time': trigger_time, 'table_name': 'Application'}, activity_type),
    generate_activity(sourced_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'cmdb_ci_appl'}, activity_type),
    generate_activity(sourced_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'incident'}, activity_type),
    generate_activity(sourced_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'u_inf_generic_request'}, activity_type),
    # generate_activity(sourced_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'sc_req_item'}, activity_type),
    generate_activity(sourced_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'sc_task'}, activity_type),
    generate_activity(sourced_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'sys_user'}, activity_type),
    generate_activity(sourced_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'task_sla'}, activity_type),
    generate_activity(sourced_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'core_company'}, activity_type),
    generate_activity(sourced_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'cmdb_ci_service'}, activity_type),
    generate_activity(sourced_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'cmdb_rel_ci'}, activity_type),
    generate_activity(sourced_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'cmdb_ci_outage'}, activity_type),
    generate_activity(sourced_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'sys_user_grmember'}, activity_type),
    generate_activity(sourced_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'sys_user_group'}, activity_type),
    generate_activity(sourced_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'asmt_assessment_instance'}, activity_type),
    generate_activity(sourced_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'asmt_assessment_instance_question'}, activity_type), 
    generate_activity(sourced_nb.format('coupa'), {'trigger_time': trigger_time, 'table_name': 'suppliers'}),
    generate_activity(sourced_nb.format('coupa'), {'trigger_time': trigger_time, 'table_name': 'contracts'}, activity_type, [f"{sourced_nb.format('coupa')}_suppliers"]),
    generate_activity(sourced_nb.format('euc'), {'trigger_time': trigger_time, 'table_name': 'push_euc_asset'}, activity_type),
    generate_activity(sourced_nb.format('csc'), {'trigger_time': trigger_time, 'table_name': 'push_csc_domain_name'}, activity_type),
    # generate_activity(sourced_nb.format('active_directory'), {'trigger_time': trigger_time, 'table_name': 'users'}, activity_type), #runtime too long 
    generate_activity(sourced_nb.format('smartsheet'), {'trigger_time': trigger_time, 'table_name': '4612826324750212'}, activity_type),
    generate_activity(sourced_nb.format('smartsheet'), {'trigger_time': trigger_time, 'table_name': '6425435520847748'}, activity_type),
    generate_activity(sourced_nb.format('oracle_hr'), {'trigger_time': trigger_time, 'table_name': 'Employee'}, activity_type),
    generate_activity(sourced_nb.format('sap_hr'), {'trigger_time': trigger_time, 'table_name': 'sap_employee'}, activity_type)
    ]

# add cleansed activites
cleansed = [
    generate_activity(cleansed_nb.format('lean_ix'), {'trigger_time': trigger_time, 'table_name': 'Interface'}, activity_type),
    generate_activity(cleansed_nb.format('lean_ix'), {'trigger_time': trigger_time, 'table_name': 'Provider'}, activity_type),
    generate_activity(cleansed_nb.format('lean_ix'), {'trigger_time': trigger_time, 'table_name': 'BusinessCapability'}, activity_type),
    generate_activity(cleansed_nb.format('lean_ix'), {'trigger_time': trigger_time, 'table_name': 'DataObject'}, activity_type),
    generate_activity(cleansed_nb.format('lean_ix'), {'trigger_time': trigger_time, 'table_name': 'ITComponent'}, activity_type),
    generate_activity(cleansed_nb.format('lean_ix'), {'trigger_time': trigger_time, 'table_name': 'Application'}, activity_type),
    generate_activity(cleansed_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'cmdb_ci_appl'}, activity_type),
    generate_activity(cleansed_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'incident'}, activity_type),
    generate_activity(cleansed_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'u_inf_generic_request'}, activity_type),
    # generate_activity(cleansed_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'sc_req_item'}, activity_type),
    generate_activity(cleansed_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'sc_task'}, activity_type),
    generate_activity(cleansed_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'sys_user'}, activity_type),
    generate_activity(cleansed_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'task_sla'}, activity_type),
    generate_activity(cleansed_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'cmdb_ci_outage'}, activity_type),
    generate_activity(cleansed_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'asmt_assessment_instance'}, activity_type),
    generate_activity(cleansed_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'asmt_assessment_instance_question'}, activity_type), 
    generate_activity(cleansed_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'core_company'}, activity_type),
    generate_activity(cleansed_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'sys_user_grmember'}, activity_type),
    generate_activity(cleansed_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'sys_user_group'}, activity_type),
    generate_activity(cleansed_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'cmdb_ci_service'}, activity_type),
    generate_activity(cleansed_nb.format('service_now'), {'trigger_time': trigger_time, 'table_name': 'cmdb_rel_ci'}, activity_type),
    generate_activity(cleansed_nb.format('coupa'), {'trigger_time': trigger_time, 'table_name': 'suppliers'}, activity_type),
    generate_activity(cleansed_nb.format('coupa'), {'trigger_time': trigger_time, 'table_name': 'contracts'}, activity_type),
    generate_activity(cleansed_nb.format('euc'), {'trigger_time': trigger_time, 'table_name': 'push_euc_asset'}, activity_type),
    generate_activity(cleansed_nb.format('csc'), {'trigger_time': trigger_time, 'table_name': 'push_csc_domain_name'}, activity_type),
    # generate_activity(cleansed_nb.format('active_directory'), {'trigger_time': trigger_time, 'table_name': 'users'}, activity_type), #runtime too long
    generate_activity(cleansed_nb.format('oracle_hr'), {'trigger_time': trigger_time, 'table_name': 'Employee'}, activity_type),
    generate_activity(cleansed_nb.format('sap_hr'), {'trigger_time': trigger_time, 'table_name': 'sap_employee'}, activity_type)
    ]

# add conformed activities
conformed = [
    generate_activity(conformed_nb.format('dim_application_source'), {'trigger_time': trigger_time}, activity_type, application_dependency),
    generate_activity(conformed_nb.format('dim_application'), {'trigger_time': trigger_time}, activity_type, application_dependency), 
    generate_activity(conformed_nb.format('dim_application_map'), {'trigger_time': trigger_time}, activity_type, application_map_dependency), 
    generate_activity(harmonized_nb.format('application'), {'trigger_time': trigger_time}, activity_type, application_harmonisation_dependency), 
    # generate_activity(conformed_nb.format('dim_ticket'), {'trigger_time': trigger_time}, activity_type, dim_ticket_dependency),
    # generate_activity(conformed_nb.format('dim_service'), {'trigger_time': trigger_time}, activity_type, dim_service_dependency),
    # generate_activity(conformed_nb.format('dim_date'), {'trigger_time': trigger_time}, activity_type),
    # generate_activity(conformed_nb.format('dim_supplier_source'), {'trigger_time': trigger_time}, activity_type, supplier_dependency),
    # generate_activity(conformed_nb.format('dim_supplier'), {'trigger_time': trigger_time}, activity_type, supplier_dependency),
    # generate_activity(conformed_nb.format('dim_supplier_map'), {'trigger_time': trigger_time}, activity_type, supplier_map_dependency),
    # generate_activity(harmonized_nb.format('supplier'), {'trigger_time': trigger_time}, activity_type, supplier_harmonisation_dependency),
    # generate_activity(conformed_nb.format('dim_device'), {'trigger_time': trigger_time}, activity_type, dim_device_dependency),
    # generate_activity(conformed_nb.format('dim_device_history'), {'trigger_time': trigger_time}, activity_type, dim_device_history_dependency),
    # generate_activity(conformed_nb.format('dim_app_interface'), {'trigger_time': trigger_time}, activity_type, dim_app_interface_dependency),
    # generate_activity(conformed_nb.format('dim_domain'), {'trigger_time': trigger_time}, activity_type, dim_domain_dependency),
    # generate_activity(conformed_nb.format('dim_app_classification'), {'trigger_time': trigger_time}, activity_type, dim_app_classiciation_dependency),
    # generate_activity(conformed_nb.format('fact_app_classification_map'), {'trigger_time': trigger_time}, activity_type, fact_app_classiciation_map_dependency),
    # generate_activity(conformed_nb.format('fact_app_interface_map'), {'trigger_time': trigger_time}, activity_type, fact_app_interface_map_dependency),
    # generate_activity(conformed_nb.format('fact_contract'), {'trigger_time': trigger_time}, activity_type, fact_contract_dependency),
    # generate_activity(conformed_nb.format('fact_user_device_map'), {'trigger_time': trigger_time}, activity_type, fact_user_device_map_dependency),
    generate_activity(conformed_nb.format('fact_ticket_event'), {'trigger_time': trigger_time}, activity_type, fact_ticket_event_dependecy),
    generate_activity(conformed_nb.format('fact_outage'), {'trigger_time': trigger_time}, activity_type, fact_outage_dependecy),
    # generate_activity(conformed_nb.format('dim_user_group'), {'trigger_time': trigger_time}, activity_type, dim_user_group_dependency),
    # generate_activity(conformed_nb.format('fact_user_group_map'), {'trigger_time': trigger_time}, activity_type, fact_user_group__map_dependency),
    # generate_activity(conformed_nb.format('dim_user'), {'trigger_time': trigger_time}, activity_type, dim_user_dependency),
    ]

privacy = [
    {
        "name": 'nb_privacy_vault_mask_personal_and_sensitive_fields',
        "path": 'nb_privacy_vault_mask_personal_and_sensitive_fields',
        "args": {'trigger_time': trigger_time},
        "dependencies": [],
        "timeoutPerCellInSeconds": activity_configs['timeout_per_cell'],
        "retry": activity_configs['retries'],
        "retryIntervalInSeconds": activity_configs['retry_interval']
    }
]

# build the DAG
normal_dag = {"activities": [activity for activity in sourced + cleansed + conformed], "timeoutInSeconds": dag_configs['timeout_in_seconds'], "concurrency": dag_configs['concurrency']}
privacy_dag = {"activities": privacy, "timeoutInSeconds": dag_configs['timeout_in_seconds'], "concurrency": dag_configs['concurrency']}


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ###### **<u>Step 5: Run SIT</u>**
# ---
# Run the below cell to start the integration tests and masking

# CELL ********************

try:
    mssparkutils.notebook.runMultiple(normal_dag, {
        "displayDAGViaGraphviz": dag_configs['display_dag_via_graph_viz'], 
        "DAGLayout": dag_configs['dag_layout'], 
        "DAGSize": dag_configs['dag_size']
    })
except Exception as e:
     print(f"An error occurred while running normal_dag: {e}")
finally:
    # This block will execute regardless of whether the first piece succeeds or fails
    mssparkutils.notebook.runMultiple(privacy_dag, {
        "displayDAGViaGraphviz": dag_configs['display_dag_via_graph_viz'], 
        "DAGLayout": dag_configs['dag_layout'], 
        "DAGSize": dag_configs['dag_size']
    })

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
