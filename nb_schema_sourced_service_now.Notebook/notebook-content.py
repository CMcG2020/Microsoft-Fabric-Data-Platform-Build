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

# ##### CMDB_CI_APPL_V1 Schema
# ---

# CELL ********************

schema_cmdb_ci_appl_v1 = [
    {'from': 'name', 'to': 'Name', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'business_criticality', 'to': 'BusinessCriticality', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'u_primary_parent', 'to': 'UPrimaryParent', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'support_group', 'to': 'SupportGroup', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_technical_group', 'to': 'UTechnicalGroup', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'change_control', 'to': 'ChangeControl', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_change_group', 'to': 'UChangeGroup', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_owner_group', 'to': 'UOwnerGroup', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_active', 'to': 'UActive', 'dataType': BooleanType(), 'personal': False, 'sensitive': True},
    {'from': 'u_additional_notes', 'to': 'UAdditionalNotes', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'asset', 'to': 'Asset', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'asset_tag', 'to': 'AssetTag', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'assigned', 'to': 'Assigned', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'company', 'to': 'Company', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'config_directory', 'to': 'ConfigDirectory', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'config_file', 'to': 'ConfigFile', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'correlation_id', 'to': 'CorrelationId', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'cost', 'to': 'Cost', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'cost_center', 'to': 'CostCenter', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'cost_cc', 'to': 'CostCc', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'sys_created_on', 'to': 'SysCreatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'sys_mod_count', 'to': 'SysModCount', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
    {'from': 'used_for', 'to': 'UsedFor', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'vendor', 'to': 'Vendor', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_verified', 'to': 'UVerified', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'version', 'to': 'Version', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'warranty_expiration', 'to': 'WarrantyExpiration', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_current_criticality_level', 'to': 'UCurrentCriticalityLevel', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'u_unique_identifier', 'to': 'UUniqueIdentifier', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_bc_owner', 'to': 'UBCOwner', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'u_business_continuity_status', 'to': 'UBusinessContinuityStatus', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_business_group', 'to': 'UBusinessGroup', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'sys_class_name', 'to': 'SysClassName', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_crown_jewels_name', 'to': 'UCrownJewelsName', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_crown_jewels_visible', 'to': 'UCrownJewelsVisible', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_dr_owner', 'to': 'UDROwner', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'u_dr_status', 'to': 'UDRStatus', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_deployment_model', 'to': 'UDeploymentModel', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'short_description', 'to': 'ShortDescription', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'u_desiredbusinesscriticality', 'to': 'UDesiredBusinessCriticality', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_drp_last_tested', 'to': 'UDRPLastTested', 'dataType': DateType(), 'personal': False, 'sensitive': False},
    {'from': 'u_division', 'to': 'UDivision', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_effective_date', 'to': 'UEffectiveDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'fqdn', 'to': 'Fqdn', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_impacted_division', 'to': 'UImpactedDivision', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_leaving_date', 'to': 'ULeavingDate', 'dataType': DateType(), 'personal': True, 'sensitive': False},
    {'from': 'location', 'to': 'Location', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_no_longer_supported', 'to': 'UNoLongerSupported', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'operational_status', 'to': 'OperationalStatus', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'owned_by', 'to': 'OwnedBy', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'u_owning_division', 'to': 'UOwningDivision', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_system_rpo', 'to': 'USystemRpo', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
    {'from': 'u_system_rto', 'to': 'USystemRto', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
    {'from': 'u_show_on_service_status_page', 'to': 'UShowOnServiceStatusPage', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'sys_updated_on', 'to': 'SysUpdatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'start_date', 'to': 'StartDate', 'dataType': DateType(), 'personal': False, 'sensitive': False},
    {'from': 'sys_class_path', 'to': 'SysClassPath', 'dataType': StringType(), 'personal': False, 'sensitive': False},
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### INCIDENT_V1 Schema
# ---

# CELL ********************

schema_incident_v1 = [
    {'from': 'number', 'to': 'Number', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_customer', 'to': 'UCustomer', 'dataType': StringType(), 'personal': True, 'sensitive' : False},
    {'from': 'active', 'to': 'Active', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'sys_id', 'to': 'SysId', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'priority', 'to': 'Priority', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_inf_task_state', 'to': 'UInfTaskState', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'state', 'to': 'State', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'vendor', 'to': 'Vendor', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'vendor_ticket', 'to': 'VendorTicket', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'assignment_group', 'to': 'AssignmentGroup', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'assigned_to', 'to': 'AssignedTo', 'dataType': StringType(), 'personal': True, 'sensitive' : False},
    {'from': 'sys_created_on', 'to': 'SysCreatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'sys_mod_count', 'to': 'SysModCount', 'dataType': IntegerType(), 'personal': False, 'sensitive' : False},
    {'from': 'upon_approval', 'to': 'UponApproval', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'upon_reject', 'to': 'UponReject', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'urgency', 'to': 'Urgency', 'dataType': StringType(), 'personal': False, 'sensitive' : True},
    {'from': 'u_vendor_duration', 'to': 'UVendorDuration', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'vendor_closed_at', 'to': 'VendorClosedAt', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'vendor_opened_at', 'to': 'VendorOpenedAt', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'vendor_point_of_contact', 'to': 'VendorPointOfContact', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'vendor_resolved_at', 'to': 'VendorResolvedAt', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_ebond_owner', 'to': 'UEbondOwner', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_ebond_source', 'to': 'UEbondSource', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_ebonded', 'to': 'UEbonded', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_knowledge_article', 'to': 'UKnowledgeArticle', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_on_hold_counter', 'to': 'UOnHoldCounter', 'dataType': IntegerType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_project', 'to': 'UProject', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_project_name', 'to': 'UProjectName', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'business_duration', 'to': 'BusinessDuration', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_vendor_related', 'to': 'UVendorRelated', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'made_sla', 'to': 'MadeSla', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'resolved_at', 'to': 'ResolvedAt', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'sys_class_name', 'to': 'SysClassName', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'rfc', 'to': 'Rfc', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_third_party_reference', 'to': 'UThirdPartyReference', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'reopened_time', 'to': 'ReopenedTime', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'incident_state', 'to': 'IncidentState', 'dataType': StringType(), 'personal': False, 'sensitive' : True},
    {'from': 'child_incidents', 'to': 'ChildIncidents', 'dataType': IntegerType(), 'personal': False, 'sensitive' : False},
    {'from': 'notify', 'to': 'Notify', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'problem_id', 'to': 'ProblemId', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'promoted_on', 'to': 'PromotedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'reopen_count', 'to': 'ReopenCount', 'dataType': IntegerType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_request', 'to': 'URequest', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'severity', 'to': 'Severity', 'dataType': StringType(), 'personal': False, 'sensitive' : True},
    {'from': 'task_effective_number', 'to': 'TaskEffectiveNumber', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'expected_start', 'to': 'ExpectedStart', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_call_back_type', 'to': 'UCallBackType', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_major_incident_grade', 'to': 'UMajorIncidentGrade', 'dataType': StringType(), 'personal': False, 'sensitive' : True},
    {'from': 'u_major_incident', 'to': 'UMajorIncident', 'dataType': BooleanType(), 'personal': False, 'sensitive' : True},
    {'from': 'cmdb_ci', 'to': 'CmdbCi', 'dataType': StringType(), 'personal': False, 'sensitive' : True},
    {'from': 'opened_at', 'to': 'OpenedAt', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'major_incident_state', 'to': 'MajorIncidentState', 'dataType': StringType(), 'personal': False, 'sensitive' : True},
    {'from': 'parent', 'to': 'Parent', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'due_date', 'to': 'DueDate', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'sla_due', 'to': 'SlaDue', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_sla_exempt', 'to': 'USlaExempt', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_service', 'to': 'UService', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_should_have_been_resolved_at_service_desk', 'to': 'UShouldHaveBeenResolvedAtServiceDesk', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'closed_by', 'to': 'ClosedBy', 'dataType': StringType(), 'personal': True, 'sensitive' : False},
    {'from': 'opened_by', 'to': 'OpenedBy', 'dataType': StringType(), 'personal': True, 'sensitive' : False},
    {'from': 'resolved_by', 'to': 'ResolvedBy', 'dataType': StringType(), 'personal': True, 'sensitive' : False},
    {'from': 'u_application', 'to': 'UApplication', 'dataType': StringType(), 'personal': False, 'sensitive' : True},
    {'from': 'sys_updated_on', 'to': 'SysUpdatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},    
    {'from': 'u_business_sponsor', 'to': 'UBusinessSponsor', 'dataType': StringType(), 'personal': True, 'sensitive' : False},
    {'from': 'x_bate_transport_e_project_id', 'to': 'XBateTransportEProjectId', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'origin_table', 'to': 'OriginTable', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'approval_history', 'to': 'ApprovalHistory', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'skills', 'to': 'Skills', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_enhancement', 'to': 'UEnhancement', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'lessons_learned', 'to': 'LessonsLearned', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'knowledge', 'to': 'Knowledge', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'order', 'to': 'Order', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'contract', 'to': 'Contract', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'impact', 'to': 'Impact', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'sys_domain_path', 'to': 'SysDomainPath', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'group_list', 'to': 'GroupList', 'dataType': ArrayType(StringType()), 'personal': False, 'sensitive' : False},
    {'from': 'u_start_date', 'to': 'UStartDate', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'approval_set', 'to': 'ApprovalSet', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'universal_request', 'to': 'UniversalRequest', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'work_start', 'to': 'WorkStart', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'correlation_display', 'to': 'CorrelationDisplay', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_application_instance', 'to': 'UApplicationInstance', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'service_offering', 'to': 'ServiceOffering', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'follow_up', 'to': 'FollowUp', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'parent_incident', 'to': 'ParentIncident', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'reassignment_count', 'to': 'ReassignmentCount', 'dataType': IntegerType(), 'personal': False, 'sensitive' : False},
    {'from': 'x_bate_transport_e_te_attempts', 'to': 'XBateTransportETeAttempts', 'dataType': IntegerType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_category', 'to': 'UCategory', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'escalation', 'to': 'Escalation', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'correlation_id', 'to': 'CorrelationId', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'timeline', 'to': 'Timeline', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_delivery_date', 'to': 'UDeliveryDate', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'hold_reason', 'to': 'HoldReason', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'sys_domain', 'to': 'SysDomain', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_ibm_ass_group', 'to': 'UIbmAssGroup', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'proposed_on', 'to': 'ProposedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'x_bate_transport_e_te_type_id', 'to': 'XBateTransportETeTypeId', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'calendar_stc', 'to': 'CalendarStc', 'dataType': IntegerType(), 'personal': False, 'sensitive' : False},
    {'from': 'closed_at', 'to': 'ClosedAt', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_requesttask', 'to': 'URequesttask', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'business_service', 'to': 'BusinessService', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'time_worked', 'to': 'TimeWorked', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'work_end', 'to': 'WorkEnd', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'subcategory', 'to': 'Subcategory', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_breached_sla', 'to': 'UBreachedSla', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'close_code', 'to': 'CloseCode', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'business_stc', 'to': 'BusinessStc', 'dataType': IntegerType(), 'personal': False, 'sensitive' : False},
    {'from': 'cause', 'to': 'Cause', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'origin_id', 'to': 'OriginId', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'calendar_duration', 'to': 'CalendarDuration', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_opex', 'to': 'UOpex', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'x_bate_transport_e_te_status', 'to': 'XBateTransportETeStatus', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'contact_type', 'to': 'ContactType', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'company', 'to': 'Company', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_resolution_sla_percent', 'to': 'UResolutionSlaPercent', 'dataType': DecimalType(), 'personal': False, 'sensitive' : False},
    {'from': 'activity_due', 'to': 'ActivityDue', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_external_reference', 'to': 'UExternalReference', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_reassigned_count', 'to': 'UReassignedCount', 'dataType': IntegerType(), 'personal': False, 'sensitive' : False},
    {'from': 'approval', 'to': 'Approval', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'sys_tags', 'to': 'SysTags', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_date_of_escalation', 'to': 'UDateOfEscalation', 'dataType': DateType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_escalated', 'to': 'UEscalated', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'category', 'to': 'Category', 'dataType': StringType(), 'personal': False, 'sensitive' : False}
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### U_INF_GENERIC_REQUEST_V1 Schema
# ---

# CELL ********************

schema_u_inf_generic_request_v1 = [
    {'from': 'active', 'to': 'Active', 'dataType': BooleanType(), 'personal': False, 'sensitive': False}, 
    {'from': 'activity_due', 'to': 'ActivityDue', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'approval', 'to': 'Approval', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'sys_id', 'to': 'SysId', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'approval_history', 'to': 'ApprovalHistory', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'approval_set', 'to': 'ApprovalSet', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'assigned_to', 'to': 'AssignedTo', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'assignment_group', 'to': 'AssignmentGroup', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'backordered', 'to': 'Backordered', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'billable', 'to': 'Billable', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'business_duration', 'to': 'BusinessDuration', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'business_service', 'to': 'BusinessService', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'calendar_duration', 'to': 'CalendarDuration', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'cat_item', 'to': 'CatItem', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'closed_at', 'to': 'ClosedAt', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'closed_by', 'to': 'ClosedBy', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'cmdb_ci', 'to': 'CmdbCi', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'company', 'to': 'Company', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'configuration_item', 'to': 'ConfigurationItem', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'contact_type', 'to': 'ContactType', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'context', 'to': 'Context', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'correlation_display', 'to': 'CorrelationDisplay', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'correlation_id', 'to': 'CorrelationId', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'due_date', 'to': 'DueDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'escalation', 'to': 'Escalation', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'estimated_delivery', 'to': 'EstimatedDelivery', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'expected_start', 'to': 'ExpectedStart', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'flow_context', 'to': 'FlowContext', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'follow_up', 'to': 'FollowUp', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'group_list', 'to': 'GroupList', 'dataType': ArrayType(StringType(), True), 'personal': False, 'sensitive': False},
    {'from': 'knowledge', 'to': 'Knowledge', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'made_sla', 'to': 'MadeSla', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'number', 'to': 'Number', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'opened_at', 'to': 'OpenedAt', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'opened_by', 'to': 'OpenedBy', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'order', 'to': 'Order', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'order_guide', 'to': 'OrderGuide', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'parent', 'to': 'Parent', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'price', 'to': 'Price', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'priority', 'to': 'Priority', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'quantity', 'to': 'Quantity', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
    {'from': 'quantity_sourced', 'to': 'QuantitySourced', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
    {'from': 'reassignment_count', 'to': 'ReassignmentCount', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
    {'from': 'received', 'to': 'Received', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'recurring_frequency', 'to': 'RecurringFrequency', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'recurring_price', 'to': 'RecurringPrice', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'request', 'to': 'Request', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'sc_catalog', 'to': 'ScCatalog', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'service_offering', 'to': 'ServiceOffering', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'sla_due', 'to': 'SlaDue', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'sourced', 'to': 'Sourced', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'state', 'to': 'State', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'sys_class_name', 'to': 'SysClassName', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'sys_created_on', 'to': 'SysCreatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'sys_updated_on', 'to': 'SysUpdatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'task_effective_number', 'to': 'TaskEffectiveNumber', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'time_worked', 'to': 'TimeWorked', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_60_days_auto_close', 'to': 'U60DaysAutoClose', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'u_application', 'to': 'UApplication', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'u_attatchment', 'to': 'UAttatchment', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_breached_sla', 'to': 'UBreachedSla', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_business_sponsor', 'to': 'UBusinessSponsor', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'u_call_back_type', 'to': 'UCallBackType', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_category', 'to': 'UCategory', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_close_code', 'to': 'UCloseCode', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_contact_type', 'to': 'UContactType', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_customer', 'to': 'UCustomer', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'u_date_of_escalation', 'to': 'UDateOfEscalation', 'dataType': DateType(), 'personal': False, 'sensitive': False},
    {'from': 'u_delivery_date', 'to': 'UDeliveryDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'u_ebond_owner', 'to': 'UEbondOwner', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'u_ebond_source', 'to': 'UEbondSource', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'u_enhancement', 'to': 'UEnhancement', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'u_escalated', 'to': 'UEscalated', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'u_external_reference', 'to': 'UExternalReference', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_hidden_workflow_check', 'to': 'UHiddenWorkflowCheck', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_hold_reason', 'to': 'UHoldReason', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_inf_task_state', 'to': 'UInfTaskState', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_on_hold_counter', 'to': 'UOnHoldCounter', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
    {'from': 'u_opex', 'to': 'UOpex', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'u_project', 'to': 'UProject', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_project_name', 'to': 'UProjectName', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_reassigned_count', 'to': 'UReassignedCount', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
    {'from': 'u_requested_for', 'to': 'URequestedFor', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'u_resolution_sla_percent', 'to': 'UResolutionSlaPercent', 'dataType': DecimalType(10,0), 'personal': False, 'sensitive': False},
    {'from': 'u_resolved_at', 'to': 'UResolvedAt', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'u_resolved_by', 'to': 'UResolvedBy', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'u_rfc', 'to': 'URfc', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_send_survey', 'to': 'USendSurvey', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'u_service', 'to': 'UService', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_should_have_been_resolved_at_service_desk', 'to': 'UShouldHaveBeenResolvedAtServiceDesk', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'u_sla_exempt', 'to': 'USlaExempt', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'u_start_date', 'to': 'UStartDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'u_string_1', 'to': 'UString1', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_type', 'to': 'UType', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_vendor', 'to': 'UVendor', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_vendor_related', 'to': 'UVendorRelated', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'u_vendor_ticket', 'to': 'UVendorTicket', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'universal_request', 'to': 'UniversalRequest', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'upon_approval', 'to': 'UponApproval', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'upon_reject', 'to': 'UponReject', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'urgency', 'to': 'Urgency', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'work_end', 'to': 'WorkEnd', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'work_start', 'to': 'WorkStart', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'x_bate_transport_e_project_id', 'to': 'XBateTransportEProjectId', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'x_bate_transport_e_te_attempts', 'to': 'XBateTransportETeAttempts', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
    {'from': 'x_bate_transport_e_te_status', 'to': 'XBateTransportETeStatus', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'x_bate_transport_e_te_type_id', 'to': 'XBateTransportETeTypeId', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'contract', 'to': 'Contract', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'sys_domain_path', 'to': 'SysDomainPath', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'sys_domain', 'to': 'SysDomain', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'sys_tags', 'to': 'SysTags', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'stage', 'to': 'Stage', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'skills', 'to': 'Skills', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'sys_mod_count', 'to': 'SysModCount', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
    {'from': 'u_purchase_order', 'to': 'UPurchaseOrder', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_application_instance', 'to': 'UApplicationInstance', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'impact', 'to': 'Impact', 'dataType': StringType(), 'personal': False, 'sensitive': False}
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### SC_REQ_ITEM_V1 Schema
# ---

# CELL ********************

schema_sc_req_item_v1 = [
    {'from': 'upon_approval', 'to': 'UponApproval', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'upon_reject', 'to': 'UponReject', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'work_end', 'to': 'WorkEnd', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'sys_id', 'to': 'SysId', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'work_start', 'to': 'WorkStart', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'approval', 'to': 'Approval', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'request', 'to': 'Request', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'business_service', 'to': 'BusinessService', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_category', 'to': 'UCategory', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_close_code', 'to': 'UCloseCode', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'configuration_item', 'to': 'ConfigurationItem', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'state', 'to': 'State', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_inf_task_state', 'to': 'UInfTaskState', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_customer', 'to': 'UCustomer', 'dataType': StringType(), 'personal': True, 'sensitive' : False},
    {'from': 'u_date_of_escalation', 'to': 'UDateOfEscalation', 'dataType': DateType(), 'personal': False, 'sensitive' : False},
    {'from': 'due_date', 'to': 'DueDate', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'sla_due', 'to': 'SlaDue', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_breached_sla', 'to': 'UBreachedSla', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'activity_due', 'to': 'ActivityDue', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'business_duration', 'to': 'BusinessDuration', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'task_effective_number', 'to': 'TaskEffectiveNumber', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'expected_start', 'to': 'ExpectedStart', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'assignment_group', 'to': 'AssignmentGroup', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'approval_history', 'to': 'ApprovalHistory', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'x_bate_transport_e_project_id', 'to': 'XBateTransportEProjectId', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'impact', 'to': 'Impact', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_escalated', 'to': 'UEscalated', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'active', 'to': 'Active', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_sla_exempt', 'to': 'USlaExempt', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'made_sla', 'to': 'MadeSla', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'knowledge', 'to': 'Knowledge', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'cat_item', 'to': 'CatItem', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_project_name', 'to': 'UProjectName', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_project', 'to': 'UProject', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_on_hold_counter', 'to': 'UOnHoldCounter', 'dataType': IntegerType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_reassigned_count', 'to': 'UReassignedCount', 'dataType': IntegerType(), 'personal': False, 'sensitive' : False},
    {'from': 'reassignment_count', 'to': 'ReassignmentCount', 'dataType': IntegerType(), 'personal': False, 'sensitive' : False},
    {'from': 'sys_mod_count', 'to': 'SysModCount', 'dataType': IntegerType(), 'personal': False, 'sensitive' : False},
    {'from': 'parent', 'to': 'Parent', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'assigned_to', 'to': 'AssignedTo', 'dataType': StringType(), 'personal': True, 'sensitive' : False},
    {'from': 'requested_for', 'to': 'RequestedFor', 'dataType': StringType(), 'personal': True, 'sensitive' : False},
    {'from': 'closed_by', 'to': 'ClosedBy', 'dataType': StringType(), 'personal': True, 'sensitive' : False},
    {'from': 'opened_by', 'to': 'OpenedBy', 'dataType': StringType(), 'personal': True, 'sensitive' : False},
    {'from': 'priority', 'to': 'Priority', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'quantity', 'to': 'Quantity', 'dataType': IntegerType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_external_reference', 'to': 'UExternalReference', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_application', 'to': 'UApplication', 'dataType': StringType(), 'personal': False, 'sensitive' : True},
    {'from': 'u_service', 'to': 'UService', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_business_sponsor', 'to': 'UBusinessSponsor', 'dataType': StringType(), 'personal': True, 'sensitive' : False},
    {'from': 'stage', 'to': 'Stage', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_start_date', 'to': 'UStartDate', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'calendar_duration', 'to': 'CalendarDuration', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'time_worked', 'to': 'TimeWorked', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'closed_at', 'to': 'ClosedAt', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'sys_created_on', 'to': 'SysCreatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'sys_updated_on', 'to': 'SysUpdatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'opened_at', 'to': 'OpenedAt', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'contact_type', 'to': 'ContactType', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'escalation', 'to': 'Escalation', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'sys_class_name', 'to': 'SysClassName', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'number', 'to': 'Number', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'urgency', 'to': 'Urgency', 'dataType': StringType(), 'personal': False, 'sensitive' : True},
    {'from': 'u_60_days_auto_close', 'to': 'U60DaysAutoClose', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False}, 
    {'from': 'x_bate_transport_e_te_status', 'to': 'XBateTransportETeStatus', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'approval_set', 'to': 'ApprovalSet', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'backordered', 'to': 'Backordered', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'billable', 'to': 'Billable', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'sc_catalog', 'to': 'ScCatalog', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'company', 'to': 'Company', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'context', 'to': 'Context', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'contract', 'to': 'Contract', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'correlation_display', 'to': 'CorrelationDisplay', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'correlation_id', 'to': 'CorrelationId', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_ebond_owner', 'to': 'UEbondOwner', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_ebond_source', 'to': 'UEbondSource', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_ebonded', 'to': 'UEbonded', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'estimated_delivery', 'to': 'EstimatedDelivery', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'flow_context', 'to': 'FlowContext', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'follow_up', 'to': 'FollowUp', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'group_list', 'to': 'GroupList', 'dataType': ArrayType(StringType()), 'personal': False, 'sensitive' : False},
    {'from': 'u_opex', 'to': 'UOpex', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'order', 'to': 'Order', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'order_guide', 'to': 'OrderGuide', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'price', 'to': 'Price', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_purchase_order', 'to': 'UPurchaseOrder', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'quantity_sourced', 'to': 'QuantitySourced', 'dataType': IntegerType(), 'personal': False, 'sensitive' : False},
    {'from': 'received', 'to': 'Received', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'recurring_price', 'to': 'RecurringPrice', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'recurring_frequency', 'to': 'RecurringFrequency', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_resolution_sla_percent', 'to': 'UResolutionSlaPercent', 'dataType': DecimalType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_send_survey', 'to': 'USendSurvey', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'service_offering', 'to': 'ServiceOffering', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'skills', 'to': 'Skills', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'sourced', 'to': 'Sourced', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'sys_tags', 'to': 'SysTags', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'universal_request', 'to': 'UniversalRequest', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'sys_domain', 'to': 'SysDomain', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'sys_domain_path', 'to': 'SysDomainPath', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_application_instance', 'to': 'UApplicationInstance', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_string_1', 'to': 'UString1', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### SC_TASK_V1 Schema
# ---

# CELL ********************

schema_sc_task_v1 = [
    {'from': 'number', 'to': 'Number', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_customer', 'to': 'UCustomer', 'dataType': StringType(), 'personal': True, 'sensitive' : False},
    {'from': 'priority', 'to': 'Priority', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'sys_id', 'to': 'SysId', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'state', 'to': 'State', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'assignment_group', 'to': 'AssignmentGroup', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'assigned_to', 'to': 'AssignedTo', 'dataType': StringType(), 'personal': True, 'sensitive' : False},
    {'from': 'sys_created_on', 'to': 'SysCreatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'opened_at', 'to': 'OpenedAt', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_category', 'to': 'UCategory', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'x_bate_transport_e_te_attempts', 'to': 'XBateTransportETeAttempts', 'dataType': IntegerType(), 'personal': False, 'sensitive' : False},
    {'from': 'x_bate_transport_e_te_status', 'to': 'XBateTransportETeStatus', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'x_bate_transport_e_te_type_id', 'to': 'XBateTransportETeTypeId', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_ad_automation_failed', 'to': 'UAdAutomationFailed', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'active', 'to': 'Active', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'activity_due', 'to': 'ActivityDue', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'work_end', 'to': 'WorkEnd', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'work_start', 'to': 'WorkStart', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_application', 'to': 'UApplication', 'dataType': StringType(), 'personal': False, 'sensitive' : True},
    {'from': 'approval', 'to': 'Approval', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'approval_history', 'to': 'ApprovalHistory', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'approval_set', 'to': 'ApprovalSet', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_breached_sla', 'to': 'UBreachedSla', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'business_duration', 'to': 'BusinessDuration', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'business_service', 'to': 'BusinessService', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_business_sponsor', 'to': 'UBusinessSponsor', 'dataType': StringType(), 'personal': True, 'sensitive' : False},
    {'from': 'sc_catalog', 'to': 'ScCatalog', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'closed_at', 'to': 'ClosedAt', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'closed_by', 'to': 'ClosedBy', 'dataType': StringType(), 'personal': True, 'sensitive' : False},
    {'from': 'company', 'to': 'Company', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'cmdb_ci', 'to': 'CmdbCi', 'dataType': StringType(), 'personal': False, 'sensitive' : True},
    {'from': 'contact_type', 'to': 'ContactType', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'correlation_id', 'to': 'CorrelationId', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'correlation_display', 'to': 'CorrelationDisplay', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_date_of_escalation', 'to': 'UDateOfEscalation', 'dataType': DateType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_delivery_date', 'to': 'UDeliveryDate', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'sys_domain', 'to': 'SysDomain', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'sys_domain_path', 'to': 'SysDomainPath', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'due_date', 'to': 'DueDate', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'calendar_duration', 'to': 'CalendarDuration', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'task_effective_number', 'to': 'TaskEffectiveNumber', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_enhancement', 'to': 'UEnhancement', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_escalated', 'to': 'UEscalated', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'escalation', 'to': 'Escalation', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'expected_start', 'to': 'ExpectedStart', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_external_reference', 'to': 'UExternalReference', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'follow_up', 'to': 'FollowUp', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'impact', 'to': 'Impact', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'cat_item', 'to': 'CatItem', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'knowledge', 'to': 'Knowledge', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'made_sla', 'to': 'MadeSla', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_old_servicenow_ref', 'to': 'UOldServicenowRef', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_on_hold_counter', 'to': 'UOnHoldCounter', 'dataType': IntegerType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_opex', 'to': 'UOpex', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'opened_by', 'to': 'OpenedBy', 'dataType': StringType(), 'personal': True, 'sensitive' : False},
    {'from': 'order', 'to': 'Order', 'dataType': IntegerType(), 'personal': False, 'sensitive' : False},
    {'from': 'parent', 'to': 'Parent', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_pending_reason', 'to': 'UPendingReason', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_project', 'to': 'UProject', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'x_bate_transport_e_project_id', 'to': 'XBateTransportEProjectId', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_project_name', 'to': 'UProjectName', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_reassigned_count', 'to': 'UReassignedCount', 'dataType': IntegerType(), 'personal': False, 'sensitive' : False},
    {'from': 'reassignment_count', 'to': 'ReassignmentCount', 'dataType': IntegerType(), 'personal': False, 'sensitive' : False},
    {'from': 'request', 'to': 'Request', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'request_item', 'to': 'RequestItem', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_resolution_sla_percent', 'to': 'UResolutionSlaPercent', 'dataType': DecimalType(), 'personal': False, 'sensitive' : False},
    {'from': 'calendar_stc', 'to': 'CalendarStc', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'sla_due', 'to': 'SlaDue', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_sla_exempt', 'to': 'USlaExempt', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'service_offering', 'to': 'ServiceOffering', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_should_have_been_resolved_at_service_desk', 'to': 'UShouldHaveBeenResolvedAtServiceDesk', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'skills', 'to': 'Skills', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_start_date', 'to': 'UStartDate', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'sys_tags', 'to': 'SysTags', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_inf_task_state', 'to': 'UInfTaskState', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'sys_class_name', 'to': 'SysClassName', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'time_worked', 'to': 'TimeWorked', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'universal_request', 'to': 'UniversalRequest', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'sys_updated_on', 'to': 'SysUpdatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'sys_mod_count', 'to': 'SysModCount', 'dataType': IntegerType(), 'personal': False, 'sensitive' : False},
    {'from': 'upon_approval', 'to': 'UponApproval', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'upon_reject', 'to': 'UponReject', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'urgency', 'to': 'Urgency', 'dataType': StringType(), 'personal': False, 'sensitive' : True},
    {'from': 'u_ebond_owner', 'to': 'UEbondOwner', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_ebond_source', 'to': 'UEbondSource', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_ebonded', 'to': 'UEbonded', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_service', 'to': 'UService', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'contract', 'to': 'Contract', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'group_list', 'to': 'GroupList', 'dataType': ArrayType(StringType()), 'personal': False, 'sensitive' : False},
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### TASK_SLA_V1 Schema
# ---

# CELL ********************

schema_task_sla_v1 = [
    {'from': 'pause_duration', 'to': 'PauseDuration', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'pause_time', 'to': 'PauseTime', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'timezone', 'to': 'Timezone', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'sys_updated_on', 'to': 'SysUpdatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'business_time_left', 'to': 'BusinessTimeLeft', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'duration', 'to': 'Duration', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'sys_id', 'to': 'SysId', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'time_left', 'to': 'TimeLeft', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_breached_first', 'to': 'UBreachedFirst', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'sys_created_on', 'to': 'SysCreatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'percentage', 'to': 'Percentage', 'dataType': DecimalType(8, 2), 'personal': False, 'sensitive' : False},
    {'from': 'u_initial_assignment_group', 'to': 'UInitialAssignmentGroup', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_initial_vendor', 'to': 'UInitialVendor', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'original_breach_time', 'to': 'OriginalBreachTime', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_breached_with_vendor', 'to': 'UBreachedWithVendor', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'business_percentage', 'to': 'BusinessPercentage', 'dataType': DecimalType(8, 2), 'personal': False, 'sensitive' : False},
    {'from': 'end_time', 'to': 'EndTime', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'sys_mod_count', 'to': 'SysModCount', 'dataType': IntegerType(), 'personal': False, 'sensitive' : False},
    {'from': 'active', 'to': 'Active', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
    {'from': 'business_pause_duration', 'to': 'BusinessPauseDuration', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'sla', 'to': 'Sla', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'sys_tags', 'to': 'SysTags', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_breached_with_group', 'to': 'UBreachedWithGroup', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'schedule', 'to': 'Schedule', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'start_time', 'to': 'StartTime', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'business_duration', 'to': 'BusinessDuration', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'task', 'to': 'Task', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_breached_on_date', 'to': 'UBreachedOnDate', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'stage', 'to': 'Stage', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'u_contract', 'to': 'UContract', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'planned_end_time', 'to': 'PlannedEndTime', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
    {'from': 'has_breached', 'to': 'HasBreached', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False}
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### CORE_COMPANY_V1 Schema
# ---

# CELL ********************

schema_core_company_v1 = [
    {'from': 'customer', 'to': 'Customer', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'latitude', 'to': 'Latitude', 'dataType': DecimalType(8, 2), 'personal': False, 'sensitive': False},
    {'from': 'longitude', 'to': 'Longitude', 'dataType': DecimalType(8, 2), 'personal': False, 'sensitive': False},
    {'from': 'manufacturer', 'to': 'Manufacturer', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'name', 'to': 'Name', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'notes', 'to': 'Notes', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'primary', 'to': 'Primary', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'rank_tier', 'to': 'RankTier', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'sys_class_name', 'to': 'SysClassName', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'sys_created_by', 'to': 'SysCreatedBy', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'sys_created_on', 'to': 'SysCreatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'sys_updated_by', 'to': 'SysUpdatedBy', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'sys_updated_on', 'to': 'SysUpdatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'u_active', 'to': 'UActive', 'dataType': BooleanType(), 'personal': False, 'sensitive': True},
    {'from': 'u_additional_service_charges', 'to': 'UAdditionalServiceCharges', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_assessment_frequency', 'to': 'UAssessmentFrequency', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_assessments_reports_and_documents', 'to': 'UAssessmentsReportsAndDocuments', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'u_business_criticality', 'to': 'UBusinessCriticality', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'u_business_owner', 'to': 'UBusinessOwner', 'dataType': StringType(), 'personal': True, 'sensitive': False},
    {'from': 'u_contract_term_in_months', 'to': 'UContractTermInMonths', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'u_date_of_the_one_off_assessment', 'to': 'UDateOfTheOneOffAssessment', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'u_description_of_services_provided', 'to': 'UDescriptionOfServicesProvided', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'u_division', 'to': 'UDivision', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_hardware_software', 'to': 'UHardwareSoftware', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_highest_classification_of_informa_data_processed', 'to': 'UHighestClassificationOfInformaDataProcessed', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'u_hipaa', 'to': 'UHIPAA', 'dataType': BooleanType(), 'personal': False, 'sensitive': True},
    {'from': 'u_how_to_invoke_service_credits', 'to': 'UHowToInvokeServiceCredits', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_informa_responsibilities', 'to': 'UInformaResponsibilities', 'dataType': StringType(), 'personal': False, 'sensitive': True},
    {'from': 'u_intellectual_property', 'to': 'UIntellectualProperty', 'dataType': BooleanType(), 'personal': False, 'sensitive': True},
    {'from': 'u_next_service_review_date', 'to': 'UNextServiceReviewDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'u_notice_period_to_cease', 'to': 'UNoticePeriodToCease', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_other', 'to': 'UOther', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'u_other_service_availability_window', 'to': 'UOtherServiceAvailabilityWindow', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_security_assessment', 'to': 'USecurityAssessment', 'dataType': BooleanType(), 'personal': False, 'sensitive': True},
    {'from': 'u_security_assessment_completed_date', 'to': 'USecurityAssessmentCompletedDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': True},
    {'from': 'u_security_assessment_date', 'to': 'USecurityAssessmentDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': True},
    {'from': 'u_security_assessment_required', 'to': 'USecurityAssessmentRequired', 'dataType': BooleanType(), 'personal': False, 'sensitive': True},
    {'from': 'u_security_assessment_start_date', 'to': 'USecurityAssessmentStartDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': True},
    {'from': 'u_security_service_owner', 'to': 'USecurityServiceOwner', 'dataType': StringType(), 'personal': True, 'sensitive': True},
    {'from': 'u_service_end_date', 'to': 'UServiceEndDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'u_service_levels', 'to': 'UServiceLevels', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_service_owner_approval', 'to': 'UServiceOwnerApproval', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'u_service_reporting_frequency', 'to': 'UServiceReportingFrequency', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_service_review_frequency', 'to': 'UServiceReviewFrequency', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_service_start_date', 'to': 'UServiceStartDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'u_service_transition_period', 'to': 'UServiceTransitionPeriod', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_sub_tower', 'to': 'USubTower', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_support_language', 'to': 'USupportLanguage', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_support_tools', 'to': 'USupportTools', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_support_web_page_portal', 'to': 'USupportWebPagePortal', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_supported_sites', 'to': 'USupportedSites', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_vendor_connectivity_to_informa_systems', 'to': 'UVendorConnectivityToInformaSystems', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_vendor_owned_assets', 'to': 'UVendorOwnedAssets', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_vendor_processing_informa_data', 'to': 'UVendorProcessingInformaData', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_vendor_responsibilities', 'to': 'UVendorResponsibilities', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_vendor_security', 'to': 'UVendorSecurity', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'u_vendor_service_desk_tel_no', 'to': 'UVendorServiceDeskTelNo', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'u_volume_of_informa_data_records_processed', 'to': 'UVolumeOfInformaDataRecordsProcessed', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'vendor', 'to': 'Vendor', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'vendor_type', 'to': 'VendorType', 'dataType': StringType(), 'personal': False, 'sensitive': False}
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### SYS_USER_V1 Schema
# ---

# CELL ********************

schema_sys_user_v1 = [
    {'from': 'sys_id', 'to': 'SysId', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
    {'from': 'user_name', 'to': 'UserName', 'dataType': StringType(), 'personal': True, 'sensitive' : False},
    {'from': 'email', 'to': 'Email', 'dataType': StringType(), 'personal': True, 'sensitive' : False},
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### CMDB_CI_SERVICE_V1 Schema
# ---

# CELL ********************

schema_cmdb_ci_service_v1 = [
  {'from': 'name', 'to': 'Name', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'busines_criticality', 'to': 'BusinessCriticality', 'dataType': StringType(), 'personal': False, 'sensitive' : True},
  {'from': 'operational_status', 'to': 'OperationalStatus', 'dataType': StringType(), 'personal': False, 'sensitive' : True},
  {'from': 'service_classification', 'to': 'ServiceClassification', 'dataType': StringType(), 'personal': False, 'sensitive' : True},
  {'from': 'u_owner_group', 'to': 'Ownergroup', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'u_division', 'to': 'UDivision', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'support_group', 'to': 'SupportGroup', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'change_control', 'to': 'ChangeControl', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'u_active', 'to': 'Active', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
  {'from': 'aliases', 'to': 'Aliases', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'asset', 'to': 'Asset', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'asset_tag', 'to': 'AssetTag', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'assigned', 'to': 'Assigned', 'dataType': DateType(), 'personal': False, 'sensitive' : False},
  {'from': 'attestation_score', 'to': 'AttestationScore', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'attestation_status', 'to': 'AttestationStatus', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'attested', 'to': 'Attested', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
  {'from': 'attested_date', 'to': 'AttestedDate', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'attributes', 'to': 'Attributes', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'business_contact', 'to': 'BusinessContact', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'u_business_group', 'to': 'BusinessGroup', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'business_need', 'to': 'BusinessNeed', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'u_business_unit', 'to': 'BusinessUnit', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'can_print', 'to': 'CanPrint', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'category', 'to': 'Category', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'u_change_group', 'to': 'ChangeGroup', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'checked_in', 'to': 'CheckedIn', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'checked_out', 'to': 'CheckedOut', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'checkout', 'to': 'Checkout', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'sys_class_name', 'to': 'Class', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  #{'from': 'comments', 'to': 'Comments', 'dataType': StringType(), 'personal': True, 'sensitive' : True},
  {'from': 'company', 'to': 'Company', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'compatibility_dependencies', 'to': 'CompatibilityDependencies', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'consumer_type', 'to': 'ConsumerType', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'correlation_id', 'to': 'CorrelationID', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'cost', 'to': 'Cost', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'cost_center', 'to': 'CostCenter', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'cost_cc', 'to': 'CostCurrency', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'sys_created_on', 'to': 'Created', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
  {'from': 'dns_domain', 'to': 'DNSDomain', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'service_owner_delegate', 'to': 'Delegate', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  #{'from': 'delivery_manager', 'to': 'DeliveryManager', 'dataType': StringType(), 'personal': True, 'sensitive' : False},
  {'from': 'department', 'to': 'Department', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'discovery_source', 'to': 'DiscoverySource', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'sys_domain', 'to': 'Domain', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'sys_domain_path', 'to': 'DomainPath', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'due', 'to': 'Due', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'due_in', 'to': 'DueIn', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'duplicate_of', 'to': 'DuplicateOf', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'end_date', 'to': 'EndDate', 'dataType': DateType(), 'personal': False, 'sensitive' : False},
  {'from': 'environment', 'to': 'Environment', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'fault_count', 'to': 'FaultCount', 'dataType': IntegerType(), 'personal': False, 'sensitive' : False},
  {'from': 'first_discovered', 'to': 'FirstDiscovered', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'fqdn', 'to': 'FullyQualifiedDomainName', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'u_gitc_controlled', 'to': 'GITCControlled', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
  {'from': 'gl_account', 'to': 'GLAccount', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  #{'from': 'ip_address', 'to': 'IPAddress', 'dataType': StringType(), 'personal': False, 'sensitive' : True},
  {'from': 'install_status', 'to': 'InstallStatus', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'install_date', 'to': 'Installed', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'invoice_number', 'to': 'InvoiceNumber', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'justification', 'to': 'Justification', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'last_review_date', 'to': 'LastReviewDate', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'lease_id', 'to': 'LeaseContract', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'life_cycle_stage', 'to': 'LifeCycleStage', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'life_cycle_stage_status', 'to': 'LifeCycleStageStatus', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'location', 'to': 'Location', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  #{'from': 'mac_address', 'to': 'MACAddress', 'dataType': StringType(), 'personal': False, 'sensitive' : True},
  {'from': 'maintenance_schedule', 'to': 'MaintenanceSchedule', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'managed_by_group', 'to': 'ManagedByGroup', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'manufacturer', 'to': 'Manufacturer', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'model_id', 'to': 'ModelID', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'model_number', 'to': 'ModelNumber', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'monitor', 'to': 'Monitor', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
  {'from': 'monitoring_requirements', 'to': 'MonitoringRequirements', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'last_discovered', 'to': 'MostRecentDiscovery', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'u_not_visible_in', 'to': 'NotVisibleInPortal', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
  {'from': 'number', 'to': 'Number', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'order_date', 'to': 'OrderDate', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'po_number', 'to': 'PONumber', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'parent', 'to': 'Parent', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'prerequisites', 'to': 'Prerequisites', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'price_model', 'to': 'PriceModel', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'price_unit', 'to': 'PriceUnit', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'u_primary_parent', 'to': 'PrimaryParent', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'published_ref', 'to': 'PublishedRef', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'purchase_date', 'to': 'Purchased', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'u_qa_group', 'to': 'QAGroup', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'u_require_owner_approval', 'to': 'RequireOwnerApproval', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
  {'from': 'sla', 'to': 'SLA', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'schedule', 'to': 'Schedule', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'serial_number', 'to': 'SerialNumber', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'service_level_requirement', 'to': 'ServiceLevelRequirement', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'portfolio_status', 'to': 'ServicePortfolio', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'short_description', 'to': 'ShortDescription', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'skip_sync', 'to': 'SkipSync', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'start_date', 'to': 'StartDate', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'state', 'to': 'State', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'subcategory', 'to': 'Subcategory', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  #{'from': 'supported_by', 'to': 'SupportedBy', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'u_supported_locally', 'to': 'SupportedLocally', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
  {'from': 'sys_tags', 'to': 'Tags', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'u_technical_group', 'to': 'TechnicalGroup', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'total_vulnerable_items', 'to': 'TotalVulnerableItems', 'dataType': IntegerType(), 'personal': False, 'sensitive' : False},
  {'from': 'u_type', 'to': 'Type', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  #{'from': 'unit_description', 'to': 'UnitDescription', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'sys_updated_on', 'to': 'Updated', 'dataType': DateType(), 'personal': False, 'sensitive' : False},
  {'from': 'used_for', 'to': 'UsedFor', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'vendor', 'to': 'Vendor', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'u_verified', 'to': 'Verified', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
  {'from': 'version', 'to': 'Version', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'vulnerability_risk_score', 'to': 'VulnerabilityRiskScore', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### CMDB_REL_CI_V1 Schema
# ---

# CELL ********************

schema_cmdb_rel_ci_v1 = [
  {'from': 'parent', 'to': 'Parent', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'type', 'to': 'Type', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'child', 'to': 'Child', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'sys_mod_count', 'to': 'SysModCount', 'dataType': IntegerType(), 'personal': False, 'sensitive' : False},
  #{'from': 'sys_updated_by', 'to': 'UpdatedBy', 'dataType': StringType(), 'personal': True, 'sensitive' : False},
  {'from': 'sys_updated_on', 'to': 'Updated', 'dataType': DateType(), 'personal': False, 'sensitive' : False},
  {'from': 'sys_tags', 'to': 'Tags', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'port', 'to': 'Port', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  {'from': 'percent_outage', 'to': 'PercentOutage', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
  #{'from': 'u_active', 'to': 'Active', 'dataType': BooleanType(), 'personal': False, 'sensitive' : False},
  {'from': 'sys_created_on', 'to': 'Created', 'dataType': TimestampType(), 'personal': False, 'sensitive' : False},
  {'from': 'connection_strength', 'to': 'ConnectionStrength', 'dataType': StringType(), 'personal': False, 'sensitive' : False},
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### CMDB_CI_OUTAGE_V1 Schema
# ---

# CELL ********************

schema_cmdb_ci_outage_v1 = [
  {'from': 'u_number', 'to': 'Number', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'cmdb_ci', 'to': 'CmdbCi', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'type', 'to': 'Type', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'begin', 'to': 'Begin', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
  {'from': 'end', 'to': 'End', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
  {'from': 'duration', 'to': 'Duration', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'u_application', 'to': 'Application', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'u_autoclose', 'to': 'Autoclose', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
  {'from': 'sys_created_on', 'to': 'Created', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
  {'from': 'sys_domain', 'to': 'Domain', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'sys_domain_path', 'to': 'DomainPath', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'u_notify_group', 'to': 'NotifyGroup', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'u_publish', 'to': 'Publish', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
  {'from': 'u_status', 'to': 'Status', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'sys_tags', 'to': 'Tags', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'task_number', 'to': 'TaskNumber', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'u_template', 'to': 'Template', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'sys_updated_on', 'to': 'Updated', 'dataType': DateType(), 'personal': False, 'sensitive': False},
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### ASMT_ASSESSMENT_INSTANCE_QUESTION_V1 Schema
# ---

# CELL ********************

schema_asmt_assessment_instance_question_v1 = [
  {'from': 'sys_id', 'to': 'SysId', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'instance', 'to': 'Instance', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'category', 'to': 'Category', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'is_hidden', 'to': 'IsHidden', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
  {'from': 'metric', 'to': 'Metric', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'metric_definition', 'to': 'MetricDefinition', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'metric_type_group', 'to': 'MetricTypeGroup', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'reference_id', 'to': 'ReferenceId', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'source_id', 'to': 'SourceId', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'source_table', 'to': 'SourceTable', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'string_value', 'to': 'StringValue', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'sys_created_on', 'to': 'CreatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
  {'from': 'sys_domain', 'to': 'Domain', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'sys_domain_path', 'to': 'DomainPath', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'sys_tags', 'to': 'Tags', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'sys_updated_on', 'to': 'UpdatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
  {'from': 'sys_mod_count', 'to': 'ModCount', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
  {'from': 'value', 'to': 'Value', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### ASMT_ASSESSMENT_INSTANCE_V1 Schema
# ---

# CELL ********************

schema_asmt_assessment_instance_v1 = [
    {'from': 'number', 'to': 'Number', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'metric_type', 'to': 'MetricType', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'due_date', 'to': 'DueDate', 'dataType': DateType(), 'personal': False, 'sensitive': False},
    {'from': 'state', 'to': 'State', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'assessment_group', 'to': 'AssessmentGroup', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'channel', 'to': 'Channel', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'continue_from_question', 'to': 'ContinueFromQuestion', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'sn_grc_item', 'to': 'GrcItem', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'sys_created_on', 'to': 'CreatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'sys_domain', 'to': 'Domain', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'sys_domain_path', 'to': 'DomainPath', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'sn_grc_profile', 'to': 'GrcProfile', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'expiration_date', 'to': 'ExpirationDate', 'dataType': DateType(), 'personal': False, 'sensitive': False},
    {'from': 'sn_grc_parent', 'to': 'GrcParent', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'percent_answered', 'to': 'PercentAnswered', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
    {'from': 'preview', 'to': 'Preview', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
    {'from': 'sn_grc_status', 'to': 'GrcStatus', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'related_table_1', 'to': 'RelatedTable1', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'related_table_2', 'to': 'RelatedTable2', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'related_table_3', 'to': 'RelatedTable3', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'related_table_4', 'to': 'RelatedTable4', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'sn_grc_group_type', 'to': 'GrcGroupType', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'signature', 'to': 'Signature', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'signature_result', 'to': 'SignatureResult', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'sys_tags', 'to': 'Tags', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'take_attestation', 'to': 'TakeAttestation', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'taken_on', 'to': 'TakenOn', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'task_id', 'to': 'TaskId', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'trigger_id', 'to': 'TriggerId', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'trigger_condition', 'to': 'TriggerCondition', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'trigger_table', 'to': 'TriggerTable', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'sys_updated_on', 'to': 'UpdatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
    {'from': 'sys_mod_count', 'to': 'ModCount', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
    {'from': 'view_response', 'to': 'ViewResponse', 'dataType': StringType(), 'personal': False, 'sensitive': False},
    {'from': 'sys_id', 'to': 'SysId', 'dataType': StringType(), 'personal': False, 'sensitive': False},
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### sys_user_grmember_V1 Schema
# ---

# CELL ********************

schema_sys_user_grmember_v1 = [
  {'from': 'sys_id', 'to': 'SysId', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'sys_updated_by', 'to': 'UpdatedBy', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'sys_created_on', 'to': 'CreatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
  {'from': 'sys_mod_count', 'to': 'ModCount', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
  {'from': 'sys_updated_on', 'to': 'UpdatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
  {'from': 'sys_tags', 'to': 'Tags', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'user', 'to': 'User', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'sys_created_by', 'to': 'CreatedBy', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'group', 'to': 'Group', 'dataType': StringType(), 'personal': False, 'sensitive': False},
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### sys_user_group_V1 Schema
# ---

# CELL ********************

schema_sys_user_group_v1 = [
  {'from': 'parent', 'to': 'Parent', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'u_division', 'to': 'Division', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'roles', 'to': 'Roles', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'description', 'to': 'Description', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'u_change', 'to': 'Change', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'u_mulesoft', 'to': 'Mulesoft', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
  {'from': 'source', 'to': 'Source', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'sys_updated_on', 'to': 'UpdatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
  {'from': 'type', 'to': 'Type', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'points', 'to': 'Points', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
  {'from': 'sys_id', 'to': 'SysId', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'u_reporting', 'to': 'Reporting', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'default_assignee', 'to': 'DefaultAssignee', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'sys_created_on', 'to': 'CreatedOn', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
  {'from': 'u_approval', 'to': 'Approval', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'u_business_grp', 'to': 'BusinessGroup', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'vendors', 'to': 'Vendors', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'email', 'to': 'Email', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'sys_created_by', 'to': 'CreatedBy', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'u_leaving_date', 'to': 'LeavingDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
  {'from': 'u_external_reference', 'to': 'ExternalReference', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'u_cmdb', 'to': 'CMDB', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'u_hr', 'to': 'HR', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
  {'from': 'manager', 'to': 'Manager', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'u_effective_date', 'to': 'EffectiveDate', 'dataType': TimestampType(), 'personal': False, 'sensitive': False},
  {'from': 'sys_mod_count', 'to': 'ModCount', 'dataType': IntegerType(), 'personal': False, 'sensitive': False},
  {'from': 'active', 'to': 'Active', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
  {'from': 'average_daily_fte', 'to': 'AverageDailyFTE', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'u_vendor', 'to': 'Vendor', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'sys_tags', 'to': 'Tags', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'u_business_unt', 'to': 'BusinessUnit', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'u_category', 'to': 'Category', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'u_new_manager', 'to': 'NewManager', 'dataType': StringType(), 'personal': True, 'sensitive': False},
  {'from': 'u_service_contract', 'to': 'ServiceContract', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'u_snd_eb_integration', 'to': 'SndEbIntegration', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'cost_center', 'to': 'CostCenter', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'hourly_rate', 'to': 'HourlyRate', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'name', 'to': 'Name', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'u_incident', 'to': 'Incident', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'exclude_manager', 'to': 'ExcludeManager', 'dataType': BooleanType(), 'personal': False, 'sensitive': False},
  {'from': 'u_schedule', 'to': 'Schedule', 'dataType': StringType(), 'personal': False, 'sensitive': False},
  {'from': 'include_members', 'to': 'IncludeMembers', 'dataType': StringType(), 'personal': False, 'sensitive': False}
]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
