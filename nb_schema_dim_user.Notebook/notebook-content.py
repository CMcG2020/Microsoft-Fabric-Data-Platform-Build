# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# ##### DIM_USER_V1 Schema

# CELL ********************

schema_dim_user_v1 = [
  {'field': 'UserKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'sap_employee': 'Upn', 'Employee': 'Attribute16', 'users': 'UserPrincipalName'}, 'calculated_field': True},
  {'field': 'UserPrincipalName', 'dataType': StringType(), 'personal': True, 'sensitive': False, 'from': {'sap_employee': 'Upn', 'Employee': 'Attribute16', 'users': 'UserPrincipalName'}},
  {'field': 'EmployeeNumber', 'dataType': StringType(), 'personal': True, 'sensitive': False, 'from': {'sap_employee': 'EmpNumber', 'Employee': 'EmployeeNumber'}},
  {'field': 'JobRole', 'dataType': StringType(), 'personal': True, 'sensitive': False, 'from': {'sap_employee': 'Position', 'Employee': 'Segment1'}},
  {'field': 'LastName', 'dataType': StringType(), 'personal': True, 'sensitive': False, 'from': {'sap_employee': 'LastName', 'Employee': 'LastName'}},
  {'field': 'FirstName', 'dataType': StringType(), 'personal': True, 'sensitive': False, 'from': {'sap_employee': 'FirstName', 'Employee': 'FirstName'}},
  {'field': 'EndDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'sap_employee': 'LeaveDate', 'Employee': 'ActualTerminationDate'}},
  {'field': 'StartDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'sap_employee': 'HireDate', 'Employee': 'DateStart'}},
  {'field': 'EmailAddress', 'dataType': StringType(), 'personal': True, 'sensitive': False, 'from': {'sap_employee': 'EmailAdd', 'Employee': 'EmailAddress'}},
  {'field': 'BusinessUnit', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'sap_employee': 'BusinessUnit', 'Employee': 'AssAttribute20'}},
  {'field': 'BusinessGroup', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'sap_employee': 'BusinessGroup', 'Employee': 'AssAttribute19'}},
  {'field': 'Division', 'dataType': StringType(), 'personal': True, 'sensitive': False, 'from': {'sap_employee': 'Division', 'Employee': 'AssAttribute18'}},
  {'field': 'OfficeLocation', 'dataType': StringType(), 'personal': True, 'sensitive': False, 'from': {'sap_employee': 'Location', 'Employee': 'LocationCode'}},
  {'field': 'CostCentre', 'dataType': StringType(), 'personal': True, 'sensitive': False, 'from': {'sap_employee': 'CostCentre', 'Employee': 'CostSegment1'}},
  {'field': 'CostCentre2', 'dataType': StringType(), 'personal': True, 'sensitive': False, 'from': {'Employee': 'CostSegment2'}},
  {'field': 'CompanyCode', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'sap_employee': 'CompanyCode'}},
  {'field': 'ManagerID', 'dataType': IntegerType(), 'personal': True, 'sensitive': False, 'from': {'Employee': 'SupervisorId'}},
  {'field': 'CountryCode', 'dataType': StringType(), 'personal': True, 'sensitive': False, 'from': {'Employee': 'Country'}},
  {'field': 'FullTimeEmployee', 'dataType': StringType(), 'personal': True, 'sensitive': False, 'from': {'Employee': 'CurrentEmployeeFlag'}},
  {'field': 'NonPayrollEmployee', 'dataType': StringType(), 'personal': True, 'sensitive': False, 'from': {'Employee': 'CurrentNPWFlag'}},
  {'field': 'EmployeeStatus', 'dataType': StringType(), 'personal': True, 'sensitive': False, 'from': {'Employee': 'UserStatus'}},
  {'field': 'DisplayName', 'dataType': StringType(), 'personal': True, 'sensitive': False, 'from': {'users': 'DisplayName'}},
  {'field': 'DeletedDateTime', 'dataType': TimestampType(), 'personal': True, 'sensitive': False, 'from': {'users': 'DeletedDateTime'}},
  {'field': 'ManagerUserPrincipalName', 'dataType': StringType(), 'personal': True, 'sensitive': False, 'from': {'Employee': 'Attribute16'}, 'calculated_field': True},
  {'field': 'EmployeeType', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'users': 'ExtensionAttribute10'}},
  {'field': 'AllocatedDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from':  {'sap_employee': 'AllocatedDate','users': 'AllocatedDate', 'Employee': 'AllocatedDate'}},
  {'field': 'SourceSystem', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from':  {'sap_employee': 'SourceSystem', 'users': 'SourceSystem', 'Employee': 'SourceSystem'}},
  {'field': 'PipelineUpdatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from':  {'sap_employee': 'PipelineUpdatedDate', 'users': 'PipelineUpdatedDate', 'Employee': 'PipelineUpdatedDate'}},
  {'field': 'TableName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from':  {'sap_employee': 'TableName','users': 'TableName', 'Employee': 'TableName'}},
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
