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

# #### Generate Conformed - Dim App Classification
# ---
# Notebook to perform the creation of Dim App Classification, storing the table in the Conformed Lakehouse as delta format
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

%run nb_schema_dim_app_classification

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

table_name = 'dim_app_classification'
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
# Transform BusinessCapability data
df_business_capability = df_dicts['BusinessCapability'] \
  .filter((F.col('Name').isNotNull()) | (F.col('Name') != '')) \
  .withColumn('ClassificationType', F.col('Type')) \
  .transform(lambda df: conformed_select_alias_and_cast(df, target_schema, 'BusinessCapability', 'before')) \
  .transform(lambda df: add_hash_key(df, 'AppClassificationKey', ['ClassificationType', 'Name'], globals()['lean_ix']['name']))

# Transform DataObject data
df_data_object = df_dicts['DataObject'] \
  .filter((F.col('Name').isNotNull()) | (F.col('Name') != '')) \
  .withColumn('ClassificationType', F.col('Type')) \
  .transform(lambda df: conformed_select_alias_and_cast(df, target_schema, 'DataObject', 'before')) \
  .transform(lambda df: add_hash_key(df, 'AppClassificationKey', ['ClassificationType', 'Name'], globals()['lean_ix']['name']))

# Transform ITComponent data
df_it_component = df_dicts['ITComponent'] \
  .filter((F.col('Name').isNotNull()) | (F.col('Name') != '')) \
  .withColumn('ClassificationType', F.col('Type')) \
  .transform(lambda df: conformed_select_alias_and_cast(df, target_schema, 'ITComponent', 'before')) \
  .transform(lambda df: add_hash_key(df, 'AppClassificationKey', ['ClassificationType', 'DisplayName'], globals()['lean_ix']['name'])) \
  .transform(lambda df: add_vendor_hash_key(df, 'SupplierKey', ['ITComponentVendor'], globals()['lean_ix']['name'])) \
  
# Common transformations for hierarchy levels
def add_hierarchy_levels(df):
  return df \
      .withColumn('SplitArray', F.split('DisplayName', ' / ')) \
      .withColumn('HierarchyLevel1', F.when(F.size(F.col('SplitArray')) > 0, F.col('SplitArray').getItem(0)).otherwise(None)) \
      .withColumn('HierarchyLevel2', F.when(F.size(F.col('SplitArray')) > 1, F.col('SplitArray').getItem(1)).otherwise(None)) \
      .withColumn('HierarchyLevel3', F.when(F.size(F.col('SplitArray')) > 2, F.col('SplitArray').getItem(2)).otherwise(None)) \
      .withColumn('HierarchyLevel4', F.when(F.size(F.col('SplitArray')) > 3, F.col('SplitArray').getItem(3)).otherwise(None))

# Apply common transformations and union
df = df_business_capability \
  .transform(add_hierarchy_levels) \
  .unionByName(
      df_data_object.transform(add_hierarchy_levels),
      allowMissingColumns=True
  ) \
  .unionByName(
      df_it_component.transform(add_hierarchy_levels),
      allowMissingColumns=True
  )

# Drop the SplitArray column (used in hierarchy creation)
df = df.drop('SplitArray')

# Add attributes hash
attributes = [f['field'] for f in target_schema if f['field'] not in metadata_fields + [primary_key]]
df = df.transform(lambda df: add_hash_key(df, attributes_key, attributes)) 

##### ADDITIONAL CLEANUP TRANSFORMATION AFTER UNION #####
# List of columns that need bracket removal
bracket_columns = ['LinkedApplications', 'ITComponentVendor', 'ITComponentTechCategories', 'ITComponentHostingType']

# Apply bracket removal to specified columns
for col in bracket_columns:
  if col in df.columns:
      df = df.withColumn(col, 
          F.when(F.col(col).isNotNull(),
              F.translate(F.col(col), '[]', '')  # Remove square brackets using translate
          ).otherwise(None)
      )

##### END TRANSFORMATION #####

##### START PRIVACY #####
df,df_privacy = handle_personal_and_sensitive_fields(df, target_schema, primary_key)
##### END PRIVACY ######  

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
