# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

schema_dim_service_v1 = [
    {'field': 'ChildServiceKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_rel_ci': 'Child'},'calculated_field': True},
    {'field': 'ChildService', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_rel_ci': 'Child'}},
    {'field': 'ParentService', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_rel_ci': 'Parent'}},
    {'field': 'Name', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'cmdb_ci_service': 'Name'}},
    {'field': 'Created', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_rel_ci': 'Created'}},
    {'field': 'BusinessCriticality', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'cmdb_ci_service': 'BusinessCriticality'}},
    {'field': 'ServiceClassification', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'cmdb_ci_service': 'ServiceClassification'}},
    {'field': 'OwnerGroup', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_service': 'OwnerGroup'}},
    {'field': 'UserGroupOwnerKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_service': 'OwnerGroup'},'calculated_field': True},
    {'field': 'Division', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_service': 'UDivision'}},
    {'field': 'SupportGroup', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_service': 'SupportGroup'}},
    {'field': 'UserGroupSupportKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_service': 'SupportGroup'}, 'calculated_field': True},
    {'field': 'IsActive', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_service': 'Active'}},
    {'field': 'Aliases', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_service': 'Aliases'}},
    {'field': 'IsVisibleInPortal', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_service': 'NotVisibleInPortal'}},
    {'field': 'ParentServiceShortDescription', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'cmdb_ci_service': 'ShortDescription'}},
    {'field': 'TechnicalGroup', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_service': 'TechnicalGroup'}},
    {'field': 'UserGroupTechnicalKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_service': 'TechnicalGroup'}, 'calculated_field': True},
    {'field': 'OperationalStatus', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'cmdb_ci_service': 'OperationalStatus'}},
    {'field': 'AllocatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_rel_ci':'AllocatedDate'}},
    {'field': 'SourceSystem', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_rel_ci': 'SourceSystem'}},
    {'field': 'PipelineUpdatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_rel_ci': 'PipelineUpdatedDate' }},
    {'field': 'TableName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_rel_ci': 'TableName'}}
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
