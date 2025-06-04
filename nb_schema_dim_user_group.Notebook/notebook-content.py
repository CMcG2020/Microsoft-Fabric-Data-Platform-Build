# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

schema_dim_user_group_v1 = [
  {'field': 'UserGroupKey','dataType': StringType(),'personal': False,'sensitive': False,'from': {'sys_user_group': 'Name','groups':'GroupDisplayName'}},
  {'field': 'UserGroupName','dataType': StringType(),'personal': False,'sensitive': False,'from': {'sys_user_group': 'Name','groups': 'GroupDisplayName'}},
  {'field': 'UserGroupType','dataType': StringType(),'personal': False,'sensitive': False,'from': {'sys_user_group': 'SourceSystem','groups': 'SourceSystem'}},
  {'field': 'Division','dataType': StringType(),'personal': False,'sensitive': False,'from': {'sys_user_group': 'Division'}},
  {'field': 'BusinessGroup','dataType': StringType(),'personal': False,'sensitive': False,'from': {'sys_user_group': 'BusinessGroup'}},
  {'field': 'BusinessUnit','dataType': StringType(),'personal': False,'sensitive': False,'from': {'sys_user_group': 'BusinessUnit'}},
  {'field': 'IsActive','dataType': BooleanType(),'personal': False,'sensitive': False,'from': {'sys_user_group': 'Active'}},
  {'field': 'AllocatedDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from':  {'sys_user_group': 'AllocatedDate', 'groups': 'AllocatedDate'}},
  {'field': 'SourceSystem', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from':  {'sys_user_group': 'SourceSystem', 'groups': 'SourceSystem'}},
  {'field': 'PipelineUpdatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from':  {'sys_user_group': 'PipelineUpdatedDate', 'groups': 'PipelineUpdatedDate'}},
  {'field': 'TableName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from':  {'sys_user_group': 'TableName', 'groups': 'TableName'}},
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
