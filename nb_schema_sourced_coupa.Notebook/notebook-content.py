# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse_name": "",
# META       "default_lakehouse_workspace_id": ""
# META     }
# META   }
# META }

# MARKDOWN ********************

# ##### SUPPLIERS_V1 Schema
# ---

# CELL ********************

schema_suppliers_v1 = [
    {'from': 'account-number', 'to': 'AccountNumber', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'account-types', 'to': 'AccountTypes', 'dataType': ArrayType(StringType()), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
    {'from': 'allow-change-requests', 'to': 'AllowChangeRequests', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'allow-cn-no-backing-doc-from-connect', 'to': 'AllowCnNoBackingDocFromConnect', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'allow-cxml-invoicing', 'to': 'AllowCxmlInvoicing', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'allow-inv-choose-billing-account', 'to': 'AllowInvChooseBillingAccount', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'allow-inv-from-connect', 'to': 'AllowInvFromConnect', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'allow-inv-no-backing-doc-from-connect', 'to': 'AllowInvNoBackingDocFromConnect', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'allow-inv-unbacked-lines-from-connect', 'to': 'AllowInvUnbackedLinesFromConnect', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'allow-order-confirmation-item-substitutions', 'to': 'AllowOrderConfirmationItemSubstitutions', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'business-entity-id', 'to': 'BusinessEntityId', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'content-groups', 'to': 'BusinessGroups', 'dataType': ArrayType(StringType()), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
    {'from': 'buyer-hold', 'to': 'BuyerHold', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'commodity', 'to': 'Commodity', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
    {'from': 'confirm-by-hrs', 'to': 'ConfirmByHrs', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'coupa-pay-financing-only', 'to': 'CoupaPayFinancingOnly', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'created-at', 'to': 'CreatedAt', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'cxml-url', 'to': 'CxmlUrl', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'default-locale', 'to': 'DefaultLocale', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'disable-cert-verify', 'to': 'DisableCertVerify', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'display-name', 'to': 'DisplayName', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'do-not-accelerate', 'to': 'DoNotAccelerate', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'enterprise', 'to': 'Enterprise', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
    {'from': 'id', 'to': 'Id', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
    {'from': 'inventory-organization', 'to': 'InventoryOrganization', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'description', 'dataType': StringType()}]}},
    {'from': 'invoice-matching-level', 'to': 'InvoiceMatchingLevel', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'name', 'to': 'Name', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'number', 'to': 'Number', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
    {'from': 'one-time-supplier', 'to': 'OneTimeSupplier', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'on-hold', 'to': 'OnHold', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'online-store', 'to': 'OnlineStore', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'url', 'dataType': StringType()}]}},
    {'from': 'order-confirmation-level', 'to': 'OrderConfirmationLevel', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'parent', 'to': 'Parent', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
    {'from': 'payment-method', 'to': 'PaymentMethod', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'payment-term', 'to': 'PaymentTerm', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'nested': {'sub_fields': [{'name': 'code', 'dataType': StringType()}]}},
    {'from': 'po-change-method', 'to': 'PoChangeMethod', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'po-method', 'to': 'PoMethod', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'preferred-commodities', 'to': 'PreferredCommodities', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
    {'from': 'primary-address', 'to': 'PrimaryAddress', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [
        {'name': 'street1', 'dataType': StringType()},
        {'name': 'street2', 'dataType': StringType()},
        {'name': 'street3', 'dataType': StringType()},
        {'name': 'street4', 'dataType': StringType()},
        {'name': 'city', 'dataType': StringType()},
        {'name': 'state', 'dataType': StringType()},
        {'name': 'postal-code', 'dataType': StringType()}]}},
    {'from': 'primary-contact', 'to': 'PrimaryContact', 'dataType': StringType(), 'personal': True, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'email', 'dataType': StringType()}]}},
    #{'from': 'remit-to-addresses', 'to': 'RemitToAddresses', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'restricted-account-types', 'to': 'RestrictedAccountTypes', 'dataType': ArrayType(StringType()), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
    {'from': 'savings-pct', 'to': 'SavingsPct', 'dataType': FloatType(), 'personal': False, 'sensitive': True},
    {'from': 'scope-three-emissions', 'to': 'ScopeThreeEmissions', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'send-invoices-to-approvals', 'to': 'SendInvoicesToApprovals', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'shipping-term', 'to': 'ShippingTerm', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'code', 'dataType': StringType()}]}},
    {'from': 'status', 'to': 'Status', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'supplier-addresses', 'to': 'SupplierAddresses', 'dataType': ArrayType(StringType()), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [
        {'name': 'street1', 'dataType': StringType()},
        {'name': 'street2', 'dataType': StringType()},
        {'name': 'street3', 'dataType': StringType()},
        {'name': 'street4', 'dataType': StringType()},
        {'name': 'city', 'dataType': StringType()},
        {'name': 'state', 'dataType': StringType()},
        {'name': 'postal-code', 'dataType': StringType()}]}},
    {'from': 'taggings', 'to': 'Taggings', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'description', 'dataType': StringType()}]}},
    {'from': 'tax-code', 'to': 'TaxCode', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'code', 'dataType': StringType()}]}},
    {'from': 'tax-id', 'to': 'TaxId', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'type', 'to': 'Type', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'updated-at', 'to': 'UpdatedAt', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'website', 'to': 'Website', 'dataType': StringType(), 'personal': False, 'sensitive': False}
]


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### CONTRACTS_V1 Schema
# ---

