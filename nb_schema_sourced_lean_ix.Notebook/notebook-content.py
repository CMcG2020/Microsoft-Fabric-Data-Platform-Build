# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# ##### APPLICATION_V1 Schema
# ---

# CELL ********************

schema_Application_v1 = [
    {'from': 'id', 'to': 'Id', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'type', 'to': 'Type', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'name', 'to': 'Name', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'displayName', 'to': 'DisplayName', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'description', 'to': 'Description', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'category', 'to': 'Category', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'completion', 'to': 'Category', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{completion}', 'sub_fields': [{'name': 'Completion', 'dataType': DecimalType(3, 2)}]}},
    {'from': 'fullName', 'to': 'FullName', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'status', 'to': 'Status', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'level', 'to': 'Level', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
    {'from': 'createdAt', 'to': 'CreatedAt', 'dataType': DateType(), 'personal': False, 'sensitive': False},
    {'from': 'updatedAt', 'to': 'UpdatedAt', 'dataType': DateType(), 'personal': False, 'sensitive': False},
    {'from': 'lxState', 'to': 'LxState', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'alias', 'to': 'Alias', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'externalId', 'to': 'ExternalId', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{externalId}', 'sub_fields': [{'name': 'ExternalId', 'dataType': StringType()}]}},
    {'from': 'lifecycle', 'to': 'Lifecycle', 'personal': False, 'sensitive': True, 'nested': {'gql_string': '{asString phases {phase startDate }}', 'sub_fields': [
        {'name': 'LifecycleAsString', 'dataType': StringType(), 'personal': False, 'sensitive': True},
        {'name': 'LifecyclePlan', 'dataType': DateType(), 'personal': False, 'sensitive': False},
        {'name': 'LifecyclePhaseIn', 'dataType': DateType(), 'personal': False, 'sensitive': False},
        {'name': 'LifecycleActive', 'dataType': DateType(), 'personal': False, 'sensitive': False},
        {'name': 'LifecyclePhaseOut', 'dataType': DateType(), 'personal': False, 'sensitive': True},
        {'name': 'LifecycleEndOfLife', 'dataType': DateType(), 'personal': False, 'sensitive': True}]}},
    {'from': 'businessCriticality', 'to': 'BusinessCriticality', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'functionalSuitabilityDescription', 'to': 'FunctionalSuitabilityDescription', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'technicalSuitabilityDescription', 'to': 'TechnicalSuitabilityDescription', 'dataType': StringType(), 'personal': False, 'sensitive': False},    
    {'from': 'relToSuccessor', 'to': 'RelToSuccessor', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToSuccessor', 'dataType': ArrayType(StringType())}]}},
    {'from': 'relToPredecessor', 'to': 'RelToPredecessor', 'personal': False, 'sensitive': True, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToPredecessor', 'dataType': ArrayType(StringType())}]}},
    {'from': 'relToParent', 'to': 'RelToParent', 'personal': False, 'sensitive': True, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToParent', 'dataType': ArrayType(StringType())}]}},
    {'from': 'relToChild', 'to': 'RelToChild', 'personal': False, 'sensitive': True, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToChild', 'dataType': ArrayType(StringType())}]}},
    {'from': 'relToRequires', 'to': 'RelToRequires', 'personal': False, 'sensitive': True, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToRequires', 'dataType': ArrayType(StringType())}]}},
    {'from': 'relToRequiredBy', 'to': 'RelToRequiredBy', 'personal': False, 'sensitive': True, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToRequiredBy', 'dataType': ArrayType(StringType())}]}},
    {'from': 'relApplicationToProject', 'to': 'RelApplicationToProject', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelApplicationToProject', 'dataType': ArrayType(StringType())}]}},
    {'from': 'relApplicationToBusinessCapability', 'to': 'RelApplicationToBusinessCapability', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelApplicationToBusinessCapability', 'dataType': ArrayType(StringType())}]}},
    {'from': 'relApplicationToProcess', 'to': 'RelApplicationToProcess', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelApplicationToProcess', 'dataType': ArrayType(StringType())}]}},
    {'from': 'relApplicationToUserGroup', 'to': 'RelApplicationToUserGroup', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelApplicationToUserGroup', 'dataType': ArrayType(StringType())}]}},
    {'from': 'relApplicationToDataObject', 'to': 'RelApplicationToDataObject', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelApplicationToDataObject', 'dataType': ArrayType(StringType())}]}},
    {'from': 'relProviderApplicationToInterface', 'to': 'RelProviderApplicationToInterface', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelProviderApplicationToInterface', 'dataType': ArrayType(StringType())}]}},
    {'from': 'relConsumerApplicationToInterface', 'to': 'RelConsumerApplicationToInterface', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelConsumerApplicationToInterface', 'dataType': ArrayType(StringType())}]}},
    {'from': 'relApplicationToITComponent', 'to': 'RelApplicationToITComponent', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelApplicationToITComponent', 'dataType': ArrayType(StringType())}]}},
    {'from': 'tags', 'to': 'Tags', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{name tagGroup{name}}', 'sub_fields': [
        {'name': 'TagsInstanceType', 'dataType': StringType(), 'personal': False, 'sensitive': False},
        {'name': 'TagsImportantApplication', 'dataType': StringType(), 'personal': False, 'sensitive': True},
        {'name': 'TagsDivestedTo', 'dataType': StringType(), 'personal': False, 'sensitive': True},
        {'name': 'TagsM&AStatus', 'dataType': StringType(), 'personal': False, 'sensitive': True},
        {'name': 'TagsWebsitePurpose', 'dataType': StringType(), 'personal': False, 'sensitive': False},
        {'name': 'TagsEventArchitectures', 'dataType': StringType(), 'personal': False, 'sensitive': False},
        {'name': 'TagsPaymentChannel', 'dataType': StringType(), 'personal': False, 'sensitive': True},
        {'name': 'TagsApplicationType', 'dataType': StringType(), 'personal': False, 'sensitive': False},
        {'name': 'TagsM&AAcquisitionSource', 'dataType': StringType(), 'personal': False, 'sensitive': True},
        {'name': 'TagsWebsitePlatform', 'dataType': StringType(), 'personal': False, 'sensitive': False},
        {'name': 'TagsOtherTags', 'dataType': StringType(), 'personal': False, 'sensitive': False}]}}
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### PROVIDER_V1 Schema
# ---

# CELL ********************

schema_Provider_v1 = [
    {'from': 'id', 'to': 'Id', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'type', 'to': 'Type', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'name', 'to': 'Name', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'displayName', 'to': 'DisplayName', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'description', 'to': 'Description', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'completion', 'to': 'Completion', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{completion}', 'sub_fields': [{'name': 'Completion', 'dataType': DecimalType(10, 7)}]}},
    {'from': 'fullName', 'to': 'FullName', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'status', 'to': 'Status', 'dataType': BooleanType(), 'personal': False, 'sensitive': True},
    {'from': 'level', 'to': 'Level', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
    {'from': 'createdAt', 'to': 'CreatedAt', 'dataType': DateType(), 'personal': False, 'sensitive': False},
    {'from': 'updatedAt', 'to': 'UpdatedAt', 'dataType': DateType(), 'personal': False, 'sensitive': False},
    {'from': 'lxState', 'to': 'LxState', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'alias', 'to': 'Alias', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'externalId', 'to': 'ExternalId', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{externalId}', 'sub_fields': [{'name': 'ExternalId', 'dataType': StringType()}]}},
    {'from': 'lifecycle', 'to': 'Lifecycle', 'personal': False, 'sensitive': True, 'nested': {'gql_string': '{asString phases {phase startDate }}', 'sub_fields': [
        {'name': 'LifecycleAsString', 'dataType': StringType(), 'personal': False, 'sensitive': True},
        {'name': 'LifecyclePlan', 'dataType': DateType(), 'personal': False, 'sensitive': False},
        {'name': 'LifecyclePhaseIn', 'dataType': DateType(), 'personal': False, 'sensitive': False},
        {'name': 'LifecycleActive', 'dataType': DateType(), 'personal': False, 'sensitive': False},
        {'name': 'LifecyclePhaseOut', 'dataType': DateType(), 'personal': False, 'sensitive': True},
        {'name': 'LifecycleEndOfLife', 'dataType': DateType(), 'personal': False, 'sensitive': True}]}},
    {'from': 'providerCriticality', 'to': 'ProviderCriticality', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'providerQuality', 'to': 'ProviderQuality', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'providerCriticalityDescription', 'to': 'ProviderCriticalityDescription', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'providerQualityDescription', 'to': 'ProviderQualityDescription', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'relToSuccessor', 'to': 'RelToSuccessor', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToSuccessor', 'dataType': ArrayType(StringType())}]}},
    {'from': 'relToPredecessor', 'to': 'RelToPredecessor', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToPredecessor', 'dataType': ArrayType(StringType())}]}},
    {'from': 'relToParent', 'to': 'RelToParent', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToParent', 'dataType': ArrayType(StringType())}]}},
    {'from': 'relToChild', 'to': 'RelToChild', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToChild', 'dataType': ArrayType(StringType())}]}},
    {'from': 'relToRequires', 'to': 'RelToRequires', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToRequires', 'dataType': ArrayType(StringType())}]}},
    {'from': 'relToRequiredBy', 'to': 'RelToRequiredBy', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToRequiredBy', 'dataType': ArrayType(StringType())}]}},
    {'from': 'relProviderToProject', 'to': 'RelProviderToProject', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelProviderToProject', 'dataType': ArrayType(StringType())}]}},
    {'from': 'relProviderToITComponent', 'to': 'RelProviderToITComponent', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelProviderToITComponent', 'dataType': ArrayType(StringType())}]}},
    {'from': 'tags', 'to': 'Tags', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{name tagGroup{name}}', 'sub_fields': [
        {'name': 'TagsDivestedTo', 'dataType': StringType(), 'personal': False, 'sensitive': False},
        {'name': 'TagsWebsitePurpose', 'dataType': StringType(), 'personal': False, 'sensitive': False},
        {'name': 'TagsEventArchitectures', 'dataType': StringType(), 'personal': False, 'sensitive': False},
        {'name': 'TagsHRIntegrationType', 'dataType': StringType(), 'personal': False, 'sensitive': True},
        {'name': 'TagsOtherTags', 'dataType': StringType(), 'personal': False, 'sensitive': False}]}},
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### INTERFACE_V1 Schema
# ---

# CELL ********************

schema_Interface_v1 = [
      {'from': 'id', 'to': 'Id', 'dataType': StringType(), 'personal': False, 'sensitive': False},
      {'from': 'type', 'to': 'Type', 'dataType': StringType(), 'personal': False, 'sensitive': False},
      {'from': 'name', 'to': 'Name', 'dataType': StringType(), 'personal': False, 'sensitive': False},
      {'from': 'displayName', 'to': 'DisplayName', 'dataType': StringType(), 'personal': False, 'sensitive': False},
      {'from': 'description', 'to': 'Description', 'dataType': StringType(), 'personal': False, 'sensitive': True},
      {'from': 'category', 'to': 'Category', 'dataType': StringType(), 'personal': False, 'sensitive': False},
      {'from': 'completion', 'to': 'Completion', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{completion}', 'sub_fields': [{'name': 'Completion', 'dataType': DecimalType(10, 7)}]}},
      {'from': 'fullName', 'to': 'FullName', 'dataType': StringType(), 'personal': False, 'sensitive': False},
      {'from': 'status', 'to': 'Status', 'dataType': StringType(), 'personal': False, 'sensitive': False},
      {'from': 'level', 'to': 'Level', 'dataType': StringType(), 'personal': False, 'sensitive': False},
      {'from': 'createdAt', 'to': 'CreatedAt', 'dataType': StringType(), 'personal': False, 'sensitive': False},
      {'from': 'updatedAt', 'to': 'UpdatedAt', 'dataType': StringType(), 'personal': False, 'sensitive': False},
      {'from': 'lxState', 'to': 'LxState', 'dataType': StringType(), 'personal': False, 'sensitive': False},
      {'from': 'release', 'to': 'Release', 'dataType': StringType(), 'personal': False, 'sensitive': False},
      {'from': 'alias', 'to': 'Alias', 'dataType': StringType(), 'personal': False, 'sensitive': False},
      {'from': 'externalId', 'to': 'ExternalId', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{externalId}', 'sub_fields': [{'name': 'ExternalId', 'dataType': StringType()}]}},
      {'from': 'lifecycle', 'to': 'Lifecycle', 'personal': False, 'sensitive': True, 'nested': {'gql_string': '{asString phases {phase startDate }}', 'sub_fields': [
            {'name': 'LifecycleAsString', 'dataType': StringType(), 'personal': False, 'sensitive': True},
            {'name': 'LifecyclePlan', 'dataType': DateType(), 'personal': False, 'sensitive': False},
            {'name': 'LifecycleActive', 'dataType': DateType(), 'personal': False, 'sensitive': False},
            {'name': 'LifecyclePhaseIn', 'dataType': DateType(), 'personal': False, 'sensitive': False},
            {'name': 'LifecyclePhaseOut', 'dataType': DateType(), 'personal': False, 'sensitive': False},
            {'name': 'LifecycleEndOfLife', 'dataType': DateType(), 'personal': False, 'sensitive': False}]}},
      {'from': 'dataFlowDirection', 'to': 'DataFlowDirection', 'dataType': StringType(), 'personal': False, 'sensitive': False},
      {'from': 'interfaceType', 'to': 'InterfaceType', 'dataType': StringType(), 'personal': False, 'sensitive': True},
      {'from': 'frequency', 'to': 'Frequency', 'dataType': StringType(), 'personal': False, 'sensitive': True},
      {'from': 'relToSuccessor', 'to': 'RelToSuccessor', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToSuccessor', 'dataType': ArrayType(StringType())}]}},
      {'from': 'relToPredecessor', 'to': 'RelToPredecessor', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToPredecessor', 'dataType': ArrayType(StringType())}]}},
      {'from': 'relToParent', 'to': 'RelToParent', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToParent', 'dataType': ArrayType(StringType())}]}},
      {'from': 'relToChild', 'to': 'RelToChild', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToChild', 'dataType': ArrayType(StringType())}]}},
      {'from': 'relToRequires', 'to': 'RelToRequires', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToRequires', 'dataType': ArrayType(StringType())}]}},
      {'from': 'relToRequiredBy', 'to': 'RelToRequiredBy', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToRequiredBy', 'dataType': ArrayType(StringType())}]}},
      {'from': 'relInterfaceToProviderApplication', 'to': 'RelInterfaceToProviderApplication', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelInterfaceToProviderApplication', 'dataType': ArrayType(StringType())}]}},
      {'from': 'relInterfaceToConsumerApplication', 'to': 'RelInterfaceToConsumerApplication', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelInterfaceToConsumerApplication', 'dataType': ArrayType(StringType())}]}},
      {'from': 'relInterfaceToDataObject', 'to': 'RelInterfaceToDataObject', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelInterfaceToDataObject', 'dataType': ArrayType(StringType())}]}},
      {'from': 'relInterfaceToITComponent', 'to': 'RelInterfaceToITComponent', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelInterfaceToITComponent', 'dataType': ArrayType(StringType())}]}},
      {'from': 'tags', 'to': 'Tags', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{name tagGroup{name}}', 'sub_fields': [
            {'name': 'TagsInterfaceType', 'dataType': StringType(), 'personal': False, 'sensitive': True},
            {'name': 'TagsDivestedTo', 'dataType': StringType(), 'personal': False, 'sensitive': False},
            {'name': 'TagsM&AStatus', 'dataType': StringType(), 'personal': False, 'sensitive': False},
            {'name': 'TagsWebsitePurpose', 'dataType': StringType(), 'personal': False, 'sensitive': False},
            {'name': 'TagsEventArchitectures', 'dataType': StringType(), 'personal': False, 'sensitive': False},
            {'name': 'TagsHRIntegrationType', 'dataType': StringType(), 'personal': False, 'sensitive': True},
            {'name': 'TagsM&AAcquisitionSource', 'dataType': StringType(), 'personal': False, 'sensitive': True},
            {'name': 'TagsOtherTags', 'dataType': StringType(), 'personal': False, 'sensitive': False}]}},
      {'from': 'subscriptions', 'to': 'Subscriptions', 'personal': True, 'sensitive': False, 'nested': {'gql_string': '{edges{node{type roles{name} user{email}}}}}', 'sub_fields': [
            {'name': 'SubscriptionsObserver', 'dataType': ArrayType(StringType()), 'personal': True, 'sensitive': False},
            {'name': 'SubscriptionsObserverSubscriber1', 'dataType': ArrayType(StringType()), 'personal': True, 'sensitive': False},
            {'name': 'SubscriptionsObserverDataSteward', 'dataType': ArrayType(StringType()), 'personal': True, 'sensitive': False},
            {'name': 'SubscriptionsObserverInterfaceOwner', 'dataType': ArrayType(StringType()), 'personal': True, 'sensitive': False},
            {'name': 'SubscriptionsObserverEnterpriseArchitect', 'dataType': ArrayType(StringType()), 'personal': True, 'sensitive': False}, 
            {'name': 'SubscriptionsObserverBusinessOwner', 'dataType': ArrayType(StringType()), 'personal': True, 'sensitive': False}, 
            {'name': 'SubscriptionsResponsible', 'dataType': ArrayType(StringType()), 'personal': True, 'sensitive': False}, 
            {'name': 'SubscriptionsResponsibleDataSteward', 'dataType': ArrayType(StringType()), 'personal': True, 'sensitive': False}, 
            {'name': 'SubscriptionsResponsibleInterfaceOwner', 'dataType': ArrayType(StringType()), 'personal': True, 'sensitive': False},  
            {'name': 'SubscriptionsResponsibleEnterpriseArchitect', 'dataType': ArrayType(StringType()), 'personal': True, 'sensitive': False}, 
            {'name': 'SubscriptionsResponsibleBusinessOwner', 'dataType': ArrayType(StringType()), 'personal': True, 'sensitive': False}, 
            {'name': 'SubscriptionsAccountable', 'dataType': ArrayType(StringType()), 'personal': True, 'sensitive': False}, 
            {'name': 'SubscriptionsAccountableDataSteward', 'dataType': ArrayType(StringType()), 'personal': True, 'sensitive': False}, 
            {'name': 'SubscriptionsAccountableInterfaceOwner', 'dataType': ArrayType(StringType()), 'personal': True, 'sensitive': False}, 
            {'name': 'SubscriptionsAccountableEnterpriseArchitect', 'dataType': ArrayType(StringType()), 'personal': True, 'sensitive': False},
            {'name': 'SubscriptionsAccountableBusinessOwner', 'dataType': ArrayType(StringType()), 'personal': True, 'sensitive': False}]}}
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### BUSINESSCAPABILITY_V1 Schema
# ---

# CELL ********************

schema_BusinessCapability_v1 = [
  {'from': 'id', 'to': 'Id', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'type', 'to': 'Type', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'name', 'to': 'Name', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'displayName', 'to': 'DisplayName', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'description', 'to': 'Description', 'dataType': StringType(), 'personal': False, 'sensitive': True},
  {'from': 'category', 'to': 'Category', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'completion', 'to': 'Completion', 'dataType': DecimalType(), 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{completion}', 'sub_fields': [{'name': 'Completion', 'dataType': DecimalType(3, 2)}]}},
  {'from': 'fullName', 'to': 'FullName', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'status', 'to': 'Status', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'level', 'to': 'Level', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
  {'from': 'createdAt', 'to': 'CreatedAt', 'dataType': DateType(), 'personal': False, 'sensitive': False},
  {'from': 'updatedAt', 'to': 'UpdatedAt', 'dataType': DateType(), 'personal': False, 'sensitive': False},
  {'from': 'lxState', 'to': 'LxState', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'alias', 'to': 'Alias', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'externalId', 'to': 'ExternalId', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{externalId}', 'sub_fields': [{'name': 'ExternalId', 'dataType': StringType()}]}},
  {'from': 'lifecycle', 'to': 'Lifecycle', 'personal': False, 'sensitive': True, 'nested': {'gql_string': '{asString phases {phase startDate }}', 'sub_fields': [
      {'name': 'LifecycleAsString', 'dataType': StringType(), 'personal': False, 'sensitive': False},
      {'name': 'LifecyclePlan', 'dataType': DateType(), 'personal': False, 'sensitive': True},
      {'name': 'LifecycleActive', 'dataType': DateType(), 'personal': False, 'sensitive': True},
      {'name': 'LifecyclePhaseIn', 'dataType': DateType(), 'personal': False, 'sensitive': True},
      {'name': 'LifecyclePhaseOut', 'dataType': DateType(), 'personal': False, 'sensitive': True},
      {'name': 'LifecycleEndOfLife', 'dataType': DateType(), 'personal': False, 'sensitive': True}]}},
  {'from': 'relToSuccessor', 'to': 'RelToSuccessor', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToSuccessor', 'dataType': ArrayType(StringType())}]}},
  {'from': 'relToPredecessor', 'to': 'RelToPredecessor', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToPredecessor', 'dataType': ArrayType(StringType())}]}},
  {'from': 'relToParent', 'to': 'RelToParent', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToParent', 'dataType': ArrayType(StringType())}]}},
  {'from': 'relToChild', 'to': 'RelToChild', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToChild', 'dataType': ArrayType(StringType())}]}},
  {'from': 'relToRequires', 'to': 'RelToRequires', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToRequires', 'dataType': ArrayType(StringType())}]}},
  {'from': 'relToRequiredBy', 'to': 'RelToRequiredBy', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToRequiredBy', 'dataType': ArrayType(StringType())}]}},
  {'from': 'relBusinessCapabilityToApplication', 'to': 'RelBusinessCapabilityToApplication', 'personal': False, 'sensitive': True,'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelBusinessCapabilityToApplication', 'dataType': ArrayType(StringType())}]}},
  {'from': 'tags', 'to': 'Tags', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{name tagGroup{name}}', 'sub_fields': [
      {'name': 'TagsDivestedTo', 'dataType': StringType(), 'personal': False, 'sensitive': False},
      {'name': 'TagsEventArchitectures', 'dataType': StringType(), 'personal': False, 'sensitive': False},
      {'name': 'TagsHRIntegrationType', 'dataType': StringType(), 'personal': False, 'sensitive': False},
      {'name': 'TagsDivisionCreatedCapability', 'dataType': StringType(), 'personal': False, 'sensitive': False},
      {'name': 'TagsOtherTags', 'dataType': StringType(), 'personal': False, 'sensitive': False}]}},
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### DATAOBJECT_V1 Schema
# ---

# CELL ********************

schema_DataObject_v1 = [
  {'from': 'id', 'to': 'Id', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'type', 'to': 'Type', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'name', 'to': 'Name', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'displayName', 'to': 'DisplayName', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'description', 'to': 'Description', 'dataType': StringType(), 'personal': False, 'sensitive': True},
  {'from': 'category', 'to': 'Category', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'completion', 'to': 'Completion', 'dataType': DecimalType(), 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{completion}', 'sub_fields': [{'name': 'Completion', 'dataType': DecimalType(3, 2)}]}},
  {'from': 'fullName', 'to': 'FullName', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'status', 'to': 'Status', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'level', 'to': 'Level', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
  {'from': 'createdAt', 'to': 'CreatedAt', 'dataType': DateType(), 'personal': False, 'sensitive': False},
  {'from': 'updatedAt', 'to': 'UpdatedAt', 'dataType': DateType(), 'personal': False, 'sensitive': False},
  {'from': 'lxState', 'to': 'LxState', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'alias', 'to': 'Alias', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'externalId', 'to': 'ExternalId', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{externalId}', 'sub_fields': [{'name': 'ExternalId', 'dataType': StringType()}]}},
  {'from': 'lifecycle', 'to': 'Lifecycle', 'personal': False, 'sensitive': True, 'nested': {'gql_string': '{asString phases {phase startDate }}', 'sub_fields': [
      {'name': 'LifecycleAsString', 'dataType': StringType(), 'personal': False, 'sensitive': True},
      {'name': 'LifecyclePlan', 'dataType': DateType(), 'personal': False, 'sensitive': True},
      {'name': 'LifecycleActive', 'dataType': DateType(), 'personal': False, 'sensitive': True},
      {'name': 'LifecyclePhaseIn', 'dataType': DateType(), 'personal': False, 'sensitive': True},
      {'name': 'LifecyclePhaseOut', 'dataType': DateType(), 'personal': False, 'sensitive': True},
      {'name': 'LifecycleEndOfLife', 'dataType': DateType(), 'personal': False, 'sensitive': True}]}},
  {'from': 'tags', 'to': 'Tags', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{name tagGroup{name}}', 'sub_fields': [
      {'name': 'TagsDivestedTo', 'dataType': StringType(), 'personal': False, 'sensitive': False},
      {'name': 'TagsEventArchitectures', 'dataType': StringType(), 'personal': False, 'sensitive': False},
      {'name': 'TagsHRIntegrationType', 'dataType': StringType(), 'personal': False, 'sensitive': False},
      {'name': 'TagsDataObjectType', 'dataType': StringType(), 'personal': False, 'sensitive': False},
      {'name': 'TagsOtherTags', 'dataType': StringType(), 'personal': False, 'sensitive': False}]}},
  {'from': 'relToSuccessor', 'to': 'RelToSuccessor', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToSuccessor', 'dataType': ArrayType(StringType())}]}},
  {'from': 'relToPredecessor', 'to': 'RelToPredecessor', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToPredecessor', 'dataType': ArrayType(StringType())}]}},
  {'from': 'relToParent', 'to': 'RelToParent', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToParent', 'dataType': ArrayType(StringType())}]}},
  {'from': 'relToChild', 'to': 'RelToChild', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToChild', 'dataType': ArrayType(StringType())}]}},
  {'from': 'relToRequires', 'to': 'RelToRequires', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToRequires', 'dataType': ArrayType(StringType())}]}},
  {'from': 'relToRequiredBy', 'to': 'RelToRequiredBy', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToRequiredBy', 'dataType': ArrayType(StringType())}]}},
  {'from': 'relDataObjectToApplication', 'to': 'RelDataObjectToApplication', 'personal': False, 'sensitive': True,'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelDataObjectToApplication', 'dataType': ArrayType(StringType())}]}},
  {'from': 'dataClassification', 'to': 'DataClassification', 'dataType': StringType(), 'personal': False, 'sensitive': True},
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### ITCOMPONENT Schema
# ---

# CELL ********************

schema_ITComponent_v1 = [
  {'from': 'id', 'to': 'Id', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'type', 'to': 'Type', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'name', 'to': 'Name', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'displayName', 'to': 'DisplayName', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'description', 'to': 'Description', 'dataType': StringType(), 'personal': False, 'sensitive': True},
  {'from': 'category', 'to': 'Category', 'dataType': StringType(), 'personal': False, 'sensitive': True},
  {'from': 'completion', 'to': 'Completion', 'dataType': DecimalType(), 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{completion}', 'sub_fields': [{'name': 'Completion', 'dataType': DecimalType(3, 2)}]}},
  {'from': 'fullName', 'to': 'FullName', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'status', 'to': 'Status', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'level', 'to': 'Level', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
  {'from': 'createdAt', 'to': 'CreatedAt', 'dataType': DateType(), 'personal': False, 'sensitive': False},
  {'from': 'updatedAt', 'to': 'UpdatedAt', 'dataType': DateType(), 'personal': False, 'sensitive': False},
  {'from': 'lxState', 'to': 'LxState', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'release', 'to': 'Release', 'dataType': StringType(), 'personal': False, 'sensitive': True},
  {'from': 'alias', 'to': 'Alias', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'externalId', 'to': 'ExternalId', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{externalId}', 'sub_fields': [{'name': 'ExternalId', 'dataType': StringType()}]}},
  {'from': 'lifecycle', 'to': 'Lifecycle', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{asString phases {phase startDate }}', 'sub_fields': [
      {'name': 'LifecycleAsString', 'dataType': StringType(), 'personal': False, 'sensitive': True},
      {'name': 'LifecyclePlan', 'dataType': DateType(), 'personal': False, 'sensitive': True},
      {'name': 'LifecycleActive', 'dataType': DateType(), 'personal': False, 'sensitive': True},
      {'name': 'LifecyclePhaseIn', 'dataType': DateType(), 'personal': False, 'sensitive': True},
      {'name': 'LifecyclePhaseOut', 'dataType': DateType(), 'personal': False, 'sensitive': True},
      {'name': 'LifecycleEndOfLife', 'dataType': DateType(), 'personal': False, 'sensitive': True}]}},
  {'from': 'location', 'to': 'Location','personal': True, 'sensitive': False, 'nested': {'gql_string': '{geoAddress}', 'sub_fields': [{'name': 'GeoAddress', 'dataType': StringType()}]}},
  {'from': 'technicalSuitability', 'to': 'TechnicalSuitability', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'relITComponentToProvider', 'to': 'RelITComponentToProvider', 'personal': False, 'sensitive': False,'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelITComponentToProvider', 'dataType': ArrayType(StringType())}]}},
  {'from': 'relToSuccessor', 'to': 'RelToSuccessor', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToSuccessor', 'dataType': ArrayType(StringType())}]}},
  {'from': 'relToPredecessor', 'to': 'RelToPredecessor', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToPredecessor', 'dataType': ArrayType(StringType())}]}},
  {'from': 'relToParent', 'to': 'RelToParent', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToParent', 'dataType': ArrayType(StringType())}]}},
  {'from': 'relToChild', 'to': 'RelToChild', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToChild', 'dataType': ArrayType(StringType())}]}},
  {'from': 'relToRequires', 'to': 'RelToRequires', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToRequires', 'dataType': ArrayType(StringType())}]}},
  {'from': 'relToRequiredBy', 'to': 'RelToRequiredBy', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelToRequiredBy', 'dataType': ArrayType(StringType())}]}},
  {'from': 'relITComponentToProject', 'to': 'RelITComponentToProject', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelITComponentToProject', 'dataType': ArrayType(StringType())}]}},
  {'from': 'relITComponentToTechnologyStack', 'to': 'RelITComponentToTechnologyStack', 'personal': False, 'sensitive': True, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelITComponentToTechnologyStack', 'dataType': ArrayType(StringType())}]}},
  {'from': 'relITComponentToApplication', 'to': 'RelITComponentToApplication', 'personal': False, 'sensitive': True, 'nested': {'gql_string': '{edges{node{factSheet{name}}}}', 'sub_fields': [{'name': 'RelITComponentToApplication', 'dataType': ArrayType(StringType())}]}},
  {'from': 'tags', 'to': 'Tags', 'personal': False, 'sensitive': False, 'nested': {'gql_string': '{name tagGroup{name}}', 'sub_fields': [
      {'name': 'TagsDivestedTo', 'dataType': StringType(), 'personal': False, 'sensitive': False},
      {'name': 'TagsM&AStatus', 'dataType': StringType(), 'personal': False, 'sensitive': False},
      {'name': 'TagsEventArchitectures', 'dataType': StringType(), 'personal': False, 'sensitive': False},
      {'name': 'TagsHostingType', 'dataType': StringType(), 'personal': False, 'sensitive': True},
      {'name': 'TagsHRIntegrationType', 'dataType': StringType(), 'personal': False, 'sensitive': False},
      {'name': 'TagsOtherTags', 'dataType': StringType(), 'personal': False, 'sensitive': False}]}},
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
