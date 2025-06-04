# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# ##### SAP_HR_V1 Schema

# CELL ********************

schema_sap_employee_v1 = [
  {'from': 'EmpNumber', 'to': 'EmpNumber', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'CompanyCode', 'to': 'CompanyCode', 'dataType': StringType(), 'personal': False, 'sensitive': True},
  {'from': 'Position', 'to': 'Position', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'LastName', 'to': 'LastName', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'FirstName', 'to': 'FirstName', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'LeaveDate', 'to': 'LeaveDate', 'dataType': DateType(), 'personal': False, 'sensitive': False},
  {'from': 'HireDate', 'to': 'HireDate', 'dataType': DateType(), 'personal': False, 'sensitive': False},
  {'from': 'EmailAdd', 'to': 'EmailAdd', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'Upn', 'to': 'Upn', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'BusinessUnit', 'to': 'BusinessUnit', 'dataType': StringType(), 'personal': False, 'sensitive': True},
  {'from': 'BusinessGroup', 'to': 'BusinessGroup', 'dataType': StringType(), 'personal': False, 'sensitive': True},
  {'from': 'Division', 'to': 'Division', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'Location', 'to': 'Location', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'CostCentre', 'to': 'CostCentre', 'dataType': StringType(), 'personal': True, 'sensitive': False}
]


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
