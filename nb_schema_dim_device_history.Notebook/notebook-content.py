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
# META     }
# META   }
# META }

# CELL ********************

schema_dim_device_history_v1 = [
    {'field': 'DeviceKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'push_euc_asset': 'SerialNumber'}, 'calculated_field': True},
    {'field': 'StartDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'push_euc_asset': 'SerialNumber'}, 'calculated_field': True},
    {'field': 'EndDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'push_euc_asset': 'DeviceName'}, 'calculated_field': True},
    {'field': 'Status', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'push_euc_asset': 'CurrentDeviceStatus'}, 'calculated_field': True},
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
