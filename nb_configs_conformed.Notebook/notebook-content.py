# Fabric notebook source# 
# NOTE: This is an anonymized example configuration file.
# Client-specific data, system names, and identifiers have been replaced with generic placeholders.
#
# 
# Anonymization changes made:
# - File paths: Removed client-specific prefixes (e.g., "sd_" prefix)
# - System names: 
#   * "coupa" -> "procurement_system"
#   * "lean_ix" -> "architecture_tool" 
#   * "euc" -> "asset_management"
#   * "csc" -> "domain_service"
#   * "sap_hr"/"oracle_hr" -> "hr_system_1"/"hr_system_2"
# - Table names: Replaced client-specific table names with generic equivalents
# - Custom field names: Anonymized where they contained client-specific information
# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# #### Conformed Layer Configs
# ---
# Notebook to store all configurations for conformed layer tables alongside any harmonisation configurations.

# MARKDOWN ********************

# ##### **Facts**

# CELL ********************

facts = {    
    'fact_ticket_event': {
        'name': 'fact_ticket_event',
        'schema_version': 2,
        'live': True,
        'write_type': 'append',
        'primary_key': None,
        'attributes_key': 'AttributesKey',
        'dq_check_file': '/lakehouse/default/Files/DataQuality/Conformed/sd_fact_ticket_event_checks.yaml',
        'partition_by': ['Year', 'Month'],
        'required_tables': {
            'cleansed': {
                'service_now': {
                    'task_sla': {'schema_version': 1}
                }
            },
        }
    },  
    'fact_contract': {
        'name': 'fact_contract',
        'schema_version': 2,
        'live': True,
        'write_type': 'merge',
        'primary_key': 'ContractKey',
        'attributes_key': 'AttributesKey',
        'non_nullable_cols': ['ContractKey'],
        'non_nullable_cols_pii': ['ContractKey'],
        'required_tables': {
            'cleansed': {
                'coupa': {
                    'contracts': {'schema_version': 2}
                }
            }
        }
    },
    'fact_app_interface_map': {
        'name': 'fact_app_interface_map',
        'schema_version': 1,
        'live': False,
        'write_type': 'overwrite',
        'primary_key': None,
        'attributes_key': None,
        'required_tables': {
            'cleansed': {
                'lean_ix': {
                    'Interface': {'schema_version': 1}
                }
            }
        }
    },
    'fact_outage': {
        'name': 'fact_outage',
        'schema_version': 1,
        'live': True,
        'write_type': 'merge',
        'primary_key': 'OutageKey',
        'attributes_key': 'AttributesKey',
        'non_nullable_cols': ['OutageKey', 'TicketOutageNumber'],
        'non_nullable_cols_pii': ['OutageKey', 'TicketOutageNumber'],
        'required_tables': {
            'cleansed': {
                'service_now': {
                    'cmdb_ci_outage': {'schema_version': 1}
                }
            }
        }
    },
    'fact_app_classification_map': {
        'name': 'fact_app_classification_map',
        'schema_version': 1,
        'live': True,
        'write_type': 'overwrite',
        'primary_key': 'AppClassificationKey',
        'attributes_key': 'AttributesKey',
        'non_nullable_cols': ['AppClassificationKey'],
        'required_tables': {
            'cleansed': {
                'lean_ix': {
                    'BusinessCapability': {'schema_version': 1},
                    'DataObject': {'schema_version': 1},
                    'ITComponent': {'schema_version': 1}
                }
            }
        }
    },
    'fact_user_device_map': {
        'name': 'fact_user_device_map',
        'schema_version': 1,
        'live': False,
        'write_type': 'overwrite',
        'primary_key': "DeviceKey",
        'user_key': "UserKey",
        'attributes_key': 'AttributesKey',
        'data_key': "DataKey",
        'scd2_partition_col': "DeviceKey",
        'scd2_start_date_col': "StartDate",
        'scd2_end_date_col': "EndDate",
        'scd2_order_col': "StartDate",
        'scd2_current_status_col': "Status",
        'scd2_active_status': "Active",
        'scd2_default_end_date': "9999-12-31",
        'required_tables': {
            'cleansed': {
                'euc': {
                    'push_euc_asset': {'schema_version': 1}
                }
            },
            'conformed': {
                'facts': {
                    'fact_user_device_map': {'schema_version': 1}
                } 
            }
        }
    },
    'fact_user_group_map': {
        'name': 'fact_user_group_map',
        'schema_version': 1,
        'live': True,
        'write_type': 'overwrite',
        'primary_key': None,
        'attributes_key': 'AttributesKey',
        'dq_check_file': '/lakehouse/default/Files/DataQuality/Conformed/sd_fact_user_group_map_checks.yaml',
        'required_tables': {
            'cleansed': {
                'service_now': {
                    'sys_user_grmember': {'schema_version': 1},
                    'sys_user': {'schema_version': 1}
                }, 
                'active_directory': {
                    'groups': {'schema_version': 1}}
                }
            }
        },
}

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### **Dimensions**

