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
# META       "environmentId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
# META       "workspaceId": "00000000-0000-0000-0000-000000000000"
# META     }
# META   }
# META }

# MARKDOWN ********************

# #### Generate Conformed - Dim Supplier
# ---
# Notebook to perform the creation of Dim Supplier, storing the table in the `Conformed` Lakehouse as delta format
# 
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

%run nb_schema_dim_supplier

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

table_name = 'dim_supplier'
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
# servicenow - suppliers transformations (master)
df_suppliers = df_dicts['suppliers'] \
    .filter((F.col('Name').isNotNull()) & (F.col('Name') != '')) \
    .transform(lambda df: conformed_select_alias_and_cast(df, target_schema, 'suppliers', 'before')) \
    .transform(lambda df: add_hash_key(df, primary_key, ['Name'], globals()['service_now']['name'])) \
    .transform(lambda df: add_hash_key(df, 'SupplierParentKey', ['Parent'], globals()['service_now']['name']))

# leanix - provider transformations
df_provider = df_dicts['Provider'] \
    .filter((F.col('Name').isNotNull()) | (F.col('Name') != '')) \
    .transform(lambda df: conformed_select_alias_and_cast(df, target_schema, 'Provider', 'before')) \
    .transform(lambda df: add_hash_key(df, primary_key, ['Name'], globals()['lean_ix']['name'])) \
    .transform(lambda df: add_hash_key(df, 'SupplierParentKey', ['RelToParent'], globals()['lean_ix']['name'])) \
    .transform(lambda df: fill_unknown_columns(df, [primary_key] + metadata_fields + ['SupplierParentKey']))

# Retrieve smaller subset of sys_user  
df_sys_user = df_dicts['sys_user'].select(*['SysId', 'Email'])  

# ServiceNow - create personal related foreign keys  
personal_schema = [x for x in target_schema if x['field'].endswith('Key')  
                   and x['field'] != primary_key  
                   and x['field'] != 'SupplierParentKey'  # exclude non-user keys  
                   and 'core_company' in x['from'].keys()] 

# Define foreign key mappings
personal_keys = {  
    'UBusinessOwner': 'BusinessOwnerKey',  
    'SysCreatedBy': 'CreatedByKey',  
    'SysUpdatedBy': 'UpdatedByKey',  
    'USecurityServiceOwner': 'SecurityServiceOwnerKey'  
}  

# ServiceNow - core_company transformations
df_core_company = (df_dicts['core_company']
    .filter((F.col('Name').isNotNull()) & (F.col('Name') != ''))
    .filter(F.col('Vendor') == 'true')
    .filter(F.col('UActive') == 'true')
    .transform(lambda df: deduplicate_by_keys(df, ['Name'], ['SysCreatedOn']))
    .withColumn(
        'SupplierStatus',
        F.when(F.col('UActive') == 'true', F.lit('Active'))
         .otherwise(F.lit('Inactive'))
    )
    .withColumn(
        'IsVendor',
        F.when(F.col('Vendor') == 'true', F.lit(True))
         .otherwise(F.lit(False))
    )
)

# Store original columns for foreign keys BEFORE schema transformation
df_core_company_with_ids = df_core_company.select(
    'Name',
    *[F.col(col).alias(f"orig_{col}") for col in personal_keys.keys()]
)

# Apply the schema transformation
df_core_company = df_core_company.transform(
    lambda df: conformed_select_alias_and_cast(df, target_schema, 'core_company', 'before')
)

# Add hash key
df_core_company = df_core_company.transform(
    lambda df: add_hash_key(df, primary_key, ['Name'], globals()['service_now']['name'])
)

# Join back the original ID columns
df_core_company = df_core_company.join(
    df_core_company_with_ids,
    'Name',
    'left'
)

# Generate foreign keys
for orig_col, key_name in personal_keys.items():
    orig_col_name = f"orig_{orig_col}"

    # Join with sys_user to get email
    temp_df = df_core_company.join(
        df_sys_user,
        F.col(orig_col_name) == df_sys_user.SysId,
        'left'
    )

    # Create a column with either email or original value
    temp_df = temp_df.withColumn(
        'value_to_hash',
        F.when(
            F.col('Email').isNotNull(),
            F.col('Email')
        ).otherwise(
            F.col(orig_col_name)
        )
    )

    # Use add_hash_key to generate the key consistently
    temp_df = temp_df.transform(
        lambda df: add_hash_key(df, key_name, ['value_to_hash'], globals()['service_now']['name'])
    )

    # Drop temporary columns and keep the result
    df_core_company = temp_df.drop('SysId', 'Email', 'value_to_hash')

# Drop the original columns
columns_to_drop = [f"orig_{col}" for col in personal_keys.keys()]
df_core_company = df_core_company.drop(*columns_to_drop)

# Fill unknown values in specified columns
df_core_company = df_core_company.transform(
    lambda df: fill_unknown_columns(df, [primary_key] + metadata_fields)
)

# Ensure all required columns are present
required_columns = [f['field'] for f in target_schema]
for col in required_columns:
    if col not in df_core_company.columns:
        df_core_company = df_core_company.withColumn(col, F.lit(None))

# Union the dataframes, add IsMaster and de-duplicate
attributes = [f['field'] for f in target_schema if f['field'] not in metadata_fields + [primary_key]]

df = (
    df_suppliers
    .unionByName(df_provider, allowMissingColumns=True)
    .unionByName(df_core_company, allowMissingColumns=True)
    .select(*[F.col(f['field']) for f in target_schema])
    .withColumn(
        'IsTechnologySupplier',
        F.when(
            (F.col('SourceSystem') == 'Coupa') & (F.col('ContentGroups').contains('Technology')),
            F.lit(True)
        ).otherwise(F.lit(False))
    )
    .filter(
        (F.col('SourceSystem') != 'Coupa') | (F.col('IsTechnologySupplier') == True)
    )
    .transform(lambda df: add_hash_key(df, attributes_key, attributes))
    .withColumn('IsMaster', 
        F.when(F.col('SourceSystem') == globals()['coupa']['name'], F.lit(True))
         .otherwise(F.lit(False))
    )
    .transform(lambda df: deduplicate_by_keys(df, [primary_key], ['LastUpdatedDateTime']))
)
##### END TRANSFORMATION #####

##### START PRIVACY #####
# Note: masking only happens at the harmonisation stage
##### END PRIVACY #####

##### START WRITE #####
# write to Conformed
delta_writer(
    df = df, 
    lakehouse_name = global_configs['conformed_lh_name'], 
    table = target_table_configs['name'], 
    schema_version = target_table_configs['schema_version'], 
    write_type = target_table_configs['write_type'], 
    primary_key = primary_key, 
    attributes_key = attributes_key
)
##### END WRITE #####

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
