# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "environment": {
# META       "environmentId": "xxx",
# META       "workspaceId": "00000000-0000-0000-0000-000000000000"
# META     }
# META   }
# META }

# MARKDOWN ********************

# #### Generate View Definitions
# ---
# Notebook to generate view definitions of assets which are currently live. This notebook will extract the table name, schema version and column names of assets specified in the live_assets array in order to generate two parameters: 
# 
# **table_column_map**: which will be a dictionary mapping of the table names and column values
# 
# **live_table_names** which will be an array/list of the table names in the format asset_name_sv_schema_version where asset name and schema version are the asset names and schema versions as defined by the config files for the live assets.
# 
# **Note**: If the columns of specific assets need to be amended/changed, they have to be specified in the code.

# CELL ********************

%run nb_helper_functions_parent_caller

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Run Schema of Live Assets
# ---
# 
# Always ensure that the schemas of all assets defined in live_assets variable below are run in their own cell.

# CELL ********************

global_configs = globals()['global_configs']

# Initialize dictionaries to hold table names and their columns
table_column_map = {}
live_table_names = []
# Combine the asset infos from dimensions & facts. 
# Excluding harmonized asset info for supplier and application as this should use the same name & schema version for dimensions
all_asset_infos = list(dimensions.values()) + list(facts.values())

live_assets = [asset_list['name'] for asset_list in all_asset_infos if asset_list['live']==True]


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_schema_dim_application

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_schema_dim_application_source

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_schema_dim_application_map

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_schema_dim_date

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_schema_dim_ticket

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_schema_fact_ticket_event

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_schema_fact_outage

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_schema_fact_contract

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_schema_fact_app_classification_map

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_schema_dim_app_classification

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_schema_dim_user_group

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_schema_fact_user_group_map

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

# CELL ********************

%run nb_schema_dim_service

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Amending Column Names for Specific Assets
# ---
# If you need to amend or override the column names for specific assets, you can do so by updating the **column_overrides** dictionary below. This allows you to specify custom columns for any asset.
# 
# Instructions:
# - For any asset where you want to amend the columns, add an entry to the column_overrides dictionary.
# - The key should be the asset_name (e.g., 'dim_application'). This should be the exact same name as defined in the live_assets variable above.
# - The value should be a list of column names you want to include for that asset. For example, if dim_application should only have the column names 'ApplicationKey', 'Name', 'ApplicationType', then the column_overrides dict will be:
# column_overrides = {
#     'dim_application': ['ApplicationKey', 'Name', 'ApplicationType',]
# }


# CELL ********************

# Define any column overrides for specific assets as defined in the example above. 
# Selecting all columns by default
column_overrides = {}

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Loop through each asset in live_assets
for asset_name in live_assets:
    # Find the asset_info in all_asset_infos based on the asset_name
    asset_info = next((info for info in all_asset_infos if info['name'] == asset_name), None)
    if asset_info is None:
        print(f"Asset {asset_name} not found in dimensions")
        continue
    
    schema_version = asset_info['schema_version']
    table_name = f"{asset_name}_sv_{schema_version}"
    
    # Get the schema variable name
    schema_var_name = f"schema_{asset_name}_v{schema_version}"
    
    schema = globals().get(schema_var_name)
    
    if schema is None:
        print(f"Schema {schema_var_name} not found")
        continue
    
    # Get the column names
    if asset_name in column_overrides:
        # Use the overridden columns
        column_names = column_overrides[asset_name]
        print(f"Using overridden columns for {asset_name}: {column_names}")
    else:
        # Use the columns from the schema
        column_names = [field['field'] for field in schema]
    
    # Build the SELECT clause
    select_clause = ', '.join(column_names)

    # Add to the table_column_map
    table_column_map[table_name] = select_clause

    # Add to live_table_names
    live_table_names.append(table_name)

# Prepare the outputs
outputs = {
    'table_column_map': table_column_map,
    'live_table_names': live_table_names
}

# Output the parameters so that they can be called in ADF Run Activity
mssparkutils.notebook.exit(json.dumps(outputs))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
