# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# ##### DIM_SUPPLIER_SOURCE_V1 Schema
# ---

# CELL ********************

schema_dim_supplier_source_v1 = [
  # Common Fields
  {'field': 'SupplierKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'Name', 'core_company': 'Name', 'suppliers': 'Name'}, 'calculated_field': True},
  {'field': 'SupplierName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'Name', 'core_company': 'Name', 'suppliers': 'Name'}},
  {'field': 'SupplierParentKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'RelToParent', 'suppliers': 'Parent'}, 'calculated_field': True},
  {'field': 'DisplayName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'DisplayName', 'suppliers': 'DisplayName'}},
  {'field': 'Parent', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'RelToParent', 'suppliers': 'Parent'}},
  {'field': 'SupplierStatus', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'Provider': 'Status', 'core_company': 'UActive'}},
  {'field': 'SupplierId', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'Id', 'suppliers': 'Id'}},
  {'field': 'SupplierBusinessCriticality', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'Provider': 'ProviderCriticality', 'core_company': 'UBusinessCriticality'}},
  {'field': 'CreatedByKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'core_company': 'SysCreatedBy'}, 'calculated_field': True},
  {'field': 'ReceiptDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'ReceiptDate', 'core_company': 'ReceiptDate', 'suppliers': 'ReceiptDate'}},
  {'field': 'AllocatedDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'AllocatedDate', 'core_company': 'AllocatedDate', 'suppliers': 'AllocatedDate'}},
  {'field': 'SourceSystem', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'SourceSystem', 'core_company': 'SourceSystem', 'suppliers': 'SourceSystem'}},
  {'field': 'CreatedDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'CreatedAt', 'core_company': 'SysCreatedOn', 'suppliers': 'CreatedAt'}},
  {'field': 'LastUpdatedByKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'core_company': 'SysUpdatedBy'}, 'calculated_field': True},
  {'field': 'LastUpdatedDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'UpdatedAt', 'core_company': 'SysUpdatedOn', 'suppliers': 'UpdatedAt'}},
  {'field': 'PipelineUpdatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'PipelineUpdatedDate', 'core_company': 'PipelineUpdatedDate', 'suppliers': 'PipelineUpdatedDate'}},
  {'field': 'TableName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'TableName', 'core_company': 'TableName', 'suppliers': 'TableName'}},

  # LeanIX specific fields 
  {'field': 'Type', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'Type'}},
  {'field': 'Description', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'Provider': 'Description'}},
  {'field': 'Completion', 'dataType': DecimalType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'Completion'}},
  {'field': 'FullName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'FullName'}},
  {'field': 'Level', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'Level'}},
  {'field': 'LxState', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'LxState'}},
  {'field': 'Alias', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'Alias'}},
  {'field': 'ExternalId', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'ExternalId'}},
  {'field': 'LifecycleAsString', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'Provider': 'LifecycleAsString'}},
  {'field': 'LifecyclePlan', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'LifecyclePlan'}},
  {'field': 'LifecyclePhaseIn', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'LifecyclePhaseIn'}},
  {'field': 'LifecycleActive', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'LifecycleActive'}},
  {'field': 'LifecyclePhaseOut', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'LifecyclePhaseOut'}},
  {'field': 'LifecycleEndOfLife', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'LifecycleEndOfLife'}},
  {'field': 'ProviderQuality', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'ProviderQuality'}},
  {'field': 'ProviderQualityDescription', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'Provider': 'ProviderQualityDescription'}},
  {'field': 'ProviderCriticalityDescription', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'Provider': 'ProviderCriticalityDescription'}},
  {'field': 'Successor', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'RelToSuccessor'}},
  {'field': 'Predecessor', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'RelToPredecessor'}},
  {'field': 'Child', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'RelToChild'}},
  {'field': 'Requires', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'RelToRequires'}},
  {'field': 'RequiredBy', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'RelToRequiredBy'}},
  {'field': 'Project', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'RelProviderToProject'}},
  {'field': 'ITComponent', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'RelProviderToITComponent'}},
  {'field': 'DivestedTo', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'TagsDivestedTo'}},
  {'field': 'WebsitePurpose', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'TagsWebsitePurpose'}},
  {'field': 'EventArchitectures', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'TagsEventArchitectures'}},
  {'field': 'HRIntegrationType', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'Provider': 'TagsHRIntegrationType'}},
  {'field': 'OtherTags', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'Provider': 'TagsOtherTags'}},

  # ServiceNow specific fields
  {'field': 'SupplierTier', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'core_company': 'RankTier'}},
  {'field': 'AdditionalServiceCharges', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'core_company': 'UAdditionalServiceCharges'}},
  {'field': 'SupplierAssessmentFrequency', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'core_company': 'UAssessmentFrequency'}},
  {'field': 'BusinessOwnerKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'core_company': 'UBusinessOwner'}, 'calculated_field': True},
  #{'field': 'BusinessStakeholdersKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'core_company': 'UBusinessStakeholders'}, 'calculated_field': True},
  {'field': 'Class', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'core_company': 'SysClassName'}},
  {'field': 'ContractTermInMonths', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'core_company': 'UContractTermInMonths'}},
  {'field': 'IsSupplierACustomer', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'core_company': 'Customer'}},
  {'field': 'OneOffAssessmentDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'core_company': 'UDateOfTheOneOffAssessment'}},
  {'field': 'DescriptionOfServicesProvided', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'core_company': 'UDescriptionOfServicesProvided'}},
  {'field': 'Division', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'core_company': 'UDivision'}},
  {'field': 'IsSupplierHIPAACompliant', 'dataType': BooleanType(), 'personal': False, 'sensitive': True, 'from': {'core_company': 'UHIPAA'}},
  {'field': 'HardwareSoftwareLicenseAdjustmentIncluded', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'core_company': 'UHardwareSoftware'}},
  {'field': 'HighestClassificationOfInformaDataProcessed', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'core_company': 'UHighestClassificationOfInformaDataProcessed'}},
  {'field': 'HowToInvokeServiceCredits', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'core_company': 'UHowToInvokeServiceCredits'}},
  {'field': 'InformaResponsibilities', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'core_company': 'UInformaResponsibilities'}},
  {'field': 'IntellectualProperty', 'dataType': BooleanType(), 'personal': False, 'sensitive': True, 'from': {'core_company': 'UIntellectualProperty'}},
  {'field': 'Latitude', 'dataType': DecimalType(8,2), 'personal': False, 'sensitive': False, 'from': {'core_company': 'Latitude'}},
  {'field': 'LocationOfAssessmentReportsAndDocuments', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'core_company': 'UAssessmentsReportsAndDocuments'}},
  {'field': 'Longitude', 'dataType': DecimalType(8,2), 'personal': False, 'sensitive': False, 'from': {'core_company': 'Longitude'}},
  {'field': 'IsManufacturer', 'dataType':StringType(), 'personal': False, 'sensitive': False, 'from': {'core_company': 'Manufacturer'}},
  {'field': 'NextServiceReviewDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'core_company': 'UNextServiceReviewDate'}},
  {'field': 'Notes', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'core_company': 'Notes'}},
  {'field': 'NoticePeriodToCease', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'core_company': 'UNoticePeriodToCease'}},
  {'field': 'IsVendor', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'core_company': 'Vendor'}},
  {'field': 'SecurityAssesment', 'dataType': BooleanType(), 'personal': False, 'sensitive': True, 'from': {'core_company': 'USecurityAssessment'}},
  {'field': 'SecurityAssesmentCompletedDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': True, 'from': {'core_company': 'USecurityAssessmentCompletedDate'}},
  {'field': 'SecurityAssesmentDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': True, 'from': {'core_company': 'USecurityAssessmentDate'}},
  {'field': 'SecurityAssesmentRequired', 'dataType': BooleanType(), 'personal': False, 'sensitive': True, 'from': {'core_company': 'USecurityAssessmentRequired'}},
  {'field': 'SecurityAssesmentStartedDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': True, 'from': {'core_company': 'USecurityAssessmentStartDate'}},
  {'field': 'SecurityServiceOwnerKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'core_company': 'USecurityServiceOwner'}},

  # Coupa specific fields
  {'field': 'AccountNumber', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'suppliers': 'AccountNumber'}},
  {'field': 'ContentGroups', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'suppliers': 'BusinessGroups'}},
  {'field': 'SupplierIndustry', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'suppliers': 'Commodity'}},
  #{'field': 'CorporateUrl', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'suppliers': 'CorporateUrl'}},
  {'field': 'Enterprise', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'suppliers': 'Enterprise'}},
  {'field': 'OnlineStore', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'suppliers': 'OnlineStore'}},
  {'field': 'PaymentMethod', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'suppliers': 'PaymentMethod'}},
  {'field': 'PaymentTerm', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'suppliers': 'PaymentTerm'}},
  {'field': 'PrimaryAddress', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'suppliers': 'PrimaryAddress'}},
  #{'field': 'PrimaryContactKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'suppliers': 'PrimaryContact'}, 'calculated_field': True},
  {'field': 'SavingsPct', 'dataType': DecimalType(8,2), 'personal': False, 'sensitive': True, 'from': {'suppliers': 'SavingsPct'}},
  {'field': 'Website', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'suppliers': 'Website'}},
  {'field': 'SupplierIndustry2', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'suppliers': 'PreferredCommodities'}},
]    

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
