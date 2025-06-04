# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# ##### DIM_APPLICATION_V1 Schema
# ---

# CELL ********************

schema_dim_application_v1 = [
    # Common Fields
    {'field': 'ApplicationKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'Name', 'Application': 'Name'}, 'calculated_field': True},
    {'field': 'Name', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'Name', 'Application': 'Name'}},
    {'field': 'ApplicationType', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'SysClassName', 'Application': 'TagsApplicationType'}},
    {'field': 'ApplicationDescription', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'cmdb_ci_appl': 'ShortDescription', 'Application': 'Description'}},
    {'field': 'LastUpdatedOnDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'SysUpdatedOn', 'Application': 'UpdatedAt'}},
    {'field': 'ReceiptDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'ReceiptDate', 'Application': 'ReceiptDate'}},
    {'field': 'AllocatedDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'AllocatedDate', 'Application': 'AllocatedDate'}},
    {'field': 'SourceSystem', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'SourceSystem', 'Application': 'SourceSystem'}},
    {'field': 'PipelineUpdatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'PipelineUpdatedDate', 'Application': 'PipelineUpdatedDate'}},
    {'field': 'LeanIXExternalID', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'UUniqueIdentifier', 'Application': 'ExternalId'}},
    {'field': 'TableName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'TableName', 'Application': 'TableName'}},

    # LeanIX fields
    {'field': 'DisplayName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Application': 'DisplayName'}},
    {'field': 'Alias', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Application': 'Alias'}},
    {'field': 'URLID', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Application': 'Id'}},
    {'field': 'CrownJewelsKeyApplication', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'Application': 'TagsImportantApplication'}},
    {'field': 'FactSheetTotalCompletion', 'dataType': DecimalType(3, 2), 'personal': False, 'sensitive': False, 'from': {'Application': 'Completion'}},
    {'field': 'ApplicationStatus', 'dataType': BooleanType(), 'personal': False, 'sensitive': True, 'from': {'Application': 'Status'}},
    {'field': 'HierarchyLevel', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'Application': 'Level'}},
    {'field': 'HierarchyLevel1', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'Application': 'RelToParent'}, 'calculated_field': True},
    {'field': 'HierarchyLevel2', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'Application': 'RelToParent'}, 'calculated_field': True},
    {'field': 'HierarchyLevel3', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'Application': 'RelToParent'}, 'calculated_field': True},
    {'field': 'CurrentLifecycleState', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'Application': 'LifecycleAsString'}},
    {'field': 'LifecyclePlanDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'Application': 'LifecyclePlan'}},
    {'field': 'LifecyclePhaseInDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'Application': 'LifecyclePhaseIn'}},
    {'field': 'LifecycleActiveDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'Application': 'LifecycleActive'}},
    {'field': 'LifecyclePhaseOutDate', 'dataType': DateType(), 'personal': False, 'sensitive': True, 'from': {'Application': 'LifecyclePhaseOut'}},
    {'field': 'LifecycleEndOfLifeDate', 'dataType': DateType(), 'personal': False, 'sensitive': True, 'from': {'Application': 'LifecycleEndOfLife'}},

    # ServiceNow fields
    {'field': 'BusinessCriticality', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'cmdb_ci_appl': 'BusinessCriticality'}},
    {'field': 'PrimaryParent', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'UPrimaryParent'}},
    {'field': 'FirstLineSupportGroup', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'SupportGroup'}},
    {'field': 'SecondLineSupportGroup', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'UTechnicalGroup'}},
    {'field': 'ChangeControlGroup', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'ChangeControl'}},
    {'field': 'OwnerGroup', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'UOwnerGroup'}},
    {'field': 'IsActive', 'dataType': BooleanType(), 'personal': False, 'sensitive': True, 'from': {'Application': 'Status'}},
    {'field': 'AdditionalNotes', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'cmdb_ci_appl': 'UAdditionalNotes'}},
    {'field': 'BusinessContinuityOwnerKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'UBCOwner'}, 'calculated_field': True},
    {'field': 'BusinessContinuityStatus', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'UBusinessContinuityStatus'}},
    {'field': 'BusinessGroup', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'UBusinessGroup'}},
    {'field': 'CrownJewelsName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'UCrownJewelsName'}},
    {'field': 'CrownJewelsVisible', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'UCrownJewelsVisible'}},
    {'field': 'CreatedDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'SysCreatedOn'}},
    {'field': 'DisasterRecoveryOwnerKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'UDROwner'}, 'calculated_field': True},
    {'field': 'DisasterRecoveryStatus', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'UDRStatus'}},
    {'field': 'DeploymentModel', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'UDeploymentModel'}},
    {'field': 'ApplicationTier', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'UDesiredBusinessCriticality'}},
    {'field': 'InformaDivision', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'UDivision'}},
    {'field': 'DomainName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'Fqdn'}},
    {'field': 'DomainKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'Fqdn'}, 'calculated_field': True}, 
    {'field': 'ImpactedInformaDivision', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'UImpactedDivision'}},
    {'field': 'LeavingDate', 'dataType': DateType(), 'personal': True, 'sensitive': False, 'from': {'cmdb_ci_appl': 'ULeavingDate'}},
    {'field': 'ApplicationUsageRegion', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'Location'}},
    {'field': 'IsApplicationSupported', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'UNoLongerSupported'}},
    {'field': 'OperationalStatus', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'OperationalStatus'}},
    {'field': 'DisasterRecoveryTestDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'UDRPLastTested'}},
    {'field': 'OwnedByKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'OwnedBy'}, 'calculated_field': True},
    {'field': 'InformaOwningDivision', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'UOwningDivision'}},
    {'field': 'RecoveryPointObjective', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'USystemRpo'}},
    {'field': 'RecoveryTimeObjective', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'USystemRto'}},
    {'field': 'IsVisibleOnPortalStatusPage', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'UShowOnServiceStatusPage'}},
    {'field': 'EffectiveDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'StartDate'}},
    {'field': 'UpdatedCount', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'SysModCount'}},
    {'field': 'SupplierName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'Vendor'}},
    {'field': 'SupplierKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_appl': 'Vendor'}, 'calculated_field': True}
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
