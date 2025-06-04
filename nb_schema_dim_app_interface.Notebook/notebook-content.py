# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# ##### DIM_APP_Interface_V1 Schema
# ---

# CELL ********************

schema_dim_app_interface_v1 = [
    {'field': 'AppInterfaceKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Interface': 'Name'}, 'calculated_field': True},
    {'field': 'URLID', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Interface': 'Id'}},
    {'field': 'Name', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Interface': 'Name'}},
    {'field': 'DisplayName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Interface': 'DisplayName'}},
    {'field': 'Description', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Interface': 'Description'}},
    {'field': 'LeanIXCreationDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'Interface': 'CreatedAt'}},
    {'field': 'LeanIXLastUpdateDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'Interface': 'UpdatedAt'}},
    {'field': 'Alias', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Interface': 'Alias'}},
    {'field': 'CurrentLifecycleState', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Interface': 'LifecycleAsString'}},
    {'field': 'LifecyclePlanDate', 'dataType': DateType(), 'personal': False, 'sensitive': True, 'from': {'Interface': 'LifecyclePlan'}},
    {'field': 'LifecyclePhaseInDate', 'dataType': DateType(), 'personal': False, 'sensitive': True, 'from': {'Interface': 'LifecyclePhaseIn'}},
    {'field': 'LifecycleActiveInDate', 'dataType': DateType(), 'personal': False, 'sensitive': True, 'from': {'Interface': 'LifecycleActive'}},
    {'field': 'LifecyclePhaseOutDate', 'dataType': DateType(), 'personal': False, 'sensitive': True, 'from': {'Interface': 'LifecyclePhaseOut'}},
    {'field': 'LifecycleEndOfLifeDate', 'dataType': DateType(), 'personal': False, 'sensitive': True, 'from': {'Interface': 'LifecycleEndOfLife'}},
    {'field': 'FlowDirection', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Interface': 'DataFlowDirection'}},
    {'field': 'InterfaceType', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Interface': 'InterfaceType'}},
    {'field': 'Frequency', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Interface': 'Frequency'}},
    {'field': 'HTTPInterface', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Interface': 'InterfaceType'}},
    {'field': 'WebsitePurpose', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Interface': 'TagsWebsitePurpose'}},
    {'field': 'EventArchitectures', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Interface': 'TagsEventArchitectures'}},
    {'field': 'HRIntegrationType', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Interface': 'TagsHRIntegrationType'}},
    {'field': 'ReceiptDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'Interface': 'ReceiptDate'}},
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
