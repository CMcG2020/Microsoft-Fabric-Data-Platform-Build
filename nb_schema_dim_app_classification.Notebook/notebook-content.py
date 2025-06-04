# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

schema_dim_app_classification_v1 = [
  {'field': 'AppClassificationKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'BusinessCapability': ['Type', 'Name'], 'DataObject': ['Type', 'Name'], 'ITComponent': ['Type', 'DisplayName']}},
  {'field': 'ClassificationType', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'BusinessCapability': 'Type', 'DataObject': 'Type', 'ITComponent': 'Type'}},
  {'field': 'LinkedApplications', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'BusinessCapability': 'relBusinessCapabilityToApplication', 'DataObject': 'relDataObjectToApplication', 'ITComponent': 'relITComponentToApplication'}},
  {'field': 'URLID', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'BusinessCapability': 'Id', 'DataObject': 'Id', 'ITComponent': 'Id'}},
  {'field': 'Name', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'BusinessCapability': 'Name', 'DataObject': 'Name', 'ITComponent': 'Name'}},
  {'field': 'DisplayName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'BusinessCapability': 'DisplayName', 'DataObject': 'DisplayName', 'ITComponent': 'DisplayName'}},
  {'field': 'Alias', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'BusinessCapability': 'Alias', 'DataObject': 'Alias', 'ITComponent': 'Alias'}},
  {'field': 'HierarchyLevel', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'BusinessCapability': 'Level', 'DataObject': 'Level', 'ITComponent': 'Level'}},
  {'field': 'HierarchyLevel1', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'BusinessCapability': 'DisplayName', 'DataObject': 'DisplayName', 'ITComponent': 'DisplayName'}, 'calculated_field': True},
  {'field': 'HierarchyLevel2', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'BusinessCapability': 'DisplayName', 'DataObject': 'DisplayName', 'ITComponent': 'DisplayName'}, 'calculated_field': True},
  {'field': 'HierarchyLevel3', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'BusinessCapability': 'DisplayName', 'DataObject': 'DisplayName', 'ITComponent': 'DisplayName'}, 'calculated_field': True},
  {'field': 'HierarchyLevel4', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'BusinessCapability': 'DisplayName', 'DataObject': 'DisplayName', 'ITComponent': 'DisplayName'}, 'calculated_field': True},
  {'field': 'Description', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'BusinessCapability': 'Description', 'DataObject': 'Description', 'ITComponent': 'Description'}},
  {'field': 'CurrentLifecycleState', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'BusinessCapability': 'LifecycleAsString', 'DataObject': 'LifecycleAsString', 'ITComponent': 'LifecycleAsString'}},
  {'field': 'LifecyclePlanDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': True, 'from': {'BusinessCapability': 'LifecyclePlan', 'DataObject': 'LifecyclePlan', 'ITComponent': 'LifecyclePlan'}},
  {'field': 'LifecyclePhaseInDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': True, 'from': {'BusinessCapability': 'LifecyclePhaseIn', 'DataObject': 'LifecyclePhaseIn', 'ITComponent': 'LifecyclePhaseIn'}},
  {'field': 'LifecycleActiveDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': True, 'from': {'BusinessCapability': 'LifecycleActive', 'DataObject': 'LifecycleActive', 'ITComponent': 'LifecycleActive'}},
  {'field': 'LifecyclePhaseOutDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': True, 'from': {'BusinessCapability': 'LifecyclePhaseOut', 'DataObject': 'LifecyclePhaseOut', 'ITComponent': 'LifecyclePhaseOut'}},
  {'field': 'LifecycleEndOfLifeDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': True, 'from': {'BusinessCapability': 'LifecycleEndOfLife', 'DataObject': 'LifecycleEndOfLife', 'ITComponent': 'LifecycleEndOfLife'}},
  {'field': 'GeographicalLocation', 'dataType': StringType(), 'personal': True, 'sensitive': False, 'from': {'ITComponent': 'GeoAddress'}},
  {'field': 'DataObjectType', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'DataObject': 'TagsDataObjectType'}},
  {'field': 'PrivacyClassification', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'DataObject': 'DataClassification'}},
  {'field': 'Subtype', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'BusinessCapability': 'Category', 'DataObject': 'Category', 'ITComponent': 'Category'}},
  {'field': 'Release', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'ITComponent': 'Release'}},
  {'field': 'SupplierKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'ITComponent': 'relITComponentToProvider'}},
  {'field': 'ITComponentVendor', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'ITComponent': 'relITComponentToProvider'}},
  {'field': 'ITComponentTechCategories', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'ITComponent': 'relITComponentToTechnologyStack'}},
  {'field': 'ITComponentHostingType', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'ITComponent': 'TagsHostingType'}},
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
