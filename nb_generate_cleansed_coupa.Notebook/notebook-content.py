# Fabric notebook source# 
# ANONYMIZED EXAMPLE - Client-specific data has been anonymized for demonstration purposes
# This notebook shows a generic pattern for data cleansing and transformation in Microsoft Fabric
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
# META       "environmentId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
# META       "workspaceId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
# META     }
# META   }
# META }

# MARKDOWN ********************

# #### Generate Cleansed - ERP System
# ---
# Generic notebook to perform cleansing / enriching activities for ERP system data derived from the `Sourced` Lakehouse, before storing the cleansed / enriched data within the `Cleansed` Lakehouse as parquet format.
# 
# 
# ###### **<u>Step 1: Import common libraries and helper functions</u>**
# 
# - Import any required public libraries and custom functions via `%run` magic command. 
# - For custom functions, import the `nb_helper_functions_parent_caller.py` notebook to collectively bring in all the required custom functions.

# CELL ********************

%run nb_helper_functions_parent_caller

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_schema_sourced_erp_system

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
table_name = None

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

global_configs = globals()['global_configs']
source_configs = globals()['erp_system']
table_config = source_configs['source_tables'][table_name]
schema = globals()[f"schema_{table_name}_v{table_config['schema_version']}"]
unnested_schema = expand_nested_schema(schema)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ###### **<u>Step 4: Define functions specifically for ERP system cleansing</u>**
# - Define common functions to be used for cleansing ERP system sourced tables

# CELL ********************

def extract_address(df: DataFrame) -> DataFrame:
    """Function to extract address from relevant fields.""" 
    address_schema = StructType([
    """
    Function to extract and concatenate address components from JSON fields.
    
    This function demonstrates how to:
    - Parse JSON strings into structured data
    - Handle both single address objects and arrays of addresses
    - Transform nested data into flat string representations
    - Use regex patterns to identify relevant columns dynamically
    
    Args:
        df: Input DataFrame containing address fields in JSON format
        
    Returns:
        DataFrame with address fields converted to concatenated strings
    """ 
        StructField("street2", StringType(), True),
        StructField("street3", StringType(), True),
        StructField("street4", StringType(), True),
        StructField("city", StringType(), True),
        StructField("state", StringType(), True),
        StructField("postal-code", StringType(), True)
    ])

    pattern = re.compile(r'.*\baddress(es)?\b.*', re.IGNORECASE)
    matching_columns = [col for col in df.columns if pattern.search(col)]

    for col in matching_columns:
        df = df.withColumn(col, F.regexp_replace(F.col(col), 'None', 'null'))

        if col == 'vendor-addresses':
            # Handle vendor-addresses as an array
            array_address_schema = ArrayType(address_schema)
            df = df \
                .withColumn(col, F.from_json(F.col(col), array_address_schema)) \
                .withColumn(col, F.expr(f"""
                    transform(`{col}`, x -> 
                        concat_ws(' ', 
                            x.street1, 
                            x.street2, 
                            x.street3, 
                            x.street4, 
                            x.city, 
                            x.state, 
                            x['postal-code']
                        )
                    )
                """))
        else:
            # Handle single address objects (like primary-address)
            df = df \
                .withColumn(col, F.from_json(F.col(col), address_schema)) \
                .withColumn(col, F.concat_ws(" ", 
                    F.col(col).getItem('street1'),
                    F.col(col).getItem('street2'),
                    F.col(col).getItem('street3'),
                    F.col(col).getItem('street4'),
                    F.col(col).getItem('city'),
                    F.col(col).getItem('state'),
                    F.col(col).getItem('postal-code')))

    return df
    

def extract_array_fields(df: DataFrame, field: dict) -> DataFrame:
    """Function to extract values from array fields - only single nested supported."""
    nested_field = field['nested']['sub_fields'][0]['name']
    """
    Function to extract values from array fields with single-level nesting.
    
    This demonstrates how to:
    - Parse JSON arrays into Spark array types
    - Extract specific nested fields from array elements
    - Filter out null values from the resulting arrays
    - Handle different array structures based on field configuration
    
    Args:
        df: Input DataFrame
        field: Dictionary containing field configuration with nested structure info
        
    Returns:
        DataFrame with array fields processed and flattened
    """
    schema = ArrayType(StructType([StructField(nested_field, StringType(), True)]))

    multi_nested_array = ['remit-to-addresses', 'primary-address', 'vendor-addresses']
    if field['from'] not in multi_nested_array:
        return df \
            .withColumn(field['from'], F.regexp_replace(F.col(field['from']), 'None', 'null')) \
            .withColumn(field['from'], F.from_json(F.col(field['from']), schema)) \
            .withColumn(field['from'], F.expr(f"""filter(transform(`{field['from']}`, x -> CASE WHEN x.`{nested_field}` != 'null' THEN x.`{nested_field}` ELSE NULL END), x -> x IS NOT NULL)"""))
    else:
        return df


