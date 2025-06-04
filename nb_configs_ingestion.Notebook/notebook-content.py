# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# #### Sourced and Cleansed (Ingestion) Configs
# ---
# Notebook to store all configurations for the sourced / cleansed source systems.

# MARKDOWN ********************

# ##### **ServiceNow**

# CELL ********************

service_now = {
    'name': 'xxx',
    'kv_user_name': 'xxx',
    'kv_password_name': 'xxx',
    'source_tables': {
        'cmdb_ci_appl': { 
            'load_type': 'full',
            'schema_version': 1,
            'live': True,
            'primary_key': 'Name',
            'dq_check_file': '/lakehouse/default/Files/DataQuality/Cleansed/sd_service_now_cmdb_ci_appl_checks.yaml'
            },
        'task_sla': {
            'load_type': 'delta',
            'delta_days': 1,
            'schema_version': 1,
            'live': True,
            'dq_check_file': '/lakehouse/default/Files/DataQuality/Cleansed/sd_service_now_task_sla_checks.yaml'
            },
        'incident': {
            'load_type': 'delta',
            'delta_days': 1,
            'schema_version': 1,
            'live': True,
            'primary_key': 'Number',
            'non_nullable_cols': ['Number', 'ReceiptDate', 'AllocatedDate', 'SourceSystem']
            },
        'u_inf_generic_request': {
            'load_type': 'delta',
            'delta_days': 1,
            'schema_version': 1,
            'live': True,
            'primary_key': 'Number',
            'non_nullable_cols': ['Number']
            },
        'sc_req_item': {
            'load_type': 'delta',
            'delta_days': 1,
            'schema_version': 1,
            'live': True,
            'primary_key': 'SysId',
            'non_nullable_cols': ['SysId']
            },
        'sc_task': {
            'load_type': 'delta',
            'delta_days': 1,
            'schema_version': 1,
            'live': True,
            'primary_key': 'Number',
            'non_nullable_cols': ['Number', 'ReceiptDate', 'AllocatedDate', 'SourceSystem']
            },
        'core_company': {
            'load_type': 'full',
            'schema_version': 1,
            'live': False,
            'source_dlm_file_name': 'xxx', # TEST VALUE - TO BE REPLACED ONCE DLM HAS BEEN DECIDED ON
            'source_dlm_sheet_name': "PullApplication", # TEST VALUE - TO BE REPLACED ONCE DLM HAS BEEN DECIDED ON
            'paged_data': True,
            'primary_key': 'Name',
            'non_nullable_cols': ['Name']
            },
        'sys_user': {
            'load_type': 'full',
            'schema_version': 1,
            'live': True,
            'dq_check_file': '/lakehouse/default/Files/DataQuality/Cleansed/sd_service_now_sys_user_checks.yaml'
            },
        'cmdb_ci_service': {
            'load_type': 'full',
            'schema_version': 1,
            'live': False,
            'source_dlm_file_name': 'xxx', # TEST VALUE - TO BE REPLACED ONCE DLM HAS BEEN DECIDED ON
            'source_dlm_sheet_name': "PullApplication", # TEST VALUE - TO BE REPLACED ONCE DLM HAS BEEN DECIDED ON
            'paged_data': True,
            'primary_key': 'Name',
            'non_nullable_cols': ['Name']
            },
        'cmdb_rel_ci': {
            'load_type': 'full',
            'schema_version': 1,
            'live': False,
            'source_dlm_file_name': 'xxx', # TEST VALUE - TO BE REPLACED ONCE DLM HAS BEEN DECIDED ON
            'source_dlm_sheet_name': "PullApplication", # TEST VALUE - TO BE REPLACED ONCE DLM HAS BEEN DECIDED ON
            'paged_data': True,
            'primary_key': 'Child',
            'non_nullable_cols': ['Child']
            },
        'asmt_assessment_instance': {
            'load_type': 'delta',
            'delta_days': 1,
            'schema_version': 1,
            'live': True,
            'primary_key': 'Number',
            'non_nullable_cols': ['Number'],
            'dq_check_file': '/lakehouse/default/Files/DataQuality/Cleansed/sd_service_now_asmt_assessment_instance_checks.yaml'
            },
        'asmt_assessment_instance_question': {
            'load_type': 'delta',
            'delta_days': 1,
            'schema_version': 1,
            'live': True,
            'primary_key': 'Instance',
            'non_nullable_cols': ['Instance'],
            'dq_check_file': '/lakehouse/default/Files/DataQuality/Cleansed/sd_service_now_asmt_assessment_instance_question_checks.yaml'
            },
        'u_servicedesk_survey_results': {
            'load_type': 'delta',
            'delta_days': 1,
            'schema_version': 1,
            'live': False,
            'dq_check_file': '/lakehouse/default/Files/DataQuality/Cleansed/sd_service_now_u_servicedesk_survey_results_checks.yaml'
            },
        'cmdb_ci_outage': {
            'load_type': 'full',
            'schema_version': 1,
            'live': True,
            'source_dlm_file_name': 'xxx', # TEST VALUE - TO BE REPLACED ONCE DLM HAS BEEN DECIDED ON
            'source_dlm_sheet_name': "PullApplication", # TEST VALUE - TO BE REPLACED ONCE DLM HAS BEEN DECIDED ON
            'paged_data': True,
            'primary_key': 'Number',
            'non_nullable_cols': ['Number']
            },
        'cmdb_ci_document': {
            'load_type': 'full',
            'schema_version': 1,
            'live': False,
            'source_dlm_file_name': 'xxx', # TEST VALUE - TO BE REPLACED ONCE DLM HAS BEEN DECIDED ON
            'source_dlm_sheet_name': "PullApplication", # TEST VALUE - TO BE REPLACED ONCE DLM HAS BEEN DECIDED ON
            'paged_data': True,
            'dq_check_file': '/lakehouse/default/Files/DataQuality/Cleansed/sd_service_now_cmdb_ci_document_checks.yaml'
            },
        'sys_user_grmember': {
            'load_type': 'delta',
            'delta_days': 10,
            'schema_version': 1,
            'live': True,
            'dq_check_file': '/lakehouse/default/Files/DataQuality/Cleansed/sd_service_now_sys_user_grmember_checks.yaml',
            'source_dlm_file_name': 'xxx', # TEST VALUE - TO BE REPLACED ONCE DLM HAS BEEN DECIDED ON
            'source_dlm_sheet_name': "PullApplication", # TEST VALUE - TO BE REPLACED ONCE DLM HAS BEEN DECIDED ON
            'paged_data': True,
            },
        'sys_user_group': {
            'load_type': 'full', # TO BE UPDATED POST INGESTION
            'schema_version': 1,
            'live': True,
            'dq_check_file': '/lakehouse/default/Files/DataQuality/Cleansed/sd_service_now_sys_user_group_checks.yaml', 
            'source_dlm_file_name': 'xxx', # TEST VALUE - TO BE REPLACED ONCE DLM HAS BEEN DECIDED ON
            'source_dlm_sheet_name': "PullSysUserGroup", # TEST VALUE - TO BE REPLACED ONCE DLM HAS BEEN DECIDED ON
            'paged_data': True,
            },
    }
}

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### **LeanIX**

