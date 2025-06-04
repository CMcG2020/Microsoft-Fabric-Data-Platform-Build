# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# ##### DIM_SUPPLIER_MAP_V1 Schema
# ---

# CELL ********************

schema_dim_supplier_map_v1 = [
  {'field': 'SupplierKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'suppliers': 'Name', 'Provider': 'Name', 'core_company': 'Name'}, 'calculated_field': True},
  {'field': 'SupplierMasterKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'suppliers': None, 'Provider': None, 'core_company': None}, 'calculated_field': True},
  {'field': 'IsMastered', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'suppliers': None, 'Provider': None, 'core_company': None}, 'calculated_field': True},
  {'field': 'MasteredBy', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'suppliers': None, 'Provider': None, 'core_company': None}, 'calculated_field': True},
  {'field': 'MasteredDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'suppliers': None, 'Provider': None, 'core_company': None}, 'calculated_field': True},
  {'field': 'ReceiptDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'suppliers': 'ReceiptDate', 'Provider': 'ReceiptDate', 'core_company': 'ReceiptDate'}},
  {'field': 'AllocatedDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'suppliers': 'AllocatedDate', 'Provider': 'AllocatedDate', 'core_company': 'AllocatedDate'}},
  {'field': 'SourceSystem', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'suppliers': 'SourceSystem', 'Provider': 'SourceSystem', 'core_company': 'SourceSystem'}},
  {'field': 'PipelineUpdatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'suppliers': 'PipelineUpdatedDate', 'Provider': 'PipelineUpdatedDate', 'core_company': 'PipelineUpdatedDate'}},
  {'field': 'TableName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'suppliers': 'TableName', 'Provider': 'TableName', 'core_company': 'TableName'}}
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
