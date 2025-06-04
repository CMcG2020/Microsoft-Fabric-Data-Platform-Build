# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# ##### DIM_DATE_V1 Schema
# ---

# CELL ********************

schema_dim_date_v1 = [
    {'field': 'DateKey', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': None},
    {'field': 'Date', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': None},
    {'field': 'Day', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': None},
    {'field': 'Month', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': None},
    {'field': 'Year', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': None},
    {'field': 'DayOfWeek', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': None},
    {'field': 'Quarter', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': None},
    {'field': 'Half', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': None},
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
