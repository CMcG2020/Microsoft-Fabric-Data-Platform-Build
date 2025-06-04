# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse_name": "",
# META       "default_lakehouse_workspace_id": ""
# META     }
# META   }
# META }

# MARKDOWN ********************

# ##### DIM_TICKET_V1 Schema
# ---

# CELL ********************

schema_dim_ticket_v1 = [
    {'field': 'BusinessSponsorKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UBusinessSponsor', 'u_inf_generic_request': 'UBusinessSponsor', 'sc_req_item': 'UBusinessSponsor', 'sc_task': 'UBusinessSponsor'}, 'calculated_field': True},
    {'field': 'RequestedForKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'u_inf_generic_request': 'URequestedFor', 'sc_req_item': 'RequestedFor'}, 'calculated_field': True},
    {'field': 'UserAssignedKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'AssignedTo', 'u_inf_generic_request': 'AssignedTo', 'sc_req_item': 'AssignedTo', 'sc_task': 'AssignedTo'}, 'calculated_field': True},
    {'field': 'UserClosedKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ClosedBy', 'u_inf_generic_request': 'ClosedBy', 'sc_req_item': 'ClosedBy', 'sc_task': 'ClosedBy'}, 'calculated_field': True},
    {'field': 'UserRaisedKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'OpenedBy', 'u_inf_generic_request': 'OpenedBy', 'sc_req_item': 'OpenedBy', 'sc_task': 'OpenedBy'}, 'calculated_field': True},
    {'field': 'UserResolvedKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ResolvedBy', 'u_inf_generic_request': 'UResolvedBy'}, 'calculated_field': True},
    {'field': 'CustomerKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UCustomer', 'u_inf_generic_request': 'UCustomer', 'sc_req_item': 'UCustomer', 'sc_task': 'UCustomer'}, 'calculated_field': True},
    {'field': 'SupplierKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'Vendor', 'u_inf_generic_request': 'UVendor'}, 'calculated_field': True},
    {'field': 'ChildServiceKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UService', 'u_inf_generic_request': 'UService', 'sc_req_item': 'UService', 'sc_task': 'UService'}, 'calculated_field': True},
    {'field': 'UserAssignmentGroupKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'AssignmentGroup', 'u_inf_generic_request': 'AssignmentGroup', 'sc_req_item': 'AssignmentGroup', 'sc_task': 'AssignmentGroup'}, 'calculated_field': True},
    {'field': 'TicketKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'Number', 'u_inf_generic_request': 'Number', 'sc_req_item': 'Number', 'sc_task': 'Number'}, 'calculated_field': True},
    {'field': 'ApplicationKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UApplication', 'u_inf_generic_request': 'UApplication', 'sc_req_item': 'UApplication', 'sc_task': 'UApplication'}, 'calculated_field': True},
    {'field': 'TicketNumber', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'Number', 'u_inf_generic_request': 'Number', 'sc_req_item': 'Number', 'sc_task': 'Number'}},
    {'field': 'IsActive', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'Active', 'u_inf_generic_request': 'Active', 'sc_req_item': 'Active', 'sc_task': 'Active'}},
    {'field': 'Priority', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'Priority', 'u_inf_generic_request': 'Priority', 'sc_req_item': 'Priority', 'sc_task': 'Priority'}},
    {'field': 'TicketStatePrimary', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UInfTaskState', 'u_inf_generic_request': 'UInfTaskState', 'sc_req_item': 'UInfTaskState', 'sc_task': 'UInfTaskState'}},
    {'field': 'TicketStateSecondary', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'State', 'u_inf_generic_request': 'State', 'sc_req_item': 'State', 'sc_task': 'State'}},
    {'field': 'AssignmentGroup', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'AssignmentGroup', 'u_inf_generic_request': 'AssignmentGroup', 'sc_req_item': 'AssignmentGroup', 'sc_task': 'AssignmentGroup'}},
    {'field': 'SysCreatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'SysCreatedOn', 'u_inf_generic_request': 'SysCreatedOn', 'sc_req_item': 'SysCreatedOn', 'sc_task': 'SysCreatedOn'}},
    {'field': 'SysUpdatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'SysUpdatedOn', 'u_inf_generic_request': 'SysUpdatedOn', 'sc_req_item': 'SysUpdatedOn', 'sc_task': 'SysUpdatedOn'}},
    {'field': 'SysModCount', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'SysModCount', 'u_inf_generic_request': 'SysModCount', 'sc_req_item': 'SysModCount', 'sc_task': 'SysModCount'}},
    {'field': 'Urgency', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'incident': 'Urgency', 'u_inf_generic_request': 'Urgency', 'sc_req_item': 'Urgency', 'sc_task': 'Urgency'}},
    {'field': 'IsSupplierRelated', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UVendorRelated', 'u_inf_generic_request': 'UVendorRelated'}},
    {'field': 'IsSLAResolvedMet', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'MadeSla', 'u_inf_generic_request': 'MadeSla', 'sc_req_item': 'MadeSla', 'sc_task': 'MadeSla'}},
    {'field': 'HoldCount', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UOnHoldCounter', 'u_inf_generic_request': 'UOnHoldCounter', 'sc_req_item': 'UOnHoldCounter', 'sc_task': 'UOnHoldCounter'}},
    {'field': 'ProjectNumber', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UProject', 'u_inf_generic_request': 'UProject', 'sc_req_item': 'UProject', 'sc_task': 'UProject'}},
    {'field': 'ProjectId', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'XBateTransportEProjectId', 'u_inf_generic_request': 'XBateTransportEProjectId', 'sc_req_item': 'XBateTransportEProjectId', 'sc_task': 'XBateTransportEProjectId'}},
    {'field': 'ProjectName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UProjectName', 'u_inf_generic_request': 'UProjectName', 'sc_req_item': 'UProjectName', 'sc_task': 'UProjectName'}},
    {'field': 'Quantity', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'u_inf_generic_request': 'Quantity', 'sc_req_item': 'Quantity'}},
    {'field': 'ResolvedAt', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ResolvedAt', 'u_inf_generic_request': 'UResolvedAt'}},
    {'field': 'TicketType', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'SysClassName', 'u_inf_generic_request': 'SysClassName', 'sc_req_item': 'SysClassName', 'sc_task': 'SysClassName'}},
    {'field': 'UponApprovalAction', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UponApproval', 'u_inf_generic_request': 'UponApproval', 'sc_req_item': 'UponApproval', 'sc_task': 'UponApproval'}},
    {'field': 'UponRejectionAction', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UponReject', 'u_inf_generic_request': 'UponReject', 'sc_req_item': 'UponReject', 'sc_task': 'UponReject'}},
    {'field': 'SupplierThirdPartyTicket', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'VendorTicket', 'u_inf_generic_request': 'UVendorTicket'}},
    {'field': 'ThirdPartyReferenceName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UThirdPartyReference', 'sc_req_item': 'UExternalReference'}},
    {'field': 'RequestForChangeTicketID', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'Rfc'}},
    {'field': 'ChildIncidentCount', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ChildIncidents'}},
    {'field': 'IncidentState', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'incident': 'IncidentState'}},
    {'field': 'ReOpenedTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ReopenedTime'}},
    {'field': 'NotificationPreference', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'Notify'}},
    {'field': 'ProblemTicketId', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ProblemId'}},
    {'field': 'PromotedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'PromotedOn'}},
    {'field': 'ReOpenCount', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ReopenCount'}},
    {'field': 'AssociatedGenericRequestNumber', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'URequest', 'u_inf_generic_request': 'Request', 'sc_req_item': 'Request', 'sc_task': 'Request'}},
    {'field': 'Severity', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'incident': 'Severity'}},
    {'field': 'WorkEnd', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'sc_req_item': 'WorkEnd', 'sc_task': 'WorkEnd'}},
    {'field': 'WorkStart', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'sc_req_item': 'WorkStart', 'sc_task': 'WorkStart'}},
    {'field': 'AssociatedTaskNumber', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'TaskEffectiveNumber', 'u_inf_generic_request': 'TaskEffectiveNumber', 'sc_req_item': 'TaskEffectiveNumber', 'sc_task': 'TaskEffectiveNumber'}},
    {'field': 'ExpectedStart', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ExpectedStart', 'u_inf_generic_request': 'ExpectedStart', 'sc_req_item': 'ExpectedStart', 'sc_task': 'ExpectedStart'}},
    {'field': 'CatalogueItem', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'sc_req_item': 'CatItem', 'sc_task': 'CatItem'}},
    {'field': 'PendingStatusReason', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'sc_task': 'UPendingReason'}},
    {'field': 'CallBackType', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UCallBackType'}},
    {'field': 'ConfigurationItem', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'incident': 'CmdbCi', 'u_inf_generic_request': 'CmdbCi', 'sc_task': 'CmdbCi'}},
    {'field': 'BusinessDuration', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'BusinessDuration', 'u_inf_generic_request': 'BusinessDuration', 'sc_req_item': 'BusinessDuration', 'sc_task': 'BusinessDuration'}},
    {'field': 'OpenedDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'OpenedAt', 'u_inf_generic_request': 'OpenedAt', 'sc_req_item': 'OpenedAt', 'sc_task': 'OpenedAt'}},
    {'field': 'ParentTicketNumber', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'Parent', 'u_inf_generic_request': 'Parent', 'sc_req_item': 'Parent', 'sc_task': 'Parent'}},
    {'field': 'DueDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'DueDate', 'u_inf_generic_request': 'DueDate', 'sc_req_item': 'DueDate', 'sc_task': 'DueDate'}},
    {'field': 'SLAResolutionDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'SlaDue', 'u_inf_generic_request': 'SlaDue', 'sc_req_item': 'SlaDue', 'sc_task': 'SlaDue'}},
    {'field': 'IsSLAExempt', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'USlaExempt', 'u_inf_generic_request': 'USlaExempt', 'sc_req_item': 'USlaExempt', 'sc_task': 'USlaExempt'}},
    {'field': 'ChildService', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UService', 'u_inf_generic_request': 'UService', 'sc_req_item': 'UService', 'sc_task': 'UService'}},
    {'field': 'IsShouldHaveBeenResolvedAtServiceDesk', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UShouldHaveBeenResolvedAtServiceDesk', 'u_inf_generic_request': 'UShouldHaveBeenResolvedAtServiceDesk', 'sc_task': 'UShouldHaveBeenResolvedAtServiceDesk'}},
    {'field': 'MajorIncidentGrade', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'incident': 'UMajorIncidentGrade'}},
    {'field': 'IsMajorIncident', 'dataType': BooleanType(), 'personal': False, 'sensitive': True, 'from': {'incident': 'UMajorIncident'}},
    {'field': 'MajorIncidentState', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'incident': 'MajorIncidentState'}},
    {'field': 'IsAnEnhancement', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UEnhancement', 'u_inf_generic_request': 'UEnhancement', 'sc_task': 'UEnhancement'}},
    {'field': 'ReceiptDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ReceiptDate', 'u_inf_generic_request': 'ReceiptDate', 'sc_req_item': 'ReceiptDate', 'sc_task': 'ReceiptDate'}},
    {'field': 'AllocatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'AllocatedDate', 'u_inf_generic_request': 'AllocatedDate', 'sc_req_item': 'AllocatedDate', 'sc_task': 'AllocatedDate'}},
    {'field': 'SourceSystem', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'SourceSystem', 'u_inf_generic_request': 'SourceSystem', 'sc_req_item': 'SourceSystem', 'sc_task': 'SourceSystem'}},
    {'field': 'PipelineUpdatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'PipelineUpdatedDate', 'u_inf_generic_request': 'PipelineUpdatedDate', 'sc_req_item': 'PipelineUpdatedDate', 'sc_task': 'PipelineUpdatedDate'}},
    {'field': 'TableName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'TableName', 'u_inf_generic_request': 'TableName', 'sc_req_item': 'TableName', 'sc_task': 'TableName'}}
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

schema_dim_ticket_v2 = [
    {'field': 'BusinessSponsorKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UBusinessSponsor', 'u_inf_generic_request': 'UBusinessSponsor', 'sc_req_item': 'UBusinessSponsor', 'sc_task': 'UBusinessSponsor'}, 'calculated_field': True},
    {'field': 'RequestedForKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'u_inf_generic_request': 'URequestedFor', 'sc_req_item': 'RequestedFor'}, 'calculated_field': True},
    {'field': 'UserAssignedKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'AssignedTo', 'u_inf_generic_request': 'AssignedTo', 'sc_req_item': 'AssignedTo', 'sc_task': 'AssignedTo'}, 'calculated_field': True},
    {'field': 'UserClosedKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ClosedBy', 'u_inf_generic_request': 'ClosedBy', 'sc_req_item': 'ClosedBy', 'sc_task': 'ClosedBy'}, 'calculated_field': True},
    {'field': 'UserRaisedKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'OpenedBy', 'u_inf_generic_request': 'OpenedBy', 'sc_req_item': 'OpenedBy', 'sc_task': 'OpenedBy'}, 'calculated_field': True},
    {'field': 'UserResolvedKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ResolvedBy', 'u_inf_generic_request': 'UResolvedBy'}, 'calculated_field': True},
    {'field': 'CustomerKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UCustomer', 'u_inf_generic_request': 'UCustomer', 'sc_req_item': 'UCustomer', 'sc_task': 'UCustomer'}, 'calculated_field': True},
    {'field': 'SupplierKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'Vendor', 'u_inf_generic_request': 'UVendor'}, 'calculated_field': True},
    {'field': 'ChildServiceKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UService', 'u_inf_generic_request': 'UService', 'sc_req_item': 'UService', 'sc_task': 'UService'}, 'calculated_field': True},
    {'field': 'UserAssignmentGroupKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'AssignmentGroup', 'u_inf_generic_request': 'AssignmentGroup', 'sc_req_item': 'AssignmentGroup', 'sc_task': 'AssignmentGroup'}, 'calculated_field': True},
    {'field': 'TicketKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'Number', 'u_inf_generic_request': 'Number', 'sc_req_item': 'Number', 'sc_task': 'Number'}, 'calculated_field': True},
    {'field': 'ApplicationKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UApplication', 'u_inf_generic_request': 'UApplication', 'sc_req_item': 'UApplication', 'sc_task': 'UApplication'}, 'calculated_field': True},
    {'field': 'TicketNumber', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'Number', 'u_inf_generic_request': 'Number', 'sc_req_item': 'Number', 'sc_task': 'Number'}},
    {'field': 'IsActive', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'Active', 'u_inf_generic_request': 'Active', 'sc_req_item': 'Active', 'sc_task': 'Active'}},
    {'field': 'Priority', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'Priority', 'u_inf_generic_request': 'Priority', 'sc_req_item': 'Priority', 'sc_task': 'Priority'}},
    {'field': 'TicketStatePrimary', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UInfTaskState', 'u_inf_generic_request': 'UInfTaskState', 'sc_req_item': 'UInfTaskState', 'sc_task': 'UInfTaskState'}},
    {'field': 'TicketStateSecondary', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'State', 'u_inf_generic_request': 'State', 'sc_req_item': 'State', 'sc_task': 'State'}},
    {'field': 'AssignmentGroup', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'AssignmentGroup', 'u_inf_generic_request': 'AssignmentGroup', 'sc_req_item': 'AssignmentGroup', 'sc_task': 'AssignmentGroup'}},
    {'field': 'SysCreatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'SysCreatedOn', 'u_inf_generic_request': 'SysCreatedOn', 'sc_req_item': 'SysCreatedOn', 'sc_task': 'SysCreatedOn'}},
    {'field': 'SysUpdatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'SysUpdatedOn', 'u_inf_generic_request': 'SysUpdatedOn', 'sc_req_item': 'SysUpdatedOn', 'sc_task': 'SysUpdatedOn'}},
    {'field': 'SysModCount', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'SysModCount', 'u_inf_generic_request': 'SysModCount', 'sc_req_item': 'SysModCount', 'sc_task': 'SysModCount'}},
    {'field': 'Urgency', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'incident': 'Urgency', 'u_inf_generic_request': 'Urgency', 'sc_req_item': 'Urgency', 'sc_task': 'Urgency'}},
    {'field': 'IsSupplierRelated', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UVendorRelated', 'u_inf_generic_request': 'UVendorRelated'}},
    {'field': 'IsSLAResolvedMet', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'MadeSla', 'u_inf_generic_request': 'MadeSla', 'sc_req_item': 'MadeSla', 'sc_task': 'MadeSla'}},
    {'field': 'HoldCount', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UOnHoldCounter', 'u_inf_generic_request': 'UOnHoldCounter', 'sc_req_item': 'UOnHoldCounter', 'sc_task': 'UOnHoldCounter'}},
    {'field': 'ProjectNumber', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UProject', 'u_inf_generic_request': 'UProject', 'sc_req_item': 'UProject', 'sc_task': 'UProject'}},
    {'field': 'ProjectId', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'XBateTransportEProjectId', 'u_inf_generic_request': 'XBateTransportEProjectId', 'sc_req_item': 'XBateTransportEProjectId', 'sc_task': 'XBateTransportEProjectId'}},
    {'field': 'ProjectName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UProjectName', 'u_inf_generic_request': 'UProjectName', 'sc_req_item': 'UProjectName', 'sc_task': 'UProjectName'}},
    {'field': 'Quantity', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'u_inf_generic_request': 'Quantity', 'sc_req_item': 'Quantity'}},
    {'field': 'ResolvedAt', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ResolvedAt', 'u_inf_generic_request': 'UResolvedAt'}},
    {'field': 'ClosedAt', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ClosedAt', 'u_inf_generic_request': 'ClosedAt', 'sc_req_item': 'ClosedAt', 'sc_task': 'ClosedAt'}},
    {'field': 'TicketType', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'SysClassName', 'u_inf_generic_request': 'SysClassName', 'sc_req_item': 'SysClassName', 'sc_task': 'SysClassName'}},
    {'field': 'UponApprovalAction', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UponApproval', 'u_inf_generic_request': 'UponApproval', 'sc_req_item': 'UponApproval', 'sc_task': 'UponApproval'}},
    {'field': 'UponRejectionAction', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UponReject', 'u_inf_generic_request': 'UponReject', 'sc_req_item': 'UponReject', 'sc_task': 'UponReject'}},
    {'field': 'SupplierThirdPartyTicket', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'VendorTicket', 'u_inf_generic_request': 'UVendorTicket'}},
    {'field': 'ThirdPartyReferenceName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UThirdPartyReference', 'sc_req_item': 'UExternalReference'}},
    {'field': 'RequestForChangeTicketID', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'Rfc'}},
    {'field': 'ChildIncidentCount', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ChildIncidents'}},
    {'field': 'IncidentState', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'incident': 'IncidentState'}},
    {'field': 'ReOpenedTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ReopenedTime'}},
    {'field': 'NotificationPreference', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'Notify'}},
    {'field': 'ProblemTicketId', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ProblemId'}},
    {'field': 'PromotedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'PromotedOn'}},
    {'field': 'ReOpenCount', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ReopenCount'}},
    {'field': 'AssociatedGenericRequestNumber', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'URequest', 'u_inf_generic_request': 'Request', 'sc_req_item': 'Request', 'sc_task': 'Request'}},
    {'field': 'Severity', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'incident': 'Severity'}},
    {'field': 'WorkEnd', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'sc_req_item': 'WorkEnd', 'sc_task': 'WorkEnd'}},
    {'field': 'WorkStart', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'sc_req_item': 'WorkStart', 'sc_task': 'WorkStart'}},
    {'field': 'AssociatedTaskNumber', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'TaskEffectiveNumber', 'u_inf_generic_request': 'TaskEffectiveNumber', 'sc_req_item': 'TaskEffectiveNumber', 'sc_task': 'TaskEffectiveNumber'}},
    {'field': 'ExpectedStart', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ExpectedStart', 'u_inf_generic_request': 'ExpectedStart', 'sc_req_item': 'ExpectedStart', 'sc_task': 'ExpectedStart'}},
    {'field': 'CatalogueItem', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'sc_req_item': 'CatItem', 'sc_task': 'CatItem'}},
    {'field': 'PendingStatusReason', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'sc_task': 'UPendingReason'}},
    {'field': 'CallBackType', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UCallBackType'}},
    {'field': 'ConfigurationItem', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'incident': 'CmdbCi', 'u_inf_generic_request': 'CmdbCi', 'sc_task': 'CmdbCi'}},
    {'field': 'BusinessDuration', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'BusinessDuration', 'u_inf_generic_request': 'BusinessDuration', 'sc_req_item': 'BusinessDuration', 'sc_task': 'BusinessDuration'}},
    {'field': 'OpenedDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'OpenedAt', 'u_inf_generic_request': 'OpenedAt', 'sc_req_item': 'OpenedAt', 'sc_task': 'OpenedAt'}},
    {'field': 'ParentTicketNumber', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'Parent', 'u_inf_generic_request': 'Parent', 'sc_req_item': 'Parent', 'sc_task': 'Parent'}},
    {'field': 'DueDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'DueDate', 'u_inf_generic_request': 'DueDate', 'sc_req_item': 'DueDate', 'sc_task': 'DueDate'}},
    {'field': 'SLAResolutionDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'SlaDue', 'u_inf_generic_request': 'SlaDue', 'sc_req_item': 'SlaDue', 'sc_task': 'SlaDue'}},
    {'field': 'IsSLAExempt', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'USlaExempt', 'u_inf_generic_request': 'USlaExempt', 'sc_req_item': 'USlaExempt', 'sc_task': 'USlaExempt'}},
    {'field': 'ChildService', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UService', 'u_inf_generic_request': 'UService', 'sc_req_item': 'UService', 'sc_task': 'UService'}},
    {'field': 'IsShouldHaveBeenResolvedAtServiceDesk', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UShouldHaveBeenResolvedAtServiceDesk', 'u_inf_generic_request': 'UShouldHaveBeenResolvedAtServiceDesk', 'sc_task': 'UShouldHaveBeenResolvedAtServiceDesk'}},
    {'field': 'MajorIncidentGrade', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'incident': 'UMajorIncidentGrade'}},
    {'field': 'IsMajorIncident', 'dataType': BooleanType(), 'personal': False, 'sensitive': True, 'from': {'incident': 'UMajorIncident'}},
    {'field': 'MajorIncidentState', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'incident': 'MajorIncidentState'}},
    {'field': 'CsatCompletedDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'asmt_assessment_instance':['TakenOn', 'TaskId', 'Number']}, 'calculated_field': True},
    {'field': 'CsatScore', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'asmt_assessment_instance_question': ['Value', 'Instance', 'Category']}, 'calculated_field': True},
    {'field': 'IsAnEnhancement', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UEnhancement', 'u_inf_generic_request': 'UEnhancement', 'sc_task': 'UEnhancement'}},
    {'field': 'ReceiptDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ReceiptDate', 'u_inf_generic_request': 'ReceiptDate', 'sc_req_item': 'ReceiptDate', 'sc_task': 'ReceiptDate'}},
    {'field': 'AllocatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'AllocatedDate', 'u_inf_generic_request': 'AllocatedDate', 'sc_req_item': 'AllocatedDate', 'sc_task': 'AllocatedDate'}},
    {'field': 'SourceSystem', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'SourceSystem', 'u_inf_generic_request': 'SourceSystem', 'sc_req_item': 'SourceSystem', 'sc_task': 'SourceSystem'}},
    {'field': 'PipelineUpdatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'PipelineUpdatedDate', 'u_inf_generic_request': 'PipelineUpdatedDate', 'sc_req_item': 'PipelineUpdatedDate', 'sc_task': 'PipelineUpdatedDate'}},
    {'field': 'TableName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'TableName', 'u_inf_generic_request': 'TableName', 'sc_req_item': 'TableName', 'sc_task': 'TableName'}}
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

schema_dim_ticket_v3 = [
    {'field': 'BusinessSponsorKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UBusinessSponsor', 'u_inf_generic_request': 'UBusinessSponsor', 'sc_req_item': 'UBusinessSponsor', 'sc_task': 'UBusinessSponsor'}, 'calculated_field': True},
    {'field': 'RequestedForKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'u_inf_generic_request': 'URequestedFor', 'sc_req_item': 'RequestedFor'}, 'calculated_field': True},
    {'field': 'UserAssignedKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'AssignedTo', 'u_inf_generic_request': 'AssignedTo', 'sc_req_item': 'AssignedTo', 'sc_task': 'AssignedTo'}, 'calculated_field': True},
    {'field': 'UserClosedKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ClosedBy', 'u_inf_generic_request': 'ClosedBy', 'sc_req_item': 'ClosedBy', 'sc_task': 'ClosedBy'}, 'calculated_field': True},
    {'field': 'UserRaisedKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'OpenedBy', 'u_inf_generic_request': 'OpenedBy', 'sc_req_item': 'OpenedBy', 'sc_task': 'OpenedBy'}, 'calculated_field': True},
    {'field': 'UserResolvedKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ResolvedBy', 'u_inf_generic_request': 'UResolvedBy'}, 'calculated_field': True},
    {'field': 'CustomerKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UCustomer', 'u_inf_generic_request': 'UCustomer', 'sc_req_item': 'UCustomer', 'sc_task': 'UCustomer'}, 'calculated_field': True},
    {'field': 'CustomerName', 'dataType': StringType(), 'personal': True, 'sensitive': False, 'from': {'incident': 'UCustomer', 'u_inf_generic_request': 'UCustomer', 'sc_req_item': 'UCustomer', 'sc_task': 'UCustomer'}, 'calculated_field': True},
    {'field': 'SupplierKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'Vendor', 'u_inf_generic_request': 'UVendor'}, 'calculated_field': True},
    {'field': 'ChildServiceKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UService', 'u_inf_generic_request': 'UService', 'sc_req_item': 'UService', 'sc_task': 'UService'}, 'calculated_field': True},
    {'field': 'UserAssignmentGroupKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'AssignmentGroup', 'u_inf_generic_request': 'AssignmentGroup', 'sc_req_item': 'AssignmentGroup', 'sc_task': 'AssignmentGroup'}, 'calculated_field': True},
    {'field': 'TicketKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'Number', 'u_inf_generic_request': 'Number', 'sc_req_item': 'Number', 'sc_task': 'Number'}, 'calculated_field': True},
    {'field': 'ApplicationKey', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UApplication', 'u_inf_generic_request': 'UApplication', 'sc_req_item': 'UApplication', 'sc_task': 'UApplication'}, 'calculated_field': True},
    {'field': 'TicketNumber', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'Number', 'u_inf_generic_request': 'Number', 'sc_req_item': 'Number', 'sc_task': 'Number'}},
    {'field': 'IsActive', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'Active', 'u_inf_generic_request': 'Active', 'sc_req_item': 'Active', 'sc_task': 'Active'}},
    {'field': 'Priority', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'Priority', 'u_inf_generic_request': 'Priority', 'sc_req_item': 'Priority', 'sc_task': 'Priority'}},
    {'field': 'TicketStatePrimary', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UInfTaskState', 'u_inf_generic_request': 'UInfTaskState', 'sc_req_item': 'UInfTaskState', 'sc_task': 'UInfTaskState'}},
    {'field': 'TicketStateSecondary', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'State', 'u_inf_generic_request': 'State', 'sc_req_item': 'State', 'sc_task': 'State'}},
    {'field': 'AssignmentGroup', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'AssignmentGroup', 'u_inf_generic_request': 'AssignmentGroup', 'sc_req_item': 'AssignmentGroup', 'sc_task': 'AssignmentGroup'}},
    {'field': 'SysCreatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'SysCreatedOn', 'u_inf_generic_request': 'SysCreatedOn', 'sc_req_item': 'SysCreatedOn', 'sc_task': 'SysCreatedOn'}},
    {'field': 'SysUpdatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'SysUpdatedOn', 'u_inf_generic_request': 'SysUpdatedOn', 'sc_req_item': 'SysUpdatedOn', 'sc_task': 'SysUpdatedOn'}},
    {'field': 'SysModCount', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'SysModCount', 'u_inf_generic_request': 'SysModCount', 'sc_req_item': 'SysModCount', 'sc_task': 'SysModCount'}},
    {'field': 'Urgency', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'incident': 'Urgency', 'u_inf_generic_request': 'Urgency', 'sc_req_item': 'Urgency', 'sc_task': 'Urgency'}},
    {'field': 'IsSupplierRelated', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UVendorRelated', 'u_inf_generic_request': 'UVendorRelated'}},
    {'field': 'IsSLAResolvedMet', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'MadeSla', 'u_inf_generic_request': 'MadeSla', 'sc_req_item': 'MadeSla', 'sc_task': 'MadeSla'}},
    {'field': 'HoldCount', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UOnHoldCounter', 'u_inf_generic_request': 'UOnHoldCounter', 'sc_req_item': 'UOnHoldCounter', 'sc_task': 'UOnHoldCounter'}},
    {'field': 'ProjectNumber', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UProject', 'u_inf_generic_request': 'UProject', 'sc_req_item': 'UProject', 'sc_task': 'UProject'}},
    {'field': 'ProjectId', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'XBateTransportEProjectId', 'u_inf_generic_request': 'XBateTransportEProjectId', 'sc_req_item': 'XBateTransportEProjectId', 'sc_task': 'XBateTransportEProjectId'}},
    {'field': 'ProjectName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UProjectName', 'u_inf_generic_request': 'UProjectName', 'sc_req_item': 'UProjectName', 'sc_task': 'UProjectName'}},
    {'field': 'Quantity', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'u_inf_generic_request': 'Quantity', 'sc_req_item': 'Quantity'}},
    {'field': 'ResolvedAt', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ResolvedAt', 'u_inf_generic_request': 'UResolvedAt'}},
    {'field': 'ClosedAt', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ClosedAt', 'u_inf_generic_request': 'ClosedAt', 'sc_req_item': 'ClosedAt', 'sc_task': 'ClosedAt'}},
    {'field': 'TicketType', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'SysClassName', 'u_inf_generic_request': 'SysClassName', 'sc_req_item': 'SysClassName', 'sc_task': 'SysClassName'}},
    {'field': 'UponApprovalAction', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UponApproval', 'u_inf_generic_request': 'UponApproval', 'sc_req_item': 'UponApproval', 'sc_task': 'UponApproval'}},
    {'field': 'UponRejectionAction', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UponReject', 'u_inf_generic_request': 'UponReject', 'sc_req_item': 'UponReject', 'sc_task': 'UponReject'}},
    {'field': 'SupplierThirdPartyTicket', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'VendorTicket', 'u_inf_generic_request': 'UVendorTicket'}},
    {'field': 'ThirdPartyReferenceName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UThirdPartyReference', 'sc_req_item': 'UExternalReference'}},
    {'field': 'RequestForChangeTicketID', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'Rfc'}},
    {'field': 'ChildIncidentCount', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ChildIncidents'}},
    {'field': 'IncidentState', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'incident': 'IncidentState'}},
    {'field': 'ReOpenedTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ReopenedTime'}},
    {'field': 'NotificationPreference', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'Notify'}},
    {'field': 'ProblemTicketId', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ProblemId'}},
    {'field': 'PromotedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'PromotedOn'}},
    {'field': 'ReOpenCount', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ReopenCount'}},
    {'field': 'AssociatedGenericRequestNumber', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'URequest', 'u_inf_generic_request': 'Request', 'sc_req_item': 'Request', 'sc_task': 'Request'}},
    {'field': 'Severity', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'incident': 'Severity'}},
    {'field': 'WorkEnd', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'sc_req_item': 'WorkEnd', 'sc_task': 'WorkEnd'}},
    {'field': 'WorkStart', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'sc_req_item': 'WorkStart', 'sc_task': 'WorkStart'}},
    {'field': 'AssociatedTaskNumber', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'TaskEffectiveNumber', 'u_inf_generic_request': 'TaskEffectiveNumber', 'sc_req_item': 'TaskEffectiveNumber', 'sc_task': 'TaskEffectiveNumber'}},
    {'field': 'ExpectedStart', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ExpectedStart', 'u_inf_generic_request': 'ExpectedStart', 'sc_req_item': 'ExpectedStart', 'sc_task': 'ExpectedStart'}},
    {'field': 'CatalogueItem', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'sc_req_item': 'CatItem', 'sc_task': 'CatItem'}},
    {'field': 'PendingStatusReason', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'sc_task': 'UPendingReason'}},
    {'field': 'CallBackType', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UCallBackType'}},
    {'field': 'ConfigurationItem', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'incident': 'CmdbCi', 'u_inf_generic_request': 'CmdbCi', 'sc_task': 'CmdbCi'}},
    {'field': 'BusinessDuration', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'BusinessDuration', 'u_inf_generic_request': 'BusinessDuration', 'sc_req_item': 'BusinessDuration', 'sc_task': 'BusinessDuration'}},
    {'field': 'OpenedDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'OpenedAt', 'u_inf_generic_request': 'OpenedAt', 'sc_req_item': 'OpenedAt', 'sc_task': 'OpenedAt'}},
    {'field': 'ParentTicketNumber', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'Parent', 'u_inf_generic_request': 'Parent', 'sc_req_item': 'Parent', 'sc_task': 'Parent'}},
    {'field': 'DueDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'DueDate', 'u_inf_generic_request': 'DueDate', 'sc_req_item': 'DueDate', 'sc_task': 'DueDate'}},
    {'field': 'SLAResolutionDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'SlaDue', 'u_inf_generic_request': 'SlaDue', 'sc_req_item': 'SlaDue', 'sc_task': 'SlaDue'}},
    {'field': 'IsSLAExempt', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'USlaExempt', 'u_inf_generic_request': 'USlaExempt', 'sc_req_item': 'USlaExempt', 'sc_task': 'USlaExempt'}},
    {'field': 'ChildService', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UService', 'u_inf_generic_request': 'UService', 'sc_req_item': 'UService', 'sc_task': 'UService'}},
    {'field': 'IsShouldHaveBeenResolvedAtServiceDesk', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UShouldHaveBeenResolvedAtServiceDesk', 'u_inf_generic_request': 'UShouldHaveBeenResolvedAtServiceDesk', 'sc_task': 'UShouldHaveBeenResolvedAtServiceDesk'}},
    {'field': 'MajorIncidentGrade', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'incident': 'UMajorIncidentGrade'}},
    {'field': 'IsMajorIncident', 'dataType': BooleanType(), 'personal': False, 'sensitive': True, 'from': {'incident': 'UMajorIncident'}},
    {'field': 'MajorIncidentState', 'dataType': StringType(), 'personal': False, 'sensitive': True, 'from': {'incident': 'MajorIncidentState'}},
    {'field': 'CsatCompletedDateTime', 'dataType': TimestampType(), 'personal': False, 'sensitive': False, 'from': {'asmt_assessment_instance':['TakenOn', 'TaskId', 'Number']}, 'calculated_field': True},
    {'field': 'CsatScore', 'dataType': IntegerType(), 'personal': False, 'sensitive': False, 'from': {'asmt_assessment_instance_question': ['Value', 'Instance', 'Category']}, 'calculated_field': True},
    {'field': 'IsAnEnhancement', 'dataType': BooleanType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'UEnhancement', 'u_inf_generic_request': 'UEnhancement', 'sc_task': 'UEnhancement'}},
    {'field': 'ReceiptDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'ReceiptDate', 'u_inf_generic_request': 'ReceiptDate', 'sc_req_item': 'ReceiptDate', 'sc_task': 'ReceiptDate'}},
    {'field': 'AllocatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'AllocatedDate', 'u_inf_generic_request': 'AllocatedDate', 'sc_req_item': 'AllocatedDate', 'sc_task': 'AllocatedDate'}},
    {'field': 'SourceSystem', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'SourceSystem', 'u_inf_generic_request': 'SourceSystem', 'sc_req_item': 'SourceSystem', 'sc_task': 'SourceSystem'}},
    {'field': 'PipelineUpdatedDate', 'dataType': DateType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'PipelineUpdatedDate', 'u_inf_generic_request': 'PipelineUpdatedDate', 'sc_req_item': 'PipelineUpdatedDate', 'sc_task': 'PipelineUpdatedDate'}},
    {'field': 'TableName', 'dataType': StringType(), 'personal': False, 'sensitive': False, 'from': {'incident': 'TableName', 'u_inf_generic_request': 'TableName', 'sc_req_item': 'TableName', 'sc_task': 'TableName'}}
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
