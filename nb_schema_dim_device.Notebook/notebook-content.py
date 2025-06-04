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

# MARKDOWN ********************

# ##### DIM_DEVICE_V1 Schema
# ---

# CELL ********************

schema_dim_device_v1 = [
    {'field': 'DeviceKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'push_euc_asset': 'SerialNumber'}, 'calculated_field': True},
    {'field': 'UserKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'push_euc_asset': 'CurrentUser'}, 'calculated_field': True},
    {'field': 'SerialNumber', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'push_euc_asset': 'SerialNumber'}},
    {'field': 'DeviceName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'push_euc_asset': 'DeviceName'}},
    {'field': 'JoinType', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'push_euc_asset': 'JoinType'}},
    {'field': 'DeviceOS', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'push_euc_asset': 'DeviceOS'}},
    {'field': 'OSName', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'push_euc_asset': 'OSName'}},
    {'field': 'OSMajorVersion', 'dataType': FloatType(), 'personal': False, 'sensitive': True, 'from': {'push_euc_asset': 'OSMajorVersion'}},
    {'field': 'OSPatchVersion', 'dataType': FloatType(), 'personal': False, 'sensitive': True, 'from': {'push_euc_asset': 'OSPatchVersion'}},
    {'field': 'PatchLevel', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'push_euc_asset': 'PatchLevel'}},
    {'field': 'Manufacturer', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'push_euc_asset': 'Manufacturer'}},
    {'field': 'Model', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'push_euc_asset': 'Model'}},
    {'field': 'WarrantyStartDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'push_euc_asset': 'WarrantyStartDate'}},
    {'field': 'Processor', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'push_euc_asset': 'Processor'}},
    {'field': 'MemoryGB', 'dataType': FloatType(), 'personal': False, 'sensitive': True, 'from': {'push_euc_asset': 'MemoryGB'}},
    {'field': 'HardDiskGB', 'dataType': FloatType(), 'personal': False, 'sensitive': True, 'from': {'push_euc_asset': 'HardDiskGB'}},
    {'field': 'HardwareType', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'push_euc_asset': 'HardwareType'}},
    {'field': 'Encrypted', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'push_euc_asset': 'Encrypted'}},
    {'field': 'OSEndOfLife', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'push_euc_asset': 'OSEndOfLife'}},
    {'field': 'CurrentDeviceStatus', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'push_euc_asset': 'Status'}},
    {'field': 'DefenderLastSeen', 'dataType': DateType(), 'personal': False, 'sensitive': True, 'from': {'push_euc_asset': 'DefenderLastSeen'}},
    {'field': 'SCCMLastSeen', 'dataType': DateType(), 'personal': False, 'sensitive': True, 'from': {'push_euc_asset': 'SCCMLastSeen'}},
    {'field': 'IntuneLastSeen', 'dataType': DateType(), 'personal': False, 'sensitive': True, 'from': {'push_euc_asset': 'IntuneLastSeen'}},
    {'field': 'JamfLastSeen', 'dataType': DateType(), 'personal': False, 'sensitive': True, 'from': {'push_euc_asset': 'JamfLastSeen'}},
    {'field': 'AllocatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'push_euc_asset': 'AllocatedDate'}},
    {'field': 'SourceSystem', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'push_euc_asset': 'SourceSystem'}},
    {'field': 'PipelineUpdatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'push_euc_asset': 'PipelineUpdatedDate'}},
    {'field': 'TableName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'push_euc_asset': 'TableName'}}
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
