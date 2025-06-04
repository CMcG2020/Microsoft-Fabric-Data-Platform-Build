# Fabric notebook source# 
# NOTE: This is an anonymized example with client data and IDs replaced with generic placeholders
# Original company-specific references have been generalized for demonstration purposes
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
# META       "workspaceId": "yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy"
# META     }
# META   }
# META }

# MARKDOWN ********************

# #### Generate Cleansed - Enterprise Architecture Tool
# ---
# Generic notebook to perform cleansing / enriching activities for Enterprise Architecture Tool data derived from the `Sourced` Lakehouse, before storing the cleansed / enriched data within the `Cleansed` Lakehouse as parquet format
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

%run nb_schema_sourced_enterprise_arch

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
# - Extract nested schema

# CELL ********************

global_configs = globals()['global_configs']
source_configs = globals()['enterprise_arch']
table_config = source_configs['source_tables'][table_name]

schema = globals()[f"schema_{table_name}_v{table_config['schema_version']}"]
unnested_schema = expand_nested_schema(schema)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ###### **<u>Step 4: Define extraction functions for nested fields</u>**
# - These are defined specifically within this notebook given these will only be used within the cleansed layer for Enterprise Architecture data. 

# CELL ********************

def extract_lifecycle_fields(df: DataFrame) -> DataFrame:
    """Extract lifecycle fields for Enterprise Architecture data sources."""
    lifecycle_schema = StructType([
            StructField("asString", StringType(), True),
            StructField("phases", ArrayType(StructType([
                StructField("phase", StringType(), True), 
                StructField("startDate", StringType(), True)])), True)
                ])

    return df \
            .withColumn('lifecycle', F.from_json(F.col('lifecycle'), lifecycle_schema)) \
            .withColumn('LifecycleAsString', F.col('lifecycle.asString')) \
            .withColumn("LifecyclePlan", F.coalesce(F.expr("filter(lifecycle.phases, x -> x.phase == 'plan')")[0]['startDate'], F.lit(None))) \
            .withColumn("LifecyclePhaseIn", F.coalesce(F.expr("filter(lifecycle.phases, x -> x.phase == 'phaseIn')")[0]['startDate'], F.lit(None))) \
            .withColumn("LifecycleActive", F.coalesce(F.expr("filter(lifecycle.phases, x -> x.phase == 'active')")[0]['startDate'], F.lit(None))) \
            .withColumn("LifecyclePhaseOut", F.coalesce(F.expr("filter(lifecycle.phases, x -> x.phase == 'phaseOut')")[0]['startDate'], F.lit(None))) \
            .withColumn("LifecycleEndOfLife", F.coalesce(F.expr("filter(lifecycle.phases, x -> x.phase == 'endOfLife')")[0]['startDate'], F.lit(None))) \
            .drop('lifecycle')


