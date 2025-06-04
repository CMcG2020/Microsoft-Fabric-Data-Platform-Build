# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# ##### FACT_CONTRACT_V1 Schema
# ---

# CELL ********************

schema_fact_contract_v1 = [
    {'field': 'SupplierKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'Name'}, 'calculated_field': True},
    {'field': 'ContractId', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'Id'}},
    {'field': 'ContractNumber', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'Number'}},
    {'field': 'SupplierName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'SupplierName'}},
    {'field': 'ContractName', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'Name'}},
    {'field': 'ContractStart', 'dataType': TimestampType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'StartDate'}},
    {'field': 'ContractExpiry', 'dataType': TimestampType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'EndDate'}},
    {'field': 'Status', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'Status'}},
    {'field': 'TotalContractValue', 'dataType': DecimalType(12, 2), 'personal': False, 'sensitive': True, 'from': {'contracts': 'MinCommit'}},
    {'field': 'Description', 'dataType': StringType(), 'personal': True, 'sensitive': True, 'from': {'contracts': 'Description'}},
    {'field': 'IsContainsConfidentialInformation', 'dataType': BooleanType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'CustomFieldsConfidentialInformation'}},
    {'field': 'Department', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'Department'}},
    {'field': 'HierarchyType', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'Type'}},
    {'field': 'ContentGroups', 'dataType': ArrayType(StringType()), 'personal': False, 'sensitive': False, 'from': {'contracts': 'ContentGroups'}},
    {'field': 'InternalProduct', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'CustomFieldsInternalProduct'}},
    {'field': 'CreatedDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'CreatedAt'}},
    {'field': 'LastUpdatedByKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'UpdatedBy'}, 'calculated_field': True},
    {'field': 'CreatedByKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'CreatedBy'}, 'calculated_field': True},
    {'field': 'LastUpdatedDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'UpdatedAt'}},
    {'field': 'Currency', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'Currency'}},
    {'field': 'LegalEntity', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'CustomFieldsLegalEntity'}},
    {'field': 'LegalJurisdiction', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'ContractType'}},
    {'field': 'ApproverKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'CustomFieldsContractApprover'}, 'calculated_field': True},
    {'field': 'AutoRenewalsRemaining', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'NoOfRenewals'}},
    {'field': 'AutomaticallyUpdateExpiryDate', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'AutoExtendEndDateForRenewal'}},
    {'field': 'OwnerKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'ContractOwner'}, 'calculated_field': True},
    {'field': 'NextReviewDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'CustomFieldsNextReviewDate'}},
    {'field': 'ParentContractName', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'ParentName'}},
    {'field': 'ParentContractNumber', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'ParentId'}},
    {'field': 'PaymentTerm', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'PaymentTerm'}},
    {'field': 'PersonalData', 'dataType': BooleanType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'CustomFieldsPersonalData'}},
    {'field': 'RegionOrCity', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'CustomFieldsRegionOrCity'}},
    {'field': 'TermType', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'TermType'}},
    {'field': 'SystemsAccessIntegration', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'CustomFieldsSystemsAccessIntegration'}},
    {'field': 'Terminated', 'dataType': BooleanType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'Terminated'}},
    {'field': 'AllocatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'AllocatedDate'}},
    {'field': 'SourceSystem', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'SourceSystem'}},
    {'field': 'PipelineUpdatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'PipelineUpdatedDate'}},
    {'field': 'TableName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'TableName'}}
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### FACT_CONTRACT_V2 Schema
# ---

# CELL ********************

schema_fact_contract_v2 = [
    {'field': 'ContractKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'Id'}, 'calculated_field': True},
    {'field': 'SupplierKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'SupplierName'}, 'calculated_field': True},
    {'field': 'ApproverKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'CustomFieldsContractApprover'}, 'calculated_field': True},
    {'field': 'LastUpdatedDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'UpdatedAt'}},
    {'field': 'HierarchyType', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'Type'}},
    {'field': 'TermType', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'TermType'}},
    {'field': 'Terminated', 'dataType': BooleanType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'Terminated'}},
    {'field': 'ContractId', 'dataType': IntegerType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'Id'}},
    {'field': 'SupplierName', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'SupplierName'}},
    {'field': 'Status', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'Status'}},
    {'field': 'ContractStartDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'StartDate'}},
    {'field': 'PaymentTerm', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'PaymentTerm'}},
    {'field': 'ParentContractName', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'ParentName'}},
    {'field': 'ParentContractID', 'dataType': IntegerType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'ParentId'}},
    {'field': 'ContractNumber', 'dataType': IntegerType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'Number'}},
    {'field': 'AutoRenewalsRemaining', 'dataType': IntegerType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'NoOfRenewals'}},
    {'field': 'ContractName', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'Name'}},
    {'field': 'ContractExpiry', 'dataType': TimestampType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'EndDate'}},
    {'field': 'TotalContractValue', 'dataType': DecimalType(12, 2), 'personal': False, 'sensitive': True, 'from': {'contracts': 'MinCommit'}},
    {'field': 'Description', 'dataType': StringType(), 'personal': True, 'sensitive': True, 'from': {'contracts': 'Description'}},
    {'field': 'IsContainsConfidentialInformation', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'CustomFieldsConfidentialInformation'}},
    {'field': 'Department', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'Department'}},
    {'field': 'SystemsAccessIntegration', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'CustomFieldsSystemsAccessIntegration'}},
    {'field': 'RegionOrCity', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'CustomFieldsRegionOrCity'}},
    {'field': 'PersonalData', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'CustomFieldsPersonalData'}},
    {'field': 'NextReviewDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'CustomFieldsNextReviewDate'}},
    {'field': 'LegalEntity', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'CustomFieldsLegalEntity'}},
    {'field': 'InternalProduct', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'CustomFieldsInternalProduct'}},
    {'field': 'Currency', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'Currency'}},
    {'field': 'ContentGroups', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'ContentGroups'}},
    {'field': 'CreatedDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': True, 'from': {'contracts': 'CreatedAt'}},
    {'field': 'LegalJurisdiction', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'ContractType'}},
    {'field': 'AutomaticallyUpdateExpiryDate', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'AutoExtendEndDateForRenewal'}},
    {'field': 'AllocatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'AllocatedDate'}},
    {'field': 'SourceSystem', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'SourceSystem'}},
    {'field': 'PipelineUpdatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'PipelineUpdatedDate'}},
    {'field': 'TableName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'contracts': 'TableName'}}
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