# CELL ********************

schema_contracts_v1 = [
    {'from': 'number', 'to': 'Number', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'supplier', 'to': 'SupplierName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
    {'from': 'name', 'to': 'Name', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'start-date', 'to': 'StartDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': True},
    {'from': 'end-date', 'to': 'EndDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': True},
    {'from': 'status', 'to': 'Status', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'min-commit', 'to': 'MinCommit', 'dataType': DecimalType(12, 2), 'personal': False, 'sensitive': True},
    {'from': 'description', 'to': 'Description', 'dataType': StringType(), 'personal': True, 'sensitive': True},
    {'from': 'custom-fields', 'to': 'CustomFields', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'multi': True, 'sub_fields': [
        {'name': 'next-review-date','dataType': TimestampType(), 'personal': False, 'sensitive': True},
        {'name': 'personal-data', 'dataType': StringType(), 'personal': False, 'sensitive': True},
        {'name': 'confidential-information',  'dataType': StringType(), 'personal': False, 'sensitive': True},
        {'name': 'internal-product',  'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
        {'name': 'legal-entity',  'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
        {'name': 'contract-approver',  'dataType': StringType(), 'personal': True, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'fullname', 'dataType': StringType()}]}},
        {'name': 'region-or-city',  'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
        {'name': 'systems-access--integration',  'dataType': StringType(), 'personal': False, 'sensitive': False}]}},
    {'from': 'id', 'to': 'Id', 'dataType': IntegerType(), 'personal': False, 'sensitive': True},
    {'from': 'department', 'to': 'Department', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
    {'from': 'type', 'to': 'Type', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'content-groups', 'to': 'ContentGroups', 'dataType': ArrayType(StringType()), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
    {'from': 'created-at', 'to': 'CreatedAt', 'dataType': TimestampType(), 'personal': False, 'sensitive': True},
    {'from': 'updated-by', 'to': 'UpdatedBy', 'dataType': StringType(), 'personal': True, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'fullname', 'dataType': StringType()}]}},
    {'from': 'created-by', 'to': 'CreatedBy', 'dataType': StringType(), 'personal': True, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'fullname', 'dataType': StringType()}]}},
    {'from': 'updated-at', 'to': 'UpdatedAt', 'dataType': TimestampType(), 'personal': False, 'sensitive': True},
    {'from': 'currency', 'to': 'Currency', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'code', 'dataType': StringType()}]}},
    {'from': 'contract-type', 'to': 'ContractType', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
    {'from': 'no-of-renewals', 'to': 'NoOfRenewals', 'dataType': IntegerType(), 'personal': False, 'sensitive': True},
    {'from': 'auto-extend-end-date-for-renewal', 'to': 'AutoExtendEndDateForRenewal', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'contract-owner', 'to': 'ContractOwner', 'dataType': StringType(), 'personal': True, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'fullname', 'dataType': StringType()}]}},
    {'from': 'payment-term', 'to': 'PaymentTerm', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'nested': {'sub_fields': [{'name': 'code', 'dataType': StringType()}]}},
    {'from': 'term-type', 'to': 'TermType', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'terminated', 'to': 'Terminated', 'dataType': BooleanType(), 'personal': False, 'sensitive': True},
    {'from': 'use-order-windows', 'to': 'UseOrderWindows', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'parent', 'to': 'Parent', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'multi': True, 'sub_fields': [
        {'name': 'name', 'dataType': StringType(), 'personal': False, 'sensitive': True},
        {'name': 'id', 'dataType': StringType(), 'personal': False, 'sensitive': True}]}},
    {'from': 'published-date', 'to': 'PublishedDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'renewal-length-value', 'to': 'RenewalLengthValue', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
    {'from': 'shipping-term', 'to': 'ShippingTerm', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'code', 'dataType': StringType()}]}},
    {'from': 'savings-pct', 'to': 'SavingsPct', 'dataType': DecimalType(9, 2), 'personal': False, 'sensitive': True},
    {'from': 'supplier-account', 'to': 'SupplierAccount', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'stop-spend-based-on-max-value', 'to': 'StopSpendBasedOnMaxValue', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'submitter', 'to': 'Submitter', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'fullname', 'dataType': StringType()}]}},
    {'from': 'tags', 'to': 'Tags', 'dataType': ArrayType(StringType()), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
    {'from': 'termination-notice', 'to': 'TerminationNotice', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'order-window-tz', 'to': 'OrderWindowTz', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'used-for-buying', 'to': 'UsedForBuying', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'amended-contract-type', 'to': 'AmendedContractType', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'consent', 'to': 'Consent', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'current-approval', 'to': 'CurrentApproval', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'status', 'dataType': StringType()}]}},
    {'from': 'current-parallel-approvals', 'to': 'CurrentParallelApprovals', 'dataType': ArrayType(StringType()), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'status', 'dataType': StringType()}]}},
    {'from': 'default-account', 'to': 'DefaultAccount', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
    {'from': 'diversity-categories', 'to': 'DiversityCategories', 'dataType': ArrayType(StringType()), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
    {'from': 'execution-date', 'to': 'ExecutionDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'is-default', 'to': 'IsDefault', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'legal-agreement-url', 'to': 'LegalAgreementUrl', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'length-of-notice-unit', 'to': 'LengthOfNoticeUnit', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'length-of-notice-value', 'to': 'LengthOfNoticeValue', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'max-commit', 'to': 'MaxCommit', 'dataType': DecimalType(12, 2), 'personal': False, 'sensitive': True},
    {'from': 'maximum-value', 'to': 'MaximumValue', 'dataType': DecimalType(12, 2), 'personal': False, 'sensitive': True},
    {'from': 'minimum-value', 'to': 'MinimumValue', 'dataType': DecimalType(12, 2), 'personal': False, 'sensitive': True},
    {'from': 'po-message', 'to': 'PoMessage', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'preferred', 'to': 'Preferred', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'proxy-supplier-id', 'to': 'ProxySupplierId', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
    {'from': 'quote-response-id', 'to': 'QuoteResponseId', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
    {'from': 'reason-insight-events', 'to': 'ReasonInsightEvent', 'dataType': ArrayType(StringType()), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'eventable-type', 'dataType': StringType()}]}},
    {'from': 'renewal-length-unit', 'to': 'RenewalLengthUnit', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'requisition-message', 'to': 'RequisitionMessage', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'schedule', 'to': 'Schedule', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'multi': True, 'sub_fields': [
        {'name': 'day1', 'dataType': StringType(), 'personal': False, 'sensitive': False},
        {'name': 'day2', 'dataType': StringType(), 'personal': False, 'sensitive': False},
        {'name': 'day3', 'dataType': StringType(), 'personal': False, 'sensitive': False},
        {'name': 'day4', 'dataType': StringType(), 'personal': False, 'sensitive': False},
        {'name': 'day5', 'dataType': StringType(), 'personal': False, 'sensitive': False},
        {'name': 'day6', 'dataType': StringType(), 'personal': False, 'sensitive': False}]}},
    {'from': 'source-id', 'to': 'SourceId', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
    {'from': 'source-type', 'to': 'SourceType', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'strict-invoicing-rules', 'to': 'StrictInvoicingRules', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'supplier-invoiceable', 'to': 'SupplierInvoiceable', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'taggings', 'to': 'Taggings', 'dataType': ArrayType(StringType()), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'description', 'dataType': StringType()}]}},
    {'from': 'termination-notice-length-unit', 'to': 'TerminationNoticeLengthUnit', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'termination-notice-length-value', 'to': 'TerminationNoticeLengthValue', 'dataType': IntegerType(), 'personal': False, 'sensitive': True},
    {'from': 'terms', 'to': 'Terms', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'version', 'to': 'Version', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
    {'from': 'external-contract-id', 'to': 'ExternalContractId', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'fill-with-counterparty', 'to': 'FillWithCounterparty', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'whose-paper', 'to': 'WhosePaper', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'contract-clauses', 'to': 'ContractClauses', 'dataType': ArrayType(StringType()), 'personal': False, 'sensitive': True, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
    {'from': 'use-online-signing', 'to': 'UseOnlineSigning', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'contract-classification', 'to': 'ContractClassification', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
    {'from': 'source', 'to': 'Source', 'dataType': StringType(), 'personal': False, 'sensitive': False},
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### CONTRACTS_V2 Schema
# ---

# CELL ********************

schema_contracts_v2 = [
    {'from': 'id', 'to': 'Id', 'dataType': IntegerType(), 'personal': False, 'sensitive': True},
    {'from': 'number', 'to': 'Number', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'supplier', 'to': 'SupplierName', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
    {'from': 'name', 'to': 'Name', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'start-date', 'to': 'StartDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': True},
    {'from': 'end-date', 'to': 'EndDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': True},
    {'from': 'status', 'to': 'Status', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'min-commit', 'to': 'MinCommit', 'dataType': DecimalType(12, 2), 'personal': False, 'sensitive': True},
    {'from': 'description', 'to': 'Description', 'dataType': StringType(), 'personal': True, 'sensitive': True},
    {'from': 'custom-fields', 'to': 'CustomFields', 'dataType': StringType(), 'personal': True, 'sensitive': True, 'nested': {'multi': True, 'sub_fields': [
        {'name': 'next-review-date','dataType': TimestampType(), 'personal': False, 'sensitive': True},
        {'name': 'personal-data', 'dataType': StringType(), 'personal': False, 'sensitive': True},
        {'name': 'confidential-information',  'dataType': StringType(), 'personal': False, 'sensitive': True},
        {'name': 'internal-product',  'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
        {'name': 'legal-entity',  'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
        {'name': 'contract-approver',  'dataType': StringType(), 'personal': True, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'email', 'dataType': StringType()}]}},
        {'name': 'region-or-city',  'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
        {'name': 'systems-access--integration',  'dataType': StringType(), 'personal': False, 'sensitive': False}]}},
    {'from': 'department', 'to': 'Department', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
    {'from': 'type', 'to': 'Type', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'content-groups', 'to': 'ContentGroups', 'dataType': ArrayType(StringType()), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
    {'from': 'created-at', 'to': 'CreatedAt', 'dataType': TimestampType(), 'personal': False, 'sensitive': True},
    {'from': 'updated-by', 'to': 'UpdatedBy', 'dataType': StringType(), 'personal': True, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'fullname', 'dataType': StringType()}]}},
    {'from': 'created-by', 'to': 'CreatedBy', 'dataType': StringType(), 'personal': True, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'fullname', 'dataType': StringType()}]}},
    {'from': 'updated-at', 'to': 'UpdatedAt', 'dataType': TimestampType(), 'personal': False, 'sensitive': True},
    {'from': 'currency', 'to': 'Currency', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'code', 'dataType': StringType()}]}},
    {'from': 'contract-type', 'to': 'ContractType', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
    {'from': 'no-of-renewals', 'to': 'NoOfRenewals', 'dataType': IntegerType(), 'personal': False, 'sensitive': True},
    {'from': 'auto-extend-end-date-for-renewal', 'to': 'AutoExtendEndDateForRenewal', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'contract-owner', 'to': 'ContractOwner', 'dataType': StringType(), 'personal': True, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'fullname', 'dataType': StringType()}]}},
    {'from': 'payment-term', 'to': 'PaymentTerm', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'nested': {'sub_fields': [{'name': 'code', 'dataType': StringType()}]}},
    {'from': 'term-type', 'to': 'TermType', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'terminated', 'to': 'Terminated', 'dataType': BooleanType(), 'personal': False, 'sensitive': True},
    {'from': 'use-order-windows', 'to': 'UseOrderWindows', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'parent', 'to': 'Parent', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'multi': True, 'sub_fields': [
        {'name': 'name', 'dataType': StringType(), 'personal': False, 'sensitive': True},
        {'name': 'id', 'dataType': StringType(), 'personal': False, 'sensitive': True}]}},
    {'from': 'published-date', 'to': 'PublishedDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'renewal-length-value', 'to': 'RenewalLengthValue', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
    {'from': 'shipping-term', 'to': 'ShippingTerm', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'code', 'dataType': StringType()}]}},
    {'from': 'stop-spend-based-on-max-value', 'to': 'StopSpendBasedOnMaxValue', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'tags', 'to': 'Tags', 'dataType': ArrayType(StringType()), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
    {'from': 'order-window-tz', 'to': 'OrderWindowTz', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'used-for-buying', 'to': 'UsedForBuying', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'amended-contract-type', 'to': 'AmendedContractType', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'current-approval', 'to': 'CurrentApproval', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'status', 'dataType': StringType()}]}},
    {'from': 'current-parallel-approvals', 'to': 'CurrentParallelApprovals', 'dataType': ArrayType(StringType()), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'status', 'dataType': StringType()}]}},
    {'from': 'default-account', 'to': 'DefaultAccount', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
    {'from': 'diversity-categories', 'to': 'DiversityCategories', 'dataType': ArrayType(StringType()), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
    {'from': 'execution-date', 'to': 'ExecutionDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'is-default', 'to': 'IsDefault', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'legal-agreement-url', 'to': 'LegalAgreementUrl', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'length-of-notice-unit', 'to': 'LengthOfNoticeUnit', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'length-of-notice-value', 'to': 'LengthOfNoticeValue', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'max-commit', 'to': 'MaxCommit', 'dataType': DecimalType(12, 2), 'personal': False, 'sensitive': True},
    {'from': 'maximum-value', 'to': 'MaximumValue', 'dataType': DecimalType(12, 2), 'personal': False, 'sensitive': True},
    {'from': 'minimum-value', 'to': 'MinimumValue', 'dataType': DecimalType(12, 2), 'personal': False, 'sensitive': True},
    {'from': 'po-message', 'to': 'PoMessage', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'preferred', 'to': 'Preferred', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'proxy-supplier-id', 'to': 'ProxySupplierId', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
    {'from': 'quote-response-id', 'to': 'QuoteResponseId', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
    {'from': 'reason-insight-events', 'to': 'ReasonInsightEvent', 'dataType': ArrayType(StringType()), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'eventable-type', 'dataType': StringType()}]}},
    {'from': 'renewal-length-unit', 'to': 'RenewalLengthUnit', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'requisition-message', 'to': 'RequisitionMessage', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'schedule', 'to': 'Schedule', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'multi': True, 'sub_fields': [
        {'name': 'day1', 'dataType': StringType(), 'personal': False, 'sensitive': False},
        {'name': 'day2', 'dataType': StringType(), 'personal': False, 'sensitive': False},
        {'name': 'day3', 'dataType': StringType(), 'personal': False, 'sensitive': False},
        {'name': 'day4', 'dataType': StringType(), 'personal': False, 'sensitive': False},
        {'name': 'day5', 'dataType': StringType(), 'personal': False, 'sensitive': False},
        {'name': 'day6', 'dataType': StringType(), 'personal': False, 'sensitive': False}]}},
    {'from': 'source-id', 'to': 'SourceId', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
    {'from': 'source-type', 'to': 'SourceType', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'strict-invoicing-rules', 'to': 'StrictInvoicingRules', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'supplier-invoiceable', 'to': 'SupplierInvoiceable', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'taggings', 'to': 'Taggings', 'dataType': ArrayType(StringType()), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'description', 'dataType': StringType()}]}},
    {'from': 'termination-notice-length-unit', 'to': 'TerminationNoticeLengthUnit', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'version', 'to': 'Version', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
    {'from': 'external-contract-id', 'to': 'ExternalContractId', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'fill-with-counterparty', 'to': 'FillWithCounterparty', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'whose-paper', 'to': 'WhosePaper', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'use-online-signing', 'to': 'UseOnlineSigning', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'contract-classification', 'to': 'ContractClassification', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'nested': {'sub_fields': [{'name': 'name', 'dataType': StringType()}]}},
    {'from': 'source', 'to': 'Source', 'dataType': StringType(), 'personal': False, 'sensitive': False},
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
