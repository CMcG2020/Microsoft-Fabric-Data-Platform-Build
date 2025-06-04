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
# META     },
# META     "environment": {
# META       "environmentId": "894291a9-f8d5-4ea0-8d4d-a41d3d9b7541",
# META       "workspaceId": "00000000-0000-0000-0000-000000000000"
# META     }
# META   }
# META }

# MARKDOWN ********************

# #### Generate Conformed - Dim User
# ---
# Notebook to perform the creation of Dim User, storing the table in the Conformed Lakehouse as delta format
# 
# ###### **<u>Step 1: Import common libraries and helper functions</u>**
# 
# - Import any required public libraries and custom functions via `%run` magic command. 
# - Custom functions are defined and stored within other notebooks within `notebooks/utilities/nb_helper_functions_<action>.py`.

# CELL ********************

%run nb_helper_functions_parent_caller

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_schema_dim_user

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ###### **<u>Step 2: Define Parameters</u>**
# - The following cell is noted as a Parameter cell; default values can be overwritten when the notebook is executed either via DAG calls or Data Factory Pipelines. 
# - To 'parameterize' a code cell, click on the `...` 'more command' button on the right as you hover your cursor over the cell and click `[@] Toggle parameter cell`

# PARAMETERS CELL ********************

trigger_time = None

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ###### **<u>Step 3: Extract configurations and table schema</u>**
# - Extract global configuration and table specific configuration defined in `notebooks/nb_configs.py`. 
# - Extract table schema defined in `notebooks/schemas/<source> or <target/<facts> or <dimension>>/`

# CELL ********************

table_name = 'dim_user'
conformed_layer = 'dimensions'

global_configs = globals()['global_configs']
target_table_configs = globals()[conformed_layer][table_name]
target_schema = globals()[f"schema_{table_name}_v{target_table_configs['schema_version']}"]

primary_key = target_table_configs['primary_key']
attributes_key = target_table_configs['attributes_key']
metadata_fields = global_configs['metadata_fields']

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Main Code Block
# ---
# ###### **<u>Step 3: Perform ETL</u>**
# Extract, transform and load data.

# CELL ********************

##### START EXTRACT #####
df_dicts = read_all_required_dataframes(target_table_configs['required_tables'], target_schema, trigger_time, False)
##### END EXTRACT #####

##### START TRANSFORMATION #####
# Start with users table - only keep essential columns and lowercase the join column
df_users_base = df_dicts['users'] \
    .withColumn('UserPrincipalName_lower', F.lower(F.col('UserPrincipalName'))) \
    .select(
        'UserPrincipalName',
        'UserPrincipalName_lower',  
        'DisplayName',
        'DeletedDateTime',
        'ExtensionAttribute10',
        'AllocatedDate',
        'SourceSystem',
        'PipelineUpdatedDate',
        'TableName'
    ) \
    .na.drop(subset=['UserPrincipalName'])

# Prepare sap_employee dataframe with duplicate handling based on latest sap_HireDate  
df_sap = df_dicts['sap_employee'] \
    .withColumn('sap_Upn_lower', F.lower(F.col('Upn'))) \
    .select([F.col(c).alias(f"sap_{c}") for c in df_dicts['sap_employee'].columns] +   
            [F.col('sap_Upn_lower')]) \
    .withColumn('row_number', F.row_number().over(  
        Window.partitionBy('sap_EmpNumber')  
        .orderBy(F.col('sap_HireDate').desc())  
    )) \
    .filter(F.col('row_number') == 1) \
    .drop('row_number')

# Prepare Oracle Employee dataframe with duplicate handling based on latest emp_DateStart  
df_employee = df_dicts['Employee'] \
    .withColumn('emp_Attribute16_lower', F.lower(F.col('Attribute16'))) \
    .select([F.col(c).alias(f"emp_{c}") for c in df_dicts['Employee'].columns] +   
            [F.col('emp_Attribute16_lower')]) \
    .withColumn('row_number', F.row_number().over(  
        Window.partitionBy('emp_EmployeeNumber')  
        .orderBy(F.col('emp_DateStart').desc())  
    )) \
    .filter(F.col('row_number') == 1) \
    .drop('row_number')  

# Create manager lookup dataframe to create ManagerUserPrincipalName
manager_lookup = df_dicts['Employee'].select(
    F.col('EmployeeNumber').alias('manager_emp_number'),
    F.col('Attribute16').alias('ManagerUserPrincipalName')
).na.drop(subset=['manager_emp_number', 'ManagerUserPrincipalName'])