# CELL ********************

dimensions = {
    'dim_date': {
        'name': 'dim_date',
        'schema_version': 1,
        'live': True,
        'write_type': 'overwrite',
        'partition_by': ['Year', 'Month'],
        'start_date': date(2020, 1, 1),
        'end_date': date(2030, 12, 31)
    },
    'dim_application_source': {
        'name': 'dim_application_source',
        'schema_version':1,
        'live': True,
        'write_type': 'overwrite',
        'primary_key': 'ApplicationKey',
        'attributes_key': 'AttributesKey',
        'dq_check_file': '/lakehouse/default/Files/DataQuality/Conformed/sd_dim_application_source_checks.yaml',
        'supplier_key': 'SupplierKey',
        'domain_key': 'DomainKey',
        'required_tables': {
            'cleansed': {
                'service_now': {
                    'cmdb_ci_appl': {'schema_version': 1},
                    'sys_user': {'schema_version': 1}
                    }, 
                'lean_ix': {
                    'Application': {'schema_version': 1}
                    }
            },
        }
    },
    'dim_application': {
        'name': 'dim_application',
        'schema_version': 1,
        'live': True,
        'write_type': 'overwrite',
        'primary_key': 'ApplicationKey',
        'attributes_key': 'AttributesKey',
        'non_nullable_cols': ['ApplicationKey'],
        'supplier_key': 'SupplierKey',
        'domain_key': 'DomainKey',
        'required_tables': {
            'cleansed': {
                'service_now': {
                    'cmdb_ci_appl': {'schema_version': 1},
                    'sys_user': {'schema_version': 1}
                    }, 
                'lean_ix': {
                    'Application': {'schema_version': 1}
                    }
            },
        }
    },
    'dim_application_map': {
        'name': 'dim_application_map',
        'schema_version': 1,
        'live': True,
        'write_type': 'overwrite',
        'primary_key': 'ApplicationKey',
        'attributes_key': 'AttributesKey',
        'non_nullable_cols': ['ApplicationKey'],
        'required_tables': {
            'cleansed': {
                'service_now': {
                    'cmdb_ci_appl': {'schema_version': 1},
                    'sys_user': {'schema_version': 1}
                    }, 
                'lean_ix': {'Application': {'schema_version': 1}},
            },
            'conformed': {
                'dimensions': {
                    'dim_application_source': {'schema_version': 1},
                    'dim_application': {'schema_version': 1}
                    }
            }
        }
    },
    'dim_app_interface': {
        'name': 'dim_app_interface',
        'schema_version': 1,
        'live': False,
        'write_type': 'overwrite',
        'primary_key': 'AppInterfaceKey',
        'attributes_key': 'AttributesKey',
        'required_tables': {
            'cleansed': {'lean_ix': {'Interface': {'schema_version': 1}},
            }
        }
    },
    'dim_ticket': {
        'name': 'dim_ticket',
        'schema_version': 3,
        'live': True,
        'write_type': 'merge',
        'primary_key': 'TicketKey',
        'non_nullable_cols': ['TicketKey', 'TicketNumber'],
        'non_nullable_cols_pii': ['TicketKey'],
        'attributes_key': 'AttributesKey',
        'partition_by': ['Year', 'Month', 'Day'],
        'required_tables': {
            'cleansed': {
                'service_now': {
                    'incident': {'schema_version': 1},
                    'u_inf_generic_request': {'schema_version': 1},
                    'sc_req_item': {'schema_version': 1},
                    'sc_task': {'schema_version': 1},
                    'sys_user': {'schema_version': 1},
                    'asmt_assessment_instance': {'schema_version': 1},
                    'asmt_assessment_instance_question': {'schema_version': 1}
                }, 
            }
        }
    },
    'dim_supplier': {
        'name': 'dim_supplier',
        'schema_version': 1,
        'live': False,
        'write_type': 'overwrite',
        'primary_key': 'SupplierKey',
        'attributes_key': 'AttributesKey',
        'required_tables': {
            'cleansed': {
                'coupa': {'suppliers': {'schema_version': 1}}, 
                'lean_ix': {'Provider': {'schema_version': 1}},
                'service_now': {
                    'core_company': {'schema_version': 1},
                    'sys_user': {'schema_version': 1}}
            },
        }
    },
    'dim_supplier_source': {
        'name': 'dim_supplier_source',
        'schema_version': 1,
        'live': False,
        'write_type': 'overwrite',
        'primary_key': 'SupplierKey',
        'attributes_key': 'AttributesKey',
        'required_tables': {
            'cleansed': {
                'lean_ix': {'Provider': {'schema_version': 1}},
                'coupa': {
                    'suppliers': {'schema_version': 1},
                    'contracts': {'schema_version': 2}}, 
                'service_now': {
                    'core_company': {'schema_version': 1},
                    'sys_user': {'schema_version': 1}}
            },
        }
    },
    'dim_supplier_map': {
        'name': 'dim_supplier_map',
        'schema_version': 1,
        'live': False,
        'write_type': 'merge',
        'primary_key': 'SupplierKey',
        'attributes_key': 'AttributesKey',
        'required_tables': {
            'cleansed': {
                'coupa': {'suppliers': {'schema_version': 1}}, 
                'lean_ix': {'Provider': {'schema_version': 1}},
                'service_now': {'core_company': {'schema_version': 1}}
            },
            'conformed': {
                'dimensions': {
                    'dim_supplier_source': {'schema_version': 1},
                    'dim_supplier': {'schema_version': 1}
                    }
            },
        }
    },
    'dim_device': {
    'name': 'dim_device',
    'schema_version': 1,
    'live': False,
    'write_type': 'merge',
    'primary_key': 'DeviceKey',
    'attributes_key': 'AttributesKey',
    'required_tables': {
        'cleansed': {
                'euc': {'push_euc_asset': {'schema_version': 1}}, 
        },
    }
},
    'dim_service': {
    'name': 'dim_service',
    'schema_version': 1,
    'live': False,
    'write_type': 'overwrite',
    'primary_key': 'ChildServiceKey',
    'attributes_key': 'AttributesKey',
    'non_nullable_cols': ['ChildServiceKey'],
    'non_nullable_cols_pii': ['ChildServiceKey'],
    'required_tables': {
        'cleansed': {
            'service_now': {
                    'cmdb_ci_service': {'schema_version': 1},
                    'cmdb_rel_ci': {'schema_version': 1}
                    },
        },
    }
},

    'dim_device_history': {
        'name': 'dim_device_history',
        'schema_version': 1,
        'live': False,
        'write_type': 'overwrite',
        'primary_key': 'DeviceKey',
        'attributes_key': 'AttributesKey',
        'data_key': 'DataKey',
        'scd2_partition_col': "DeviceKey",
        'scd2_start_date_col': "StartDate",
        'scd2_end_date_col': "EndDate",
        'scd2_order_col': "StartDate",
        'scd2_current_status_col': "Status",
        'scd2_active_status': "Active",
        'scd2_default_end_date': "9999-12-31",
        'required_tables': {
            'cleansed': {
                'euc': {
                    'push_euc_asset': {'schema_version': 1}
                    }, 
            },
            'conformed': {
                'dimensions': {
                    'dim_device_history': {'schema_version': 1}
                }, 
            },
        }
},
    'dim_domain': {
        'name': 'dim_domain',
        'schema_version': 1,
        'live': False,
        'write_type': 'overwrite',
        'primary_key': 'DomainKey',
        'attributes_key': 'AttributesKey',
        'required_tables': {
            'cleansed': {
                'csc': {'push_csc_domain_name': {'schema_version': 1}}, 
            },
        }
    },
    'dim_user': {
        'name': 'dim_user',
        'schema_version': 1,
        'live': True,
        'write_type': 'overwrite',
        'primary_key': 'UserKey',
        'attributes_key': 'AttributesKey',
        'dq_check_file': '/lakehouse/default/Files/DataQuality/Conformed/sd_dim_user_checks.yaml',
        'required_tables': {
            'cleansed': {
                'sap_hr': {'sap_employee': {'schema_version': 1}}, 
                'oracle_hr': {'Employee': {'schema_version': 1}},
                'active_directory': {'users': {'schema_version': 1},
                    }
            },
        }
    },
    'dim_app_classification': {
        'name': 'dim_app_classification',
        'schema_version': 1,
        'live': True,
        'write_type': 'overwrite',
        'primary_key': 'AppClassificationKey',
        'attributes_key': 'AttributesKey',
        'dq_check_file': '/lakehouse/default/Files/DataQuality/Conformed/sd_dim_app_classification_checks.yaml',
        'required_tables': {
            'cleansed': {
                'lean_ix': {
                    'BusinessCapability': {'schema_version': 1},
                    'DataObject': {'schema_version': 1},
                    'ITComponent': {'schema_version': 1}
                    },
            }
        }
    },
    'dim_user_group': {
        'name': 'dim_user_group',
        'schema_version': 1,
        'live': True,
        'write_type': 'overwrite',
        'primary_key': 'UserGroupKey',
        'attributes_key': 'AttributesKey',
        'non_nullable_cols': ['UserGroupKey'],
        'non_nullable_cols_pii': ['UserGroupKey'],
        'required_tables': {
            'cleansed': {
                'service_now': {'sys_user_group': {'schema_version': 1}}, 
                'active_directory': {'groups': {'schema_version': 1}},
                    },
            }
        }
}


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### **Harmonised**

# CELL ********************

harmonized = {
  'application': {
      'name': 'application',
      'write_type': 'overwrite',
      'schema_version': 1,
      'primary_key': 'ApplicationKey',
      'attributes_key': 'AttributesKey',
      'method_ranking': {
          'id': 1, 
          'name': 2
      },
      'required_tables': {
          'conformed': {
              'dimensions': {
                  'dim_application_source': {'schema_version': 1},
                  'dim_application': {'schema_version': 1},
                  'dim_application_map': {'schema_version': 1}
              }
          }
      }
  },
  'supplier': {
      'name': 'supplier',
      'schema_version': 1,
      'primary_key': 'SupplierKey',
      'attributes_key': 'AttributesKey',
      'method_ranking': {
          'name': 1
      },
      'required_tables': {
          'conformed': {
              'dimensions': {
                  'dim_supplier_source': {'schema_version': 1},
                  'dim_supplier': {'schema_version': 1},
                  'dim_supplier_map': {'schema_version': 1}
              }
          }
      }
  }
}

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### **Data Quality**

# CELL ********************

dq_checks = {    
        'name': 'dq_checks',
        'schema_version': 1,
        'live': True,
        'partition_by': ['SourceSystem', 'TableName', 'ScanDate']
}

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