def extract_tags_fields(df: DataFrame) -> DataFrame:
    """Extract tags fields for Enterprise Architecture data sources."""
    tag_schema = ArrayType(
        StructType([
            StructField('name', StringType()),
            StructField('tagGroup', StructType([StructField('name', StringType())]))
            ])
        )

    return df \
            .withColumn('tags', F.from_json(F.col('tags'), tag_schema)) \
            .withColumn("TagsInstanceType", F.coalesce(F.expr("filter(tags, x -> x.tagGroup.name == 'Instance Type')")[0]['name'], F.lit(None))) \
            .withColumn("TagsImportantApplication", F.coalesce(F.expr("filter(tags, x -> x.tagGroup.name == 'Important Application')")[0]['name'], F.lit(None))) \
            .withColumn("TagsDivestedTo", F.coalesce(F.expr("filter(tags, x -> x.tagGroup.name == 'Divested To')")[0]['name'], F.lit(None))) \
            .withColumn("TagsM&AStatus", F.coalesce(F.expr("filter(tags, x -> x.tagGroup.name == 'M&A Status')")[0]['name'], F.lit(None))) \
            .withColumn("TagsWebsitePurpose", F.coalesce(F.expr("filter(tags, x -> x.tagGroup.name == 'Website Purpose')")[0]['name'], F.lit(None))) \
            .withColumn("TagsEventArchitectures", F.coalesce(F.expr("filter(tags, x -> x.tagGroup.name == 'Event Architectures')")[0]['name'], F.lit(None))) \
            .withColumn("TagsPaymentChannel", F.coalesce(F.expr("filter(tags, x -> x.tagGroup.name == 'Payment Channel')")[0]['name'], F.lit(None))) \
            .withColumn("TagsHRIntegrationType", F.coalesce(F.expr("filter(tags, x -> x.tagGroup.name == 'HR Integration Type')")[0]['name'], F.lit(None))) \
            .withColumn("TagsApplicationType", F.coalesce(F.expr("filter(tags, x -> x.tagGroup.name == 'Application Type')")[0]['name'], F.lit(None))) \
            .withColumn("TagsCompanyBusinessCriticality", F.coalesce(F.expr("filter(tags, x -> x.tagGroup.name == 'Company Business Criticality')")[0]['name'], F.lit(None))) \
            .withColumn("TagsM&AAcquisitionSource", F.coalesce(F.expr("filter(tags, x -> x.tagGroup.name == 'M&A Acquisition Source')")[0]['name'], F.lit(None))) \
            .withColumn("TagsWebsitePlatform", F.coalesce(F.expr("filter(tags, x -> x.tagGroup.name == 'Website Platform')")[0]['name'], F.lit(None))) \
            .withColumn("TagsDivisionCreatedCapability", F.coalesce(F.expr("filter(tags, x -> x.tagGroup.name == 'Division Created Capability')")[0]['name'], F.lit(None))) \
            .withColumn("TagsDataObjectType", F.coalesce(F.expr("filter(tags, x -> x.tagGroup.name == 'Data Object Type')")[0]['name'], F.lit(None))) \
            .withColumn("TagsInterfaceType", F.coalesce(F.expr("filter(tags, x -> x.tagGroup.name == 'Interface Type')")[0]['name'], F.lit(None))) \
            .withColumn("TagsHostingType", F.coalesce(F.expr("filter(tags, x -> x.tagGroup.name == 'Hosting Type')")[0]['name'], F.lit(None))) \
            .withColumn("TagsLocation", F.coalesce(F.expr("filter(tags, x -> x.tagGroup.name == 'Location')")[0]['name'], F.lit(None))) \
            .withColumn("TagsUserGroupType", F.coalesce(F.expr("filter(tags, x -> x.tagGroup.name == 'User Group Type')")[0]['name'], F.lit(None))) \
            .withColumn("TagsOtherTags", F.coalesce(F.expr("filter(tags, x -> x.tagGroup.name == 'Other Tags')")[0]['name'], F.lit(None))) \
            .drop('tags')


def extract_subscription_emails(df: DataFrame) -> DataFrame:
    """Extract subscription emails for Enterprise Architecture data sources. """
    subscriptions_schema = StructType([
        StructField("edges", ArrayType(StructType([
            StructField("node", StructType([
                StructField("type", StringType(), True),
                StructField("roles", ArrayType(StructType([
                    StructField("name", StringType(), True)])), True),
                StructField("user", StructType([
                    StructField("email", StringType(), True)
                ]), True)
            ]), True)
        ])), True)
    ])

    types = ['OBSERVER', 'ACCOUNTABLE', 'RESPONSIBLE']
    roles = [None, 'Application Owner', 'Business Owner', 'Data Owner', 'Data Steward', 'Enterprise Architect', 'Interface Owner', 'Subscriber 1', 'SystemOwner']

    df = df.withColumn('subscriptions', F.from_json(F.col('subscriptions'), subscriptions_schema))

    for t in types:
        for r in roles:
            field_name = ''.join(['Subscriptions', t.lower().capitalize(), r.replace(' ', '') if r else ''])
            if r:
                condition = f"""TRANSFORM(FILTER(subscriptions.edges, x -> x.node.type = '{t}' AND EXISTS(x.node.roles, r -> r.name = '{r}')), x -> x.node.user.email)"""
            else:
                condition = f"""TRANSFORM(FILTER(subscriptions.edges, x -> x.node.type = '{t}'), x -> x.node.user.email)"""
            df = df.withColumn(field_name, F.expr(condition))
    
    return df.drop('subscriptions')


def extract_relationship_names(df: DataFrame) -> DataFrame:
    """Extract relationship names for Enterprise Architecture data sources."""
    relationship_schema = StructType([
    StructField("edges", ArrayType(StructType([
        StructField("node", StructType([
            StructField("factSheet", StructType([
                StructField("name", StringType(), True)
            ]), True)
        ]), True)
    ])), True)
    ])
    pattern = re.compile(r'^rel[A-Z]')
    matching_columns = [col for col in df.columns if pattern.match(col)]

    for col in matching_columns:
        df = df \
            .withColumn(col, F.from_json(F.col(col), relationship_schema)) \
            .withColumn(col, F.expr(f"transform({col}.edges, x -> x.node.factSheet.name)")) \
            .withColumnRenamed(col, col.capitalize())
    
    return df

