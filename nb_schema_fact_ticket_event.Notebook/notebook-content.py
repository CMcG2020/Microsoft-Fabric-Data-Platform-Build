# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# ##### FACT_TICKET_EVENT_V1 Schema
# ---

# CELL ********************

schema_fact_ticket_event_v2 = [
    {'field': 'TicketKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'task_sla': 'task'}, 'calculated_field': True},
    {'field': 'TicketNumber', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'task_sla': 'task'}},
    {'field': 'CreatedDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'task_sla': 'SysCreatedOn'}},
    {'field': 'Stage', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'task_sla': 'stage'}},
    {'field': 'AssignmentGroup', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'task_sla': 'UInitialAssignmentGroup'}},
    {'field': 'AssignmentGroupKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'task_sla': 'UInitialAssignmentGroup'}, 'calculated_field': True},
    {'field': 'SupplierName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'task_sla': 'UInitialVendor'}},
    {'field': 'SupplierKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'task_sla': 'UInitialVendor'}, 'calculated_field': True},
    {'field': 'SupplierBreachedName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'task_sla': 'UBreachedWithVendor'}},
    {'field': 'SupplierBreachedNameKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'task_sla': 'UBreachedWithVendor'}, 'calculated_field': True},
    {'field': 'BusinessDuration', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'task_sla': 'BusinessDuration'}, 'calculated_field': True},
    {'field': 'EventType', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'task_sla': None}, 'calculated_field': True},
    {'field': 'SLAName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'task_sla': 'Sla'}},
    {'field': 'BreachedDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'task_sla': 'UBreachedOnDate'}},
    {'field': 'IsBreached', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'task_sla': 'HasBreached'}},
    {'field': 'StartDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'task_sla': 'StartTime'}},
    {'field': 'EndDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'task_sla': 'EndTime'}},
    {'field': 'ReceiptDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'task_sla': 'ReceiptDate'}},
    {'field': 'AllocatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'task_sla': 'AllocatedDate'}},
    {'field': 'SourceSystem', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'task_sla': 'SourceSystem'}},
    {'field': 'PipelineUpdatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'task_sla': 'ReceiptDate'}},
    {'field': 'TableName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'task_sla': 'TableName'}}
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
