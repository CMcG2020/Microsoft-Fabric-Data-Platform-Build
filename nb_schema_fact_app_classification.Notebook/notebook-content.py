# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

schema_fact_app_classification_map_v1 = [
  {'field': 'AppClassificationKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'BusinessCapability': ['Type', 'Name'], 'DataObject': ['Type', 'Name'], 'ITComponent': ['Type', 'DisplayName']}},
  {'field': 'ApplicationKey','dataType': StringType(),'personal': False,'sensitive': False,'from': {'BusinessCapability': 'relBusinessCapabilityToApplication', 'DataObject': 'relDataObjectToApplication','ITComponent': 'relITComponentToApplication'},'calculated_field': True},
  {'field': 'AllocatedDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from':  {'BusinessCapability': 'AllocatedDate', 'DataObject': 'AllocatedDate', 'ITComponent': 'AllocatedDate'}},
  {'field': 'SourceSystem', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from':  {'BusinessCapability': 'SourceSystem', 'DataObject': 'SourceSystem', 'ITComponent': 'SourceSystem'}},
  {'field': 'PipelineUpdatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from':  {'BusinessCapability': 'PipelineUpdatedDate', 'DataObject': 'PipelineUpdatedDate', 'ITComponent': 'PipelineUpdatedDate'}},
  {'field': 'TableName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from':  {'BusinessCapability': 'TableName', 'DataObject': 'TableName', 'ITComponent': 'TableName'}},
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
