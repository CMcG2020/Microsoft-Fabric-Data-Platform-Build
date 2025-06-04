# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# #### Global Configs
# ---
# Notebook to store all common configurations used across all notebooks and environments.

# CELL ********************

workspace_id = mssparkutils.runtime.context['currentWorkspaceId']
workspace_name = fabric.resolve_workspace_name(workspace_id)
env = next((e for e in ['dev', 'sit', 'uat', 'prd'] if e in workspace_name), 'dev')

global_configs = {
    'workspace_id': workspace_id,
    'workspace_name': workspace_name,
    'access_token': mssparkutils.credentials.getToken("keyvault"),
    'env': env,
    'current_date': datetime.now().strftime("%m/%d/%Y"),
    'key_vault_url': f"https://{env}-kv.vault.azure.net/",
    'abfs_path': f'abfss://{env}@onelake.dfs.fabric.microsoft.com/',
    'landed_lh_name': 'lh_landed',
    'sourced_lh_name': 'lh_sourced',
    'cleansed_lh_name': 'lh_cleansed',
    'conformed_lh_name': 'lh_conformed',
    'conformed_pii_lh_name': 'lh_conformed_pii',
    'sourced_nb_name': "nb_generate_sourced_{}",
    'cleansed_nb_name': "nb_generate_cleansed_{}",
    'conformed_nb_name': "nb_generate_conformed_{}",
    'harmonised_nb_name': "nb_generate_harmonised_{}",
    'soda_generic_checks_yaml_file_path': '/lakehouse/default/Files/DataQuality/sd_generic_checks.yaml',  # stored in lh_cleansed
    'cleansed_scan_definition_name': 'Cleansed',
    'conformed_scan_definition_name': 'Conformed',
    'metadata_fields': ['ReceiptDate', 'AllocatedDate', 'PipelineUpdatedDate', 'SourceSystem', 'TableName'],
    'dq_checks_source_storage_url': "xxx",
    'dq_checks_target_storage_url': f"xxx"
}

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
