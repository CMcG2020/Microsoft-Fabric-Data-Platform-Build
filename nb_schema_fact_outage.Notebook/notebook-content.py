# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

schema_fact_outage_v1 = [
  {'field': 'OutageKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_outage': 'Number'}, 'calculated_field': True},
  {'field': 'TicketKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_outage': 'TaskNumber'}, 'calculated_field': True},
  {'field': 'ApplicationKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_outage': 'Application'}, 'calculated_field': True},
  {'field': 'ChildServiceKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_outage': 'CmdbCi'}, 'calculated_field': True},
  {'field': 'TicketOutageNumber', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_outage': 'Number'}},
  {'field': 'TicketRelatedNumber', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_outage': 'TaskNumber'}},
  {'field': 'OutageStartDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_outage': 'Begin'}},
  {'field': 'OutageEndDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_outage': 'End'}},
  {'field': 'OutageDuration', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_outage': 'Duration'}, 'calculated_field': True},
  {'field': 'CreatedDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_outage': 'Created'}},
  {'field': 'OutageStatus', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_outage': 'Status'}},
  {'field': 'AllocatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_outage': 'AllocatedDate'}},
  {'field': 'SourceSystem', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_outage': 'SourceSystem'}},
  {'field': 'PipelineUpdatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'cmdb_ci_outage': 'PipelineUpdatedDate'}},
]


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
