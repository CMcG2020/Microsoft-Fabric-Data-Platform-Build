# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

schema_dim_domain_v1 = [
    {'field': 'DomainKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'push_csc_domain_name': 'DomainName'}, 'calculated_field': True},
    {'field': 'SourceSystem', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'push_csc_domain_name': 'SourceSystem'}, 'calculated_field': False},
    {'field': 'DomainName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'push_csc_domain_name': 'DomainName'}, 'calculated_field': False},
    {'field': 'Extension', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'push_csc_domain_name': 'Extension'}, 'calculated_field': False},
    {'field': 'Country', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'push_csc_domain_name': 'Country'}, 'calculated_field': False},
    {'field': 'RegistrationDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'push_csc_domain_name': 'RegistrationDate'}, 'calculated_field': False},
    {'field': 'RegistryExpiryDate', 'dataType': DateType(), 'personal': False, 'sensitive': True, 'from': {'push_csc_domain_name': 'RegistryExpiryDate'}, 'calculated_field': False},
    {'field': 'AccountName', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'push_csc_domain_name': 'AccountName'}, 'calculated_field': False},
    {'field': 'RegistrantKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'push_csc_domain_name': ['RegFirstName', 'RegLastName']}, 'calculated_field': True},
    {'field': 'BusinessUnit', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'push_csc_domain_name': 'BusinessUnit'}, 'calculated_field': False},
    {'field': 'AllocatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'push_csc_domain_name': 'AllocatedDate'}},
    {'field': 'PipelineUpdatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'push_csc_domain_name': 'PipelineUpdatedDate'}},
    {'field': 'TableName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'push_csc_domain_name': 'TableName'}}
]


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