def extract_completion_value(df: DataFrame) -> DataFrame:
    """Extract the completion value from a JSON-like structure and convert it to Decimal(3,2)."""
    completion_schema = StructType([
        StructField("completion", FloatType(), True) 
    ])

    return df \
        .withColumn('completion_data', F.from_json(F.col('Completion'), completion_schema)) \
        .withColumn('Completion', F.col('completion_data.completion').cast(DecimalType(3, 2))) \
        .drop('completion_data')


def extract_location_fields(df: DataFrame) -> DataFrame:
  """Extract location fields for Enterprise Architecture data sources."""
  location_schema = StructType([
      StructField("geoAddress", StringType(), True)
  ])
  
  return df \
      .withColumn('Location', F.from_json(F.col('Location'), location_schema)) \
      .withColumn('GeoAddress', F.col('Location.geoAddress')) \
      .drop('Location')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Main Code Block
# ---
# ###### **<u>Step 5: Perform ETL</u>**
# - read parquet files as dataframe
# - flatten out nested fields
# - select fields, rename to PascalCase and cast to datatypes defined within DLM
# - add metadata fields
# - write to Cleansed Lakehouse


# CELL ********************

# read data from the Sourced Lakehouse
sourced_df = read_dataframe(global_configs['sourced_lh_name'], source_configs['name'], table_name, table_config['schema_version'], trigger_time).select(*extact_required_fields(schema, table_name, 'from'))

# unpack single nested fields
single_nested_fields = [f['from'] for f in schema if 'nested' in f.keys() and f['nested']['gql_string'].count('{') == 1]
for f in single_nested_fields:
    cleansed_df = sourced_df \
        .transform(lambda sourced_df: get_json_object(sourced_df, f, [f])) \
        .withColumnRenamed(f, f.capitalize())

# Check if 'lifecycle' field exists before extracting lifecycle fields
if 'lifecycle' in sourced_df.columns:
    cleansed_df = cleansed_df.transform(lambda df: extract_lifecycle_fields(df))

# Check for relationship fields starting with 'rel' before extracting relationship names
if any(col.startswith('rel') for col in sourced_df.columns):
    cleansed_df = cleansed_df.transform(lambda df: extract_relationship_names(df))

# Check if 'tags' field exists before extracting tags fields
if 'tags' in sourced_df.columns:
    cleansed_df = cleansed_df.transform(lambda df: extract_tags_fields(df))

# Check if 'subscriptions' field exists before extracting subscription emails
if 'subscriptions' in sourced_df.columns:
    cleansed_df = cleansed_df.transform(lambda df: extract_subscription_emails(df))

# Check if 'subscriptions' field exists before extracting subscription emails
if 'completion' in sourced_df.columns:
    cleansed_df = cleansed_df.transform(lambda df: extract_completion_value(df))

# Check if 'location' field exists before extracting location fields
if 'location' in sourced_df.columns:
    cleansed_df = cleansed_df.transform(lambda df: extract_location_fields(df))

# select relevant fields / rename to Pascal / cast to datatypes / add metadata / cap timestamp fields
cleansed_df = cleansed_df \
    .withColumn('Status', F.when(F.col('Status').rlike('(?i)^ACTIVE$'), True).otherwise(False)) \
    .select([F.col(c['from']).alias(c['to']).cast(c['dataType']) for c in unnested_schema]) \
    .transform(lambda df: add_pipeline_metadata(df, trigger_time, trigger_time, source_configs['name'], table_name)) \
    .transform(lambda df: cap_timestamp_fields(df)) \
    .transform(lambda df: cleansed_type_conversion(df, unnested_schema, 'to'))

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

# - [Check the Data Quality Checks Wiki for info on running DQ checks](https://company.visualstudio.com/Project/_wiki/wikis/Project.wiki/38/Running-Data-Quality-Checks).
# CELL ********************

%run nb_helper_functions_data_quality

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#execute write if df is not empty
if cleansed_df is not None and cleansed_df.head(1):
    execute_write_to_lakehouse_with_dq_checks(df=cleansed_df, layer='Cleansed', write_mode_cleansed = None)
else: 
    print("No sourced data found for table {table_name}, no dq checks executed")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