# Join the dataframes from 3 sources
df = df_users_base \
    .join(df_sap, df_users_base.UserPrincipalName_lower == df_sap.sap_Upn_lower, 'left') \
    .join(df_employee, df_users_base.UserPrincipalName_lower == df_employee.emp_Attribute16_lower, 'left') \
    .join(manager_lookup, F.col('emp_SupervisorId') == F.col('manager_emp_number'), 'left')

# Drop the temporary columns not required in final schema
df = df.drop('UserPrincipalName_lower', 'sap_Upn_lower', 'emp_Attribute16_lower')

field_expressions = []
for field in target_schema:
    field_name = field['field']
    if 'from' in field:
        sources = field['from']

        if field_name == 'ManagerUserPrincipalName':
            # Use the looked-up ManagerUserPrincipalName
            expr = F.col('ManagerUserPrincipalName').alias(field_name)
        elif field_name == 'UserPrincipalName':
            # Use the base UserPrincipalName from users table
            expr = F.col('UserPrincipalName')
        elif field_name in ['AllocatedDate', 'SourceSystem', 'PipelineUpdatedDate', 'TableName']:
            # Special handling for metadata fields
            coalesce_cols = []
            # Build a list of columns to coalesce, checking each possible source system
            if 'users' in sources:
                coalesce_cols.append(F.col(sources['users']))
            if 'sap_employee' in sources:
                coalesce_cols.append(F.col(f"sap_{sources['sap_employee']}"))
            if 'Employee' in sources:
                coalesce_cols.append(F.col(f"emp_{sources['Employee']}"))
            expr = F.coalesce(*coalesce_cols).alias(field_name)
        # Handle fields that exist in both SAP and Oracle Employee (prioritizing SAP over Oracle)
        elif 'sap_employee' in sources and 'Employee' in sources:
            sap_col = f"sap_{sources['sap_employee']}"
            emp_col = f"emp_{sources['Employee']}"
            expr = F.coalesce(
                F.col(sap_col),
                F.col(emp_col)
            ).alias(field_name)
        # Handle fields that exist only in SAP
        elif 'sap_employee' in sources:
            sap_col = f"sap_{sources['sap_employee']}"
            expr = F.col(sap_col).alias(field_name)
        # Handle fields that exist only in Employee
        elif 'Employee' in sources:
            emp_col = f"emp_{sources['Employee']}"
            expr = F.col(emp_col).alias(field_name)
        # Handle fields that exist only in Users
        elif 'users' in sources:
            expr = F.col(sources['users']).alias(field_name)
        # Default case: if field doesn't exist in any source, create NULL column with proper data type
        else:
            expr = F.lit(None).cast(field['dataType']).alias(field_name)
        # Add the constructed expression to list of fields to be selected
        field_expressions.append(expr)

# Select final columns with proper casting
df = df.select(*field_expressions) \
    .transform(lambda df: add_hash_key(df, 'UserKey', ['UserPrincipalName'], None))

# Generate Attributes hash key
attributes = [f['field'] for f in target_schema if f['field'] not in metadata_fields + [primary_key]]
df = df.transform(lambda df: add_hash_key(df, attributes_key, attributes))
##### END TRANSFORMATION #####

##### START PRIVACY #####
df, df_privacy = handle_personal_and_sensitive_fields(df, target_schema, primary_key)
##### END PRIVACY #####

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ###### **Running Data Quality Checks**
# 
# ---
# - [Check the Data Quality Checks Wiki for info on running DQ checks](https://informaeds.visualstudio.com/Global%20Support/_wiki/wikis/Global-Support.wiki/38/Running-Data-Quality-Checks).

# CELL ********************

%run nb_helper_functions_data_quality

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Variable to store error data from runs (if any)
errors = []

##### START WRITE #####
try:
    #Non PII Data
    execute_write_to_lakehouse_with_dq_checks(df=df, layer='Conformed', write_mode_cleansed=None, partition_by = None, pii_enabled = False)
except Exception as e:
    errors.append(f"Non-PII Data Check failed: {str(e)}")

#PII Data
if df_privacy:
    try:
        execute_write_to_lakehouse_with_dq_checks(df=df_privacy, layer='Conformed', write_mode_cleansed=None, partition_by = None, pii_enabled = True)
    except Exception as e:
        errors.append(f"PII Data Check failed: {str(e)}")
##### END WRITE #####

# Raise error if any checks failed
if errors:
    raise Exception("One or more data quality checks failed:\n" + "\n".join(errors))
else:
    print("Both Non-PII and PII Data Quality Checks completed successfully.")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
