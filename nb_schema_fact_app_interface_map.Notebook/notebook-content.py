# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# ##### FACT_APP_Interface_MAP_V1 Schema
# ---

# CELL ********************

schema_fact_app_interface_map_v1 = [
    {'field': 'AppInterfaceKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Interface': 'Name'}, 'calculated_field': True},
    {'field': 'ApplicationProviderKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Interface': 'RelInterfaceToProviderApplication'}, 'calculated_field': True},
    {'field': 'ApplicationConsumerKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Interface': 'RelInterfaceToConsumerApplication'}, 'calculated_field': True},
    {'field': 'AllocatedDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'Interface': 'AllocatedDate'}},
    {'field': 'SourceSystem', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Interface': 'SourceSystem'}},
    {'field': 'PipelineUpdatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'Interface': 'PipelineUpdatedDate'}},
    {'field': 'TableName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Interface': 'TableName'}}
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