# CELL ********************

lean_ix = {
    'name': 'xxx', 
    'kv_password_name': 'xxx',
    'source_tables': {
        'Application': {
            'load_type': 'full',
            'schema_version': 1,
            'live': True,
            'primary_key': 'Name',
            'dq_check_file': '/lakehouse/default/Files/DataQuality/Cleansed/sd_leanix_application_checks.yaml'
            },
        'Provider': {
            'load_type': 'full',
            'schema_version': 1,
            'live': False,
            'primary_key': 'Id',
            'non_nullable_cols': ['Id']
            },
        'BusinessCapability': {
            'load_type': 'full',
            'schema_version': 1,
            'live': True,
            'dq_check_file': '/lakehouse/default/Files/DataQuality/Cleansed/sd_leanix_business_capability_checks.yaml'
            },
        'DataObject': {
            'load_type': 'full',
            'schema_version': 1,
            'live': True,
            'dq_check_file': '/lakehouse/default/Files/DataQuality/Cleansed/sd_leanix_data_object_checks.yaml'
            },
        'ITComponent': {
            'load_type': 'full',
            'schema_version': 1,
            'live': True,
            'dq_check_file': '/lakehouse/default/Files/DataQuality/Cleansed/sd_leanix_it_component_checks.yaml'
            },
        'Interface': {
            'load_type': 'full',
            'schema_version': 1,
            'live': False,
            'primary_key': 'Name',
            'non_nullable_cols': ['Name']
            }
    }
}

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### **Coupa**

# CELL ********************

coupa = {
    'name': 'xxx', 
    'kv_user_name': 'xxx',
    'kv_password_name': 'xxx',
    'source_tables': {
        'suppliers': {
            'load_type': 'full',
            'schema_version': 1,
            'live': False,
            'primary_key': 'Name',
            'non_nullable_cols': ['ReceiptDate','AllocatedDate','SourceSystem']
            },
        'contracts': {
            'load_type': 'full',
            'schema_version': 2,
            'live': True,
            'primary_key': 'Id',
            'non_nullable_cols': ['ReceiptDate','AllocatedDate','SourceSystem']
            },
    }
}

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### **EUC**

