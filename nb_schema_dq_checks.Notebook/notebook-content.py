# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

dq_checks_v1 = [
    {'field': 'TableName', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'field': 'SourceSystem', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'field': 'CheckName', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'field': 'CheckLayer', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'field': 'CheckDescription', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'field': 'CheckOutcome', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'field': 'ScanDate', 'dataType': DateType(), 'personal': False, 'sensitive': False},
    {'field': 'ExecutionTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'field': 'AdditionalInfo', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'field': 'OnFailure', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'field': 'RecordCount', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
    {'field': 'CheckType', 'dataType': StringType(), 'personal': False, 'sensitive': False},
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
