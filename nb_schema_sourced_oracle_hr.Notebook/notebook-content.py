# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

schema_Employee_v1 = [
  {'from': 'attribute16', 'to': 'Attribute16', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'email_address', 'to': 'EmailAddress', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'first_name', 'to': 'FirstName', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'last_name', 'to': 'LastName', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'USER_STATUS', 'to': 'UserStatus', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'employee_number', 'to': 'EmployeeNumber', 'dataType': IntegerType(), 'personal': True, 'sensitive': False},
  {'from': 'current_employee_flag', 'to': 'CurrentEmployeeFlag', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'CURRENT_NPW_FLAG', 'to': 'CurrentNPWFlag', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'ass_attribute20', 'to': 'AssAttribute20', 'dataType': StringType(), 'personal': False, 'sensitive': True},
  {'from': 'ass_attribute18', 'to': 'AssAttribute18', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'supervisor_id', 'to': 'SupervisorId', 'dataType': IntegerType(), 'personal': True, 'sensitive': False},
  {'from': 'ass_attribute19', 'to': 'AssAttribute19', 'dataType': StringType(), 'personal': False, 'sensitive': True},
  {'from': 'location_code', 'to': 'LocationCode', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'country', 'to': 'Country', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'segment1', 'to': 'Segment1', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'cost_segment1', 'to': 'CostSegment1', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'cost_segment2', 'to': 'CostSegment2', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'date_start', 'to': 'DateStart', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
  {'from': 'ACTUAL_TERMINATION_DATE', 'to': 'ActualTerminationDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False}
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
