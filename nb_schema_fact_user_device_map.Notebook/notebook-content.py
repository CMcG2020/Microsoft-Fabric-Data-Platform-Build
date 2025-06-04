# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

schema_fact_user_device_map_v1 = [
    {'field': 'DeviceKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'push_euc_asset': 'SerialNumber'}, 'calculated_field': True},
    {'field': 'UserKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'push_euc_asset': 'CurrentUser'}, 'calculated_field': True},
    {'field': 'AssignedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'push_euc_asset': None}, 'calculated_field': False},
    {'field': 'ReleasedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'push_euc_asset': None}, 'calculated_field': False},
    {'field': 'AllocatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'push_euc_asset': 'AllocatedDate', 'push_euc_asset': 'ReceiptDate'}},
    {'field': 'SourceSystem', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'push_euc_asset': 'SourceSystem', 'push_euc_asset': 'ReceiptDate'}},
    {'field': 'PipelineUpdatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'push_euc_asset': 'PipelineUpdatedDate', 'push_euc_asset': 'ReceiptDate'}},
    {'field': 'TableName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'push_euc_asset': 'TableName', 'push_euc_asset': 'TableName'}},
    {'field': 'DataKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'push_euc_asset': 'SerialNumber'}},
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