# CELL ********************

euc = {
    'name': 'xxx', 
    'folder_path': "lh_landed.Lakehouse/Files/PushEUCAsset/xxx.csv",
    'source_tables': {
        'push_euc_asset': {
            'load_type': 'full',
            'schema_version': 1,
            'live': False
            },
    }
}

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### **CSC**

# CELL ********************

csc = {
    'name': 'xxx', 
    'folder_path': "lh_landed.Lakehouse/Files/PushCSCDomainName/xxx.csv",
    'source_tables': {
        'push_csc_domain_name': {
            'load_type': 'full',
            'schema_version': 1,
            'live': False
            },
    }
}

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### **Smartsheet**

# CELL ********************

smartsheet = {
    'name': 'xxx',
    'kv_api_token_name': 'xxx',
    'schema_version': 1,
    'api_base_url': 'https://api.smartsheet.com/2.0',
    'max_retries': 3,
    'timeout': 30,
    'source_tables': {
        '4612826324750212': {
            'load_type': 'full',
            'schema_version': 1,
            'live': False,
            'source_dlm_file_name': 'xxx',
            'source_dlm_sheet_name': "PullApplication", # TEST VALUE - TO BE REPLACED ONCE DLM HAS BEEN DECIDED ON
            'paged_data': False,
        },
        '6425435520847748': {
            'load_type': 'full',
            'schema_version': 1,
            'live': False,
            'source_dlm_file_name': 'xxx',
            'source_dlm_sheet_name': "PullApplication",  # TEST VALUE - TO BE REPLACED ONCE DLM HAS BEEN DECIDED ON
            'paged_data': False,
        }
    }
}

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### **Oracle HR**

# CELL ********************

oracle_hr = {
    'name': 'xxx', 
    'kv_user_name': 'xxx',
    'kv_password_name': 'xxx',
    'api-oracle-scope':'xxx',
    'api-oracle-url':'xxx',
    'api-oracle-token-url':'xxx',
    'source_tables': {
        'Employee': {
            'load_type': 'full',
            'schema_version': 1,
            'live': True,
            'dq_check_file': '/lakehouse/default/Files/DataQuality/Cleansed/sd_oracle_hr_employee_checks.yaml'
            },
    }
}

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### **Azure Active Directory**

# CELL ********************

active_directory = {  
    'name': 'xxx',  
    'kv_tenant_id': 'xxx',  
    'kv_client_id': 'xxx',  
    'kv_client_secret': 'xxx',  
    'source_tables': {  
        'users': {  
            'load_type': 'delta',  
            'delta_days': 1,  
            'schema_version': 1,  
            'live': True,  
            'dq_check_file': '/lakehouse/default/Files/DataQuality/Cleansed/sd_active_directory_users_checks.yaml'  
        },  
        'groups': {  
            'load_type': 'delta',  
            'delta_days': 1,  
            'schema_version': 1,  
            'live': True,  
            'dq_check_file': '/lakehouse/default/Files/DataQuality/Cleansed/sd_active_directory_users_checks.yaml'  
        }  
    }  
}  

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### **SAP HR**

# CELL ********************

sap_hr = {
  'name': 'xxx',
  'kv_username': 'xxx',
  'kv_password': 'xxx',
  'schema_version': 1,
  'api_base_url': 'xxx',
  'source_tables': {
      'sap_employee': {
            'load_type': 'full',
            'schema_version': 1,
            'live': True,
            'dq_check_file': '/lakehouse/default/Files/DataQuality/Cleansed/sd_sap_hr_employee_checks.yaml'
      }
  }
}


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### **JIRA TEMPO**

# CELL ********************

tempo = {
  'name': 'xxx',
  'kv_username': 'xxx',
  'kv_password': 'xxx',
  'schema_version': 1,
  'api_base_url': 'xxx',
  'source_tables': {
      'tempo_worklogs': {
            'load_type': 'full',
            'schema_version': 1,
            'live': False,
            'dq_check_file': '/lakehouse/default/Files/DataQuality/Cleansed/sd_tempo_worklogs_checks.yaml'
      },
      'tempo_accounts': {
            'load_type': 'full',
            'schema_version': 1,
            'live': False,
            'dq_check_file': '/lakehouse/default/Files/DataQuality/Cleansed/sd_tempo_accounts_checks.yaml'
        }
    }
}

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
