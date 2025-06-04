# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# ##### AAD USERS_V1 Schema

# CELL ********************

schema_users_v1 = [
  {'from': 'userPrincipalName', 'to': 'UserPrincipalName', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'displayName', 'to': 'DisplayName', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'deletedDateTime', 'to': 'DeletedDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': True},
  {'from': 'managerUPN', 'to': 'ManagerUPN', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'extensionAttribute10', 'to': 'ExtensionAttribute10', 'dataType': StringType(), 'personal': False, 'sensitive': True},
  {'from': 'allGroups', 'to': 'AllGroups', 'dataType': StringType(), 'personal': False, 'sensitive': False},
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### AAD GROUPS_V1 Schema

# CELL ********************

schema_groups_v1 = [
  {'from': 'UserPrincipalName', 'to': 'UserPrincipalName', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'GroupDisplayName', 'to': 'GroupDisplayName', 'dataType': StringType(), 'personal': False, 'sensitive': True}
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
