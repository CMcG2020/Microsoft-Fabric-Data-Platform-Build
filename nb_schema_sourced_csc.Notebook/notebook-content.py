# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# ### CSC schema V1 
# - will be a one time upload as we are consolidating to a single registrar, Safenames

# CELL ********************

schema_push_csc_domain_name_v1 = [
    {'from': 'Domain Name', 'to': 'DomainName', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'Brand', 'to': 'Brand', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'Extension', 'to': 'Extension', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'Whois Status (GDPR)', 'to': 'WhoIsStatus', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'Country', 'to': 'Country', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'Registration Date', 'to': 'RegistrationDate', 'dataType': DateType(), 'personal': False, 'sensitive': True},
    {'from': 'Registry Expiry Date', 'to': 'RegistryExpiryDate', 'dataType': DateType(), 'personal': False, 'sensitive': True},
    {'from': 'Account Name', 'to': 'AccountName', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'Account Number', 'to': 'AccountNumber', 'dataType': IntegerType(), 'personal': False, 'sensitive': True},
    {'from': 'Business Unit', 'to': 'BusinessUnit', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'Status', 'to': 'Status', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'DNS Type', 'to': 'DNSType', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'CSC MultiLock On', 'to': 'CSCMultiLockOn', 'dataType': BooleanType(), 'personal': False, 'sensitive': True},
    {'from': 'MultiLock Effective Date', 'to': 'MultiLockEffectiveDate', 'dataType': DateType(), 'personal': False, 'sensitive': True},
    {'from': 'Vital Domain', 'to': 'VitalDomain', 'dataType': BooleanType(), 'personal': False, 'sensitive': True},
    {'from': 'Forwarding', 'to': 'Forwarding', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'Redirect Type', 'to': 'RedirectType', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'New GTLD', 'to': 'NewGTLD', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'Privacy Protection', 'to': 'PrivacyProtection', 'dataType': BooleanType(), 'personal': False, 'sensitive': True},
    {'from': 'Using CSC Agent', 'to': 'UsingCSCAgent', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'Reg First Name', 'to': 'RegFirstName', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Reg Last Name', 'to': 'RegLastName', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Reg Organization', 'to': 'RegOrganization', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'Reg Address', 'to': 'RegAddress', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Reg Address 2', 'to': 'RegAddress2', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Reg City', 'to': 'RegCity', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Reg State/Province', 'to': 'RegStateProvince', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Reg Postal Code', 'to': 'RegPostalCode', 'dataType': IntegerType(), 'personal': True, 'sensitive': False},
    {'from': 'Reg Country', 'to': 'RegCountry', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Reg Email', 'to': 'RegEmail', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Reg Phone', 'to': 'RegPhone', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Reg Fax', 'to': 'RegFax', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Admin First Name', 'to': 'AdminFirstName', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Admin Last Name', 'to': 'AdminLastName', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Admin Organization', 'to': 'AdminOrganization', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'Admin Address', 'to': 'AdminAddress', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Admin Address 2', 'to': 'AdminAddress2', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Admin City', 'to': 'AdminCity', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Admin State/Province', 'to': 'AdminStateProvince', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Admin Postal Code', 'to': 'AdminPostalCode', 'dataType': IntegerType(), 'personal': True, 'sensitive': False},
    {'from': 'Admin Country', 'to': 'AdminCountry', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Admin Email', 'to': 'AdminEmail', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Admin Phone', 'to': 'AdminPhone', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Admin Fax', 'to': 'AdminFax', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Tech First Name', 'to': 'TechFirstName', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Tech Last Name', 'to': 'TechLastName', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Tech Organization', 'to': 'TechOrganization', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'Tech Address', 'to': 'TechAddress', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Tech Address 2', 'to': 'TechAddress2', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Tech City', 'to': 'TechCity', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Tech State/Province', 'to': 'TechStateProvince', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Tech Postal Code', 'to': 'TechPostalCode', 'dataType': IntegerType(), 'personal': True, 'sensitive': False},
    {'from': 'Tech Country', 'to': 'TechCountry', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Tech Email', 'to': 'TechEmail', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Tech Phone', 'to': 'TechPhone', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Tech Fax', 'to': 'TechFax', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'IDN Translation', 'to': 'IDNTranslation', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'Local Language', 'to': 'LocalLanguage', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'Notes', 'to': 'Notes', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'Has DS Record', 'to': 'HasDSRecord', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'CSC DNSSEC Enabled', 'to': 'CSCDNSSECEnabled', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'DNS 1', 'to': 'DNS1', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'DNS 2', 'to': 'DNS2', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'DNS 3', 'to': 'DNS3', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'DNS 4', 'to': 'DNS4', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'DNS 5', 'to': 'DNS5', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'DNS 6', 'to': 'DNS6', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'DNS 7', 'to': 'DNS7', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'DNS 8', 'to': 'DNS8', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'DNS 9', 'to': 'DNS9', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'DNS 10', 'to': 'DNS10', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'DNS 11', 'to': 'DNS11', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'DNS 12', 'to': 'DNS12', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'DNS 13', 'to': 'DNS13', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'Billing Code', 'to': 'BillingCode', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'Primary Contact', 'to': 'PrimaryContact', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Primary Invoice Contact', 'to': 'PrimaryInvoiceContact', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Profit Center', 'to': 'ProfitCenter', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'Profit Center Description', 'to': 'ProfitCenterDescription', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'Purchase Order Number', 'to': 'PurchaseOrderNumber', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'Requestor', 'to': 'Requestor', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'Secondary Contact', 'to': 'SecondaryContact', 'dataType': StringType(), 'personal': True, 'sensitive': False},
]


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
