# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# #### Helper Functions for Integration Tests
# ---
# Helper functions for supporting integration tests.

# CELL ********************

def clear_down_lakehouses() -> None:
    """Clears down files and tables from all lakehouses."""
    config = globals()['global_configs']
    if config['env'] in ['uat', 'prd']:
        raise Exception(f"Clear down in {config['env']} not allowed.")

    for lakehouse in [config['sourced_lh_name'], config['cleansed_lh_name'], config['conformed_lh_name'], config['conformed_pii_lh_name']]:
        root_path = get_lakehouse_abfs_path(lakehouse)
        
        for sub_path in ['Files/', 'Tables/']:
            files = mssparkutils.fs.ls(f'{root_path}/{sub_path}')
            [mssparkutils.fs.rm(file.path, True) for file in files if 'SampleLake' not in file.path and 'DataQuality' not in file.path]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
