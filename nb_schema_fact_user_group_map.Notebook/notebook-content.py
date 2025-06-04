# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

schema_fact_user_group_map_v1 = [
  {'field': 'UserGroupKey','dataType': StringType(),'personal': False,'sensitive': False,'from': {'sys_user_grmember': 'Group','groups': 'GroupDisplayName'}},
  {'field': 'UserKey','dataType': StringType(),'personal': False,'sensitive': False,'from': {'sys_user_grmember': 'User','groups': 'UserPrincipalName'}},
  {'field': 'PipelineUpdatedDate','dataType': TimestampType(),'personal': False,'sensitive': False,'from': {'sys_user_grmember': 'PipelineUpdatedDate','groups': 'PipelineUpdatedDate'}},
  {'field': 'AllocatedDate','dataType': TimestampType(),'personal': False,'sensitive': False,'from': {'sys_user_grmember': 'AllocatedDate','groups': 'AllocatedDate'}},
  {'field': 'SourceSystem','dataType': StringType(),'personal': False,'sensitive': False,'from': {'sys_user_grmember': 'SourceSystem','groups': 'SourceSystem'}},
  {'field': 'TableName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from':  {'sys_user_grmember': 'TableName', 'groups': 'TableName'}},
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
