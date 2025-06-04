# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# ##### DIM_Application_V1 Schema
# ---

# CELL ********************

schema_dim_application_map_v1 = [
    {'field': 'ApplicationKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'Name', 'Application': 'Name'}, 'calculated_field': True},
    {'field': 'ApplicationMasterKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': None, 'Application': None}, 'calculated_field': True},
    {'field': 'IsMastered', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': None, 'Application': None}, 'calculated_field': True},
    {'field': 'MasteredBy', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': None, 'Application': None}, 'calculated_field': True},
    {'field': 'MasteredDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': None, 'Application': None}, 'calculated_field': True},
    {'field': 'MasteredMethod', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': None, 'Application': None}, 'calculated_field': True},
    {'field': 'ReceiptDate', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'ReceiptDate', 'Application': 'ReceiptDate'}},
    {'field': 'AllocatedDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'AllocatedDate', 'Application': 'AllocatedDate'}},
    {'field': 'SourceSystem', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'SourceSystem', 'Application': 'SourceSystem'}},
    {'field': 'PipelineUpdatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'PipelineUpdatedDate', 'Application': 'PipelineUpdatedDate'}},
    {'field': 'TableName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'TableName', 'Application': 'TableName'}}
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