def extract_custom_fields(df: DataFrame, schema: list) -> DataFrame:
    """Function to extract sub fields from nested field - 'custom-fields'"""

    """
    Function to extract and flatten custom fields from JSON structure.
    
    This function shows how to:
    - Parse complex nested JSON structures
    - Handle dynamic field extraction based on schema configuration
    - Clean and normalize JSON strings (handle Python boolean/None values)
    - Create new columns for each custom field
    - Support both simple and nested custom field structures
    
    Args:
        df: Input DataFrame containing 'custom-fields' JSON column
        schema: List of field configurations defining the expected structure
        
    Returns:
        DataFrame with custom fields extracted as individual columns
    """
    custom_fields_schema = next((row for row in schema if row['from'] == 'custom-fields'), None)

    # if not custom_fields_schema, return the original DataFrame
    if not custom_fields_schema:
        return df

    # perform necessary transformations on 'custom-fields' to ensure valid JSON formatting
    replacements = {"True": "true", "False": "false", "None": "null"}
    for old_val, new_val in replacements.items():
        df = df.withColumn('custom-fields', F.regexp_replace('custom-fields', old_val, new_val))


    # extract and populate the fields based on the custom schema
    for sub_field in custom_fields_schema['nested']['sub_fields']:
        field_name = sub_field['name']
        col_name = f"custom-fields-{field_name}"
        if not sub_field.get('nested'):
            df = df.withColumn(col_name, F.coalesce(F.get_json_object(F.col('custom-fields'), f"$.{field_name}"), F.lit(None)))
        else:
            nested_field_name = sub_field['nested']['sub_fields'][0]['name']
            df = df.withColumn(col_name, F.get_json_object(F.get_json_object(F.col('custom-fields'), f"$.{field_name}"), f"$.{nested_field_name}"))

    return df

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Main Code Block
# ---
# ###### **<u>Step 4: Perform ETL</u>**
# - read parquet files as dataframe
# ###### **<u>Step 5: Perform ETL Pipeline</u>**
# This section demonstrates a typical ETL pattern for data cleansing:
# - Read parquet files as dataframe from source lakehouse
# - Add fields not present in target schema (handles schema evolution across environments)
# - Extract values from nested JSON columns
# - De-duplicate rows and handle data quality
# - Transform field names to target naming convention (PascalCase)
# - Cast to target datatypes defined in schema
# - Add pipeline metadata for lineage tracking
# - Perform Data Quality (DQ) checks before writing
# - Write to target lakehouse only if DQ checks succeed
# CELL ********************

# read data from the Sourced Lakehouse
cleansed_df = read_dataframe(global_configs['sourced_lh_name'], source_configs['name'], table_name, table_config['schema_version'], trigger_time)
# MAIN ETL PIPELINE EXECUTION
# This section demonstrates the complete ETL pipeline execution pattern:

# Step 1: Read source data from lakehouse
# create new df in the event no missing fields are added
cleansed_df = cleansed_df.select(*extact_required_fields(schema, table_name, 'from'))
# Step 2: Ensure all required fields exist (schema evolution handling)
# add missing fields
for field in schema:
# Step 3: Add missing fields with null values to match target schema not in cleansed_df.columns:
        cleansed_df = cleansed_df.withColumn(field['from'], F.lit(None))
        print(f"Field {field['from']} not found. Adding to df")

# un-nest single nested field
for field in schema:
# Step 4: Extract values from single-nested JSON fieldsnd field['dataType'] != ArrayType(StringType())):
        if len(field['nested']['sub_fields']) == 1:
            from_field = field['from']
            sub_field = field['nested']['sub_fields'][0]['name']
            cleansed_df = cleansed_df.withColumn(from_field, F.coalesce(F.get_json_object(F.col(from_field), f'$.{sub_field}'), F.lit(None)))

        else:

            if field['from'] not in ['custom-fields', 'primary-address']:
                         # Handle multi-field nested objects by creating separate columns                    from_field = f"{field['from']}-{sub_field['name']}"
                    sub_field = sub_field["name"]
                    cleansed_df = cleansed_df.withColumn(from_field, F.coalesce(F.get_json_object(F.col(field['from']), f'$.{sub_field}'), F.lit(None)))
            
                cleansed_df = cleansed_df.drop(field['from'])

# unpack array fields
for field in schema:
# Step 5: Process array fields using custom transformatione'] == ArrayType(StringType()):
        cleansed_df = cleansed_df.transform(lambda cleansed_df: extract_array_fields(cleansed_df, field))

# extract custom fields
cleansed_df = extract_custom_fields(cleansed_df, schema)
# Step 6: Extract custom fields from JSON structure
# concat address fields
cleansed_df = cleansed_df.transform(lambda cleansed_df: extract_address(cleansed_df))
# Step 7: Process address fields by concatenating components
# select relevant fields / rename to Pascal / cast to datatypes / add metadata
cleansed_df = cleansed_df \
# Step 8: Final transformations - select, rename, cast, and add metadatasted_schema]) \
    .transform(lambda cleansed_df: add_pipeline_metadata(cleansed_df, trigger_time, trigger_time, source_configs['name'], table_name)) \
    .transform(lambda cleansed_df: cap_timestamp_fields(cleansed_df)) \
    .transform(lambda cleansed_df: cleansed_type_conversion(cleansed_df, unnested_schema, 'to'))

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

#execute write if df is not
# DATA QUALITY CHECKS AND CONDITIONAL WRITE
# This demonstrates a pattern for ensuring data quality before persisting data:
# - Only write data if the DataFrame is not empty and contains valid records
# - Execute comprehensive data quality checks before writing to target
# - Provide clear logging when no data is available for processingif cleansed_df is not None and cleansed_df.head(1):
    execute_write_to_lakehouse_with_dq_checks(df=cleansed_df, layer='Cleansed', write_mode_cleansed = None)
else: 
    print("No sourced data found for table {table_name}, no dq checks executed")

    print(f"No sourced data found for table {table_name}, no dq checks executed")

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
