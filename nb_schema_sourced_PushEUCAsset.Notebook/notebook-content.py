# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# ##### PUSH_EUC_ASSET_V1 Schema
# ---

# CELL ********************

schema_push_euc_asset_v1 = [
    {'from': 'Serial_Number', 'to': 'SerialNumber', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'Device_Name', 'to': 'DeviceName', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'Current_User', 'to': 'CurrentUser', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Join_Type', 'to': 'JoinType', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'DeviceOS', 'to': 'DeviceOS', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'OS_Name', 'to': 'OSName', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'OS_Major_Version', 'to': 'OSMajorVersion', 'dataType': FloatType(), 'personal': False, 'sensitive': True},
    {'from': 'OS_Patch_Version', 'to': 'OSPatchVersion', 'dataType': FloatType(), 'personal': False, 'sensitive': True},
    {'from': 'Patch_Level', 'to': 'PatchLevel', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'Manufacturer', 'to': 'Manufacturer', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'Model', 'to': 'Model', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'WarrantyStartDate', 'to': 'WarrantyStartDate', 'dataType': DateType(), 'personal': False, 'sensitive': False},
    {'from': 'Processor', 'to': 'Processor', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'MemoryGB', 'to': 'MemoryGB', 'dataType': FloatType(), 'personal': False, 'sensitive': True},
    {'from': 'HardDiskGB', 'to': 'HardDiskGB', 'dataType': FloatType(), 'personal': False, 'sensitive': True},
    {'from': 'HardwareType', 'to': 'HardwareType', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'Encrypted', 'to': 'Encrypted', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'OS_EndOfLife', 'to': 'OSEndOfLife', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'DeviceStatus', 'to': 'Status', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'Defender_LastSeen', 'to': 'DefenderLastSeen', 'dataType': DateType(), 'personal': False, 'sensitive': True},
    {'from': 'SCCM_LastSeen', 'to': 'SCCMLastSeen', 'dataType': DateType(), 'personal': False, 'sensitive': True},
    {'from': 'Intune_LastSeen', 'to': 'IntuneLastSeen', 'dataType': DateType(), 'personal': False, 'sensitive': True},
    {'from': 'Jamf_LastSeen', 'to': 'JamfLastSeen', 'dataType': DateType(), 'personal': False, 'sensitive': True},
    {'from': 'AD_SamAccountName', 'to': 'SamAccountName', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'AD_UserGivenName', 'to': 'UserGivenName', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'AD_UserSurname', 'to': 'UserSurname', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'AD_UserEmployeeType', 'to': 'UserEmployeeType', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'AD_UserOffice', 'to': 'UserOffice', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'AD_UserCountry', 'to': 'UserCountry', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'AD_UserCompany', 'to': 'UserCompany', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'AD_UserDivision', 'to': 'UserDivision', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'AD_extensionattribute4', 'to': 'ExtensionAttribute4', 'dataType': StringType(), 'personal': True, 'sensitive': False}
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
