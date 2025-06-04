# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# #### Helper Functions
# ---
# To host common functions to support the activities relating to struct schema generation and type conversions


# CELL ********************

def add_hash_key(df: DataFrame, key_name: str, key_columns: list[str], static_value: str = '') -> DataFrame:
    """Add a key to the dataframe using xxhash64."""
    return df \
        .withColumn('hash_col', F.concat_ws('', *[F.coalesce(col) for col in key_columns])) \
        .withColumn('hash_col', F.when(F.col('hash_col') == '', F.lit(None)).otherwise(F.concat_ws('', *[F.col('hash_col'), F.lit(static_value)]))) \
        .withColumn(key_name, F.when(F.col('hash_col').isNotNull(), F.xxhash64(F.col('hash_col'))).otherwise(F.lit(None))) \
        .drop('hash_col')  

def add_vendor_hash_key(df: DataFrame, key_name: str, key_columns: list[str], static_value: str = '') -> DataFrame:  
    """Add a key to the dataframe using xxhash64 with special handling for ITComponentVendor."""  
    processed_columns = []  

    for col in key_columns:  
        if col == 'ITComponentVendor':  
            # Special handling for ITComponentVendor - extract part after '/'  
            processed_column = F.when(  
                F.col(col).contains('/'),  
                F.split(F.col(col), '/').getItem(1)  
            ).otherwise(F.col(col))  
        else:  
            processed_column = F.col(col)  

        processed_columns.append(F.coalesce(processed_column, F.lit('')))  

    return df \
        .withColumn('hash_col', F.concat_ws('', *processed_columns)) \
        .withColumn('hash_col', F.when(F.col('hash_col') == '', F.lit(None))  
                    .otherwise(F.concat_ws('', F.col('hash_col'), F.lit(static_value)))) \
        .withColumn(key_name, F.when(F.col('hash_col').isNotNull(), F.xxhash64(F.col('hash_col')))  
                    .otherwise(F.lit(None))) \
        .drop('hash_col')  


def transform_time_to_minutes(input_df, time_column="time_string", output_column="total_minutes"):
    """Function to transform time_string into total_minutes"""

    # Define regex patterns for days, hours, and minutes
    day_pattern = r"(\d+)\s*Day"
    hour_pattern = r"(\d+)\s*Hour"
    minute_pattern = r"(\d+)\s*Minute"
    
    # Extract and coalesce each component
    days = F.coalesce(F.regexp_extract(F.col(time_column), day_pattern, 1).cast("int"), F.lit(0))
    hours = F.coalesce(F.regexp_extract(F.col(time_column), hour_pattern, 1).cast("int"), F.lit(0))
    minutes = F.coalesce(F.regexp_extract(F.col(time_column), minute_pattern, 1).cast("int"), F.lit(0))
    
    # Compute total minutes and apply cast at the column level
    total_minutes = (days * 1440 + hours * 60 + minutes).cast("int")
    
    # Add the total_minutes column to the DataFrame
    transformed_df = input_df.withColumn(output_column, total_minutes)
    
    return transformed_df


def deduplicate_by_keys(df: DataFrame, keys: list[str], order_by: list[str], rank: str = 'desc') -> DataFrame:
    """Deduplicate a DataFrame based on a given set of keys."""
    if rank == 'desc':
        order_columns = [F.col(col).desc() for col in order_by]
    else:
        order_columns = [F.col(col).asc() for col in order_by]

    window_spec = Window.partitionBy(*keys).orderBy(*order_columns)

    return df \
        .withColumn('row_number', F.row_number().over(window_spec)) \
        .where(F.col('row_number') == 1) \
        .drop(F.col('row_number'))


def add_pipeline_metadata(df: DataFrame, receipt_date: str, allocated_date: str, source_system: str, table_name: str) -> DataFrame:
    """Adds metadata columns to the given DataFrame."""
    try:
        receipt_date_parsed = F.to_date(F.lit(receipt_date))
    except Exception as e:
        raise ValueError(f"Invalid `receipt_date` format: {receipt_date}. Expected format is 'yyyy-MM-dd'. Error: {e}")

    allocated_date_col = F.to_date(F.lit(allocated_date)) if allocated_date else receipt_date_parsed

    return df \
        .withColumn('TableName', F.lit(table_name)) \
        .withColumn("ReceiptDate", receipt_date_parsed) \
        .withColumn("AllocatedDate", allocated_date_col) \
        .withColumn("PipelineUpdatedDate", receipt_date_parsed) \
        .withColumn("SourceSystem", F.lit(source_system))


def get_json_object(df: DataFrame, value: str, columns: list = None):
    """
    Replace dataframe field with a specific value from JSON objects in specified columns or all columns if none are specified.
    Only extracts values at one level of nestedness within the JSON object.
    """
    columns_to_process = columns if columns else df.columns
        
    for k in columns_to_process:
        df = df.withColumn(k, F.coalesce(F.get_json_object(F.col(k), f'$.{value}'), F.lit(None)))
    
    return df


def fill_unknown_columns(df: DataFrame, excluded_fields: List[str]) -> DataFrame:
  """
  Function to fill columns with default values after harmonisation process.
  
  Args:
  df (DataFrame): Input DataFrame
  excluded_fields (List[str]): List of column names to be excluded from filling
  
  Returns:
  DataFrame: DataFrame with filled values
  """
  for field in df.columns:
      # Skip excluded fields, IsMaster, and MasteredDate columns
      if field in excluded_fields or field in ['IsMaster', 'MasteredDate']:
          continue
      
      # Get the data type of the column
      data_type = df.schema[field].dataType
      
      # Check the data type and fill accordingly
      if isinstance(data_type, StringType):
          df = df.withColumn(field, F.lit('UNKNOWN'))
      elif isinstance(data_type, (IntegerType, FloatType)):
          df = df.withColumn(field, F.lit(0))
      elif isinstance(data_type, DecimalType):
          # Handle DecimalType separately
          precision = data_type.precision
          scale = data_type.scale
          default_value = F.lit(0).cast(DecimalType(precision, scale))
          df = df.withColumn(field, F.lit(default_value))
      elif isinstance(data_type, DateType):
          df = df.withColumn(field, F.to_date(F.lit('1900-01-01')))
      elif isinstance(data_type, TimestampType):
          df = df.withColumn(field, F.to_timestamp(F.lit('1900-01-01')))
      elif isinstance(data_type, BooleanType):
          df = df.withColumn(field, F.lit(False))
      else:
          # Skip any other data types
          continue
  return df


def cap_timestamp_fields(df: DataFrame) -> DataFrame:
    """Cap timestamp fields to 1900-01-01. Anything before will throw errors when writing to parquet / delta."""
    threshold_date = "1900-01-01T00:00:00Z"
    for field in df.schema.fields:
        if isinstance(field.dataType, (TimestampType, DateType)):
            df = df.withColumn(field.name, F.when(F.col(field.name) < F.lit(threshold_date), F.lit(threshold_date).cast(field.dataType)).otherwise(F.col(field.name).cast(field.dataType)))
    return df


def duration_to_seconds(df: DataFrame, columns: list) -> DataFrame:
    """Convert a duration string to seconds."""
    regex_day = r"(\d+)\s+Days?"
    regex_hour = r"(\d+)\s+Hours?"
    regex_minute = r"(\d+)\s+Minutes?"
    regex_second = r"(\d+)\s+Seconds?"
    for f in columns:
        df = df \
            .withColumn("days", F.coalesce(F.regexp_extract(F.col(f), regex_day, 1) * 86400, F.lit(0))) \
            .withColumn("hours", F.coalesce(F.regexp_extract(F.col(f), regex_hour, 1) * 3600, F.lit(0))) \
            .withColumn("minutes", F.coalesce(F.regexp_extract(F.col(f), regex_minute, 1) * 60, F.lit(0))) \
            .withColumn("seconds", F.coalesce(F.regexp_extract(F.col(f), regex_second, 1) * 1, F.lit(0))) \
            .withColumn(f, F.col('days') + F.col('hours') + F.col('minutes') + F.col('seconds')) \
            .withColumn(f, F.col(f).cast(IntegerType()))
    
    return df

@F.udf(returnType=IntegerType())
def convert_duration_to_minutes(duration_str):
  """
  Converts a duration string to total minutes.
  
  Args:
      duration_str (str): A string representing duration in the format "X Days Y Hours Z Minutes".
  
  Returns:
      int: Total duration in minutes, or None if the input is invalid.
  
  Example:
      "1 Day 2 Hours 30 Minutes" -> 1590  # (1*24*60 + 2*60 + 30)
      "" -> None
  """
  try:
      total_minutes = 0
      if duration_str:
          parts = duration_str.split()
          for i in range(0, len(parts), 2):
              value = int(parts[i])
              unit = parts[i+1].lower()
              if 'day' in unit:
                  total_minutes += value * 24 * 60
              elif 'hour' in unit:
                  total_minutes += value * 60
              elif 'minute' in unit:
                  total_minutes += value
          return total_minutes
  except (ValueError, IndexError):
      pass
  
  if not duration_str:
      return None
  
  return None
    

def conformed_select_alias_and_cast(df: DataFrame, schema: list, table: str, phase: str = 'after') -> DataFrame:
  """Function to select, alias and cast a dataframe - only used for conformed layer given nature of schema."""
  table_fields = [field for field in schema if table in field['from']]
  new_schema = []
  
  for field in table_fields:
      if phase == 'after':
          # post all required transformation
          original = field['field'] if 'calculated_field' in field else field['from'][table]
          renamed = field['field']
      elif phase == 'before':
          # pre all required transformation
          original = field['from'][table]
          renamed = field['from'][table] if 'calculated_field' in field else field['field']
      else:
          raise ValueError(f'Unknown phase: {phase}')
      
      # Handle both single values and lists in the 'from' field
      if isinstance(original, list):
          # For fields that require multiple source columns
          # Skip them in the 'before' phase as they'll be handled separately
          if phase == 'before':
              continue
      else:
          record = {'field': renamed, 'from': original, 'dataType': field['dataType']}
          if record not in new_schema:
              new_schema.append(record)
  
  return df.select(*[F.col(f['from']).alias(f['field']).cast(f['dataType']) for f in new_schema])



def cleansed_type_conversion(df: DataFrame, schema: list, origin: str) -> DataFrame:
    """Function to select, alias, and cast a DataFrame based on the provided schema."""
    
    for field in schema:
        field_name = field[origin]  # Get the field name based on the origin
        if field_name in df.columns:  # Check if the field exists in the DataFrame
            if isinstance(field['dataType'], TimestampType):
                df = df.withColumn(field_name, F.to_timestamp(F.col(field_name), "dd-MM-yyyy HH:mm:ss"))
            elif isinstance(field['dataType'], DateType):
                df = df.withColumn(field_name, F.to_date(F.col(field_name), "dd-MM-yyyy"))
            elif isinstance(field['dataType'], StringType):
                df = df.withColumn(field_name, 
                                   F.when((F.col(field_name) == '') | 
                                          (F.col(field_name) == 'NULL') | 
                                          (F.col(field_name) == 'None'), 
                                          F.lit(None)).otherwise(F.col(field_name)))
            elif isinstance(field['dataType'], IntegerType):
                df = df.withColumn(field_name, 
                                   F.regexp_replace(F.col(field_name), ",", "").cast(IntegerType()))
            elif isinstance(field['dataType'], ArrayType):
                df = df.withColumn(field_name, 
                                   F.when((F.size(F.col(field_name)) == 0), F.lit(None)).otherwise(F.col(field_name)))
            elif isinstance(field['dataType'], FloatType):
                df = df.withColumn(field_name, 
                                   F.when(F.col(field_name).isNull() | 
                                           (F.col(field_name) == 'NULL') | 
                                           (F.col(field_name) == ''), 
                                           F.lit(None).cast(FloatType()))
                                   .otherwise(F.col(field_name).cast(FloatType())))
            
    return df


def retrieve_user_email_hash(main_df: DataFrame, user_df: DataFrame, personal_schema: list, table: str) -> DataFrame:
    """Common function used to extract emails and creates a hash for ServiceNow source tables."""
    for row in personal_schema:

        join_field = row['from'][table]

        main_df = main_df \
            .join(F.broadcast(user_df.withColumnRenamed('SysId', join_field)), join_field, 'left') \
            .withColumn(row['field'], F.coalesce('Email', join_field)) \
            .transform(lambda df: add_hash_key(df, row['field'], [row['field']])) \
            .drop(*['Email'])

    return main_df


def handle_personal_and_sensitive_fields(df: DataFrame, target_schema: list, primary_key: str, partition_fields: list = None):
    """Common function to handle personal and sensitive fields in Conformed."""
    personal_and_sensitive_fields = [row for row in target_schema if row['personal'] or row['sensitive']]
    df_privacy = None

    if personal_and_sensitive_fields:
        required_fields = set([primary_key, 'AttributesKey', 'TableName'] + [row['field'] for row in personal_and_sensitive_fields] + (partition_fields or []))
        df_privacy = df.select(*required_fields)

        for field in personal_and_sensitive_fields:
            df = df.withColumn(field['field'], F.lit(None).cast(field['dataType']))
    
    return df, df_privacy


def clean_and_explode_column(df, col_name):
    """Explodes an array column and applies a string cleaning transformation. Used in lean_ix builds currently
    example: input ['\"value1\"', '\"value2\"'] output value1, value2 """
    # Exploding the array column first
    exploded_df = df.withColumn(col_name, F.explode(F.col(col_name)))
    
    # Applying the regex transformation on the exploded column (to remove brackets if they exist)
    cleaned_df = exploded_df.withColumn(col_name, 
                                        F.trim(F.regexp_replace(F.col(col_name), r'^"(.*)"$', r'\1')))
    return cleaned_df

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def calculate_scd2_dates(df_cleansed, target_table_configs, current_date):
    """
    Processes the incoming DataFrame to manage Slowly Changing Dimensions Type 2 (SCD2).
    If StartDate and EndDate columns do not exist, they will be calculated according to SCD2 rules.

    Args:
        df_cleansed (DataFrame): Incoming DataFrame containing device information.
        target_table_configs (dict): Dictionary containing configuration values for active status,
                                      default end date, and column names for current status, end date,
                                      start date, and current indicator.

    Returns:
        DataFrame: A new DataFrame with updated records reflecting the current state of devices.
    """

    device_key_col = target_table_configs['scd2_partition_col']
    active_status = target_table_configs['scd2_active_status']
    default_end_date = target_table_configs['scd2_default_end_date']
    current_status_col = target_table_configs['scd2_current_status_col']
    end_date_col = target_table_configs['scd2_end_date_col']
    start_date_col = target_table_configs['scd2_start_date_col'] 

    print("Total Records in Cleansed Data:", df_cleansed.count())

    # Process Active Records
    df_active = df_cleansed.filter(F.col(current_status_col) == active_status) \
        .withColumn("IsCurrent", F.lit(True)) \
        .withColumn(end_date_col, F.to_date(F.lit(default_end_date), 'yyyy-MM-dd')) \
        .withColumn(start_date_col, F.to_date(F.lit(current_date), 'yyyy-MM-dd'))

    print("Active Records Count:", df_active.count())

    # Process Inactive Records
    df_inactive = df_cleansed.filter(F.col(current_status_col) != active_status) \
        .withColumn("IsCurrent", F.lit(False)) \
        .withColumn(end_date_col, F.to_date(F.lit(current_date), 'yyyy-MM-dd')) \
        .withColumn(start_date_col, F.to_date(F.lit(current_date), 'yyyy-MM-dd'))

    print("Inactive Records Count:", df_inactive.count())

    # Combine Active and Inactive Records
    df = df_active.unionByName(df_inactive)

    return df


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def create_empty_df_if_needed(schema, table_exists: bool):
    """
    Create an empty DataFrame with the specified schema if the table does not exist.

    Args:
        schema (list): A list of column names to define the schema of the empty DataFrame.
        table_exists (bool): A flag indicating whether the table exists.
    
    Returns:
        DataFrame: An empty DataFrame with the specified schema if the table does not exist;
                    Otherwise, returns a DataFrame (e.g. could be an existing one).
    """
    
    schema = StructType([StructField(field, StringType(), True) for field in schema])
    
    df = spark.createDataFrame([], schema)

    if not table_exists:
        print("Table does not exist; returning an empty DataFrame.")
    else:

        print("Table exists; returning an existing DataFrame.")
        
    return df

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def generate_AssignedDate_and_ReleasedDate(df_cleansed, device_key_col, user_key_col):
    """
    Computes AssignedDate and sets ReleasedDate as NULL for the given DataFrame.
    """
    # Assign AssignedDate to current date and ReleasedDate as NULL
    df_cleansed = df_cleansed.withColumn("AssignedDate", F.current_date()).withColumn("ReleasedDate", F.lit(None))

    return df_cleansed

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def reallocate_device_based_on_user(initial_df, new_data_df, device_key_col, user_key_col, assigned_date_col, release_date_col):
    """
    Processes device allocation data based on user reassignments by updating the release dates of devices when user keys change.

    This function merges two DataFrames: the initial allocation of devices and new allocation data. 
    It checks for any changes in user assignments for devices. If any devices are found to have been reassigned, 
    their release dates are updated accordingly. If the initial DataFrame is empty, it returns the new data without processing.

    Parameters:
    - initial_df (DataFrame): The initial DataFrame containing the current device assignments.
    - new_data_df (DataFrame): The new DataFrame containing updated device assignments.
    - device_key_col (str): The name of the column that uniquely identifies the devices.
    - user_key_col (str): The name of the column that identifies the users assigned to the devices.
    - assigned_date_col (str): The name of the column representing the date the device was assigned.
    - release_date_col (str): The name of the column representing the date the device was released.

    Returns:
    - DataFrame: A DataFrame containing updated device allocations with modified release dates 
                 for reassigned users. If the initial DataFrame is empty, returns new_data_df.

    Example Usage:
    >>> updated_devices_df = reallocate_device_based_on_user(initial_devices_df, new_devices_df,
    ...                                                      "DeviceKey", "UserKey", 
    ...                                                      "AssignedDate", "ReleasedDate")
    """
    
    # Check if the initial DataFrame is empty
    if initial_df.isEmpty():
        return new_data_df

    # Checking for reassignment by joining old and new data
    joined_df = initial_df.alias("old").join(new_data_df.alias("new"), 
        (col("old.DeviceKey") == col("new.DeviceKey")), "outer"
    ).select(
        col("old.DeviceKey").alias("DeviceKey"),
        col("old.UserKey").alias("OldUserKey"),
        col("new.UserKey").alias("NewUserKey"),
    )

    # Filter only those records where the user was reassigned
    reassigned_df = joined_df.filter(col("OldUserKey") != col("NewUserKey"))

    # Here we process only the reassigned records
    if reassigned_df.count() > 0:
        # Combine initial and new data with assigned and released dates only for reassigned entries
        combined_df = initial_df.union(new_data_df)
        
        # Define window specification to detect changes in UserKey
        window_spec = Window.partitionBy(device_key_col).orderBy(assigned_date_col)

        # Use lead to get the next UserKey for comparison
        combined_df = combined_df.withColumn("NextUserKey", F.lead(col(user_key_col)).over(window_spec))

        # Update ReleasedDate where UserKey changes only for reassigned records
        updated_df = combined_df.withColumn(
            release_date_col,
            F.when(col(user_key_col) != col("NextUserKey"), F.current_date().cast("string"))
            .otherwise(col(release_date_col))
        ).drop("NextUserKey")
        
        # Final logic to only keep active and reassigned records
        df = updated_df.filter(
            (col("AssignedDate").isNotNull()) | (col("ReleasedDate").isNotNull())
        )

        return df
    else:
        return initial_df

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def remove_null_or_empty_records(df: DataFrame, filter_col: str) -> (DataFrame, DataFrame):
    """
    Splits the DataFrame into two: one containing records with empty or null current_user,
    and the other containing the rest of the records.

    Args:
        df (DataFrame): Input DataFrame containing the current_user column.
        filter_col (str): The name of the column to check for empty or null values.

    Returns:
        (DataFrame, DataFrame): Two DataFrames, the first with empty/null current_user,
                                   the second with other records.
    """

    # Filter records with empty or null current_user
    df_empty_user = df.filter(F.col(filter_col).isNull() | (F.trim(F.col(filter_col)) == ''))

    # Filter records that do not have empty/null current_user
    df = df.filter(~(F.col(filter_col).isNull() | (F.trim(F.col(filter_col)) == '')))

    return df

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def execute_scd2_logic(df_cleansed, df_conformed, config, current_date):
    
    """
    Execute Slowly Changing Dimension Type 2 (SCD2) logic on the provided DataFrames.

    This function combines two DataFrames representing cleansed and conformed data, applies 
    SCD2 logic to manage the historical status of records based on specified configuration settings, 
    and returns a DataFrame containing the updated records with appropriate start and end dates.

    Parameters:
    ----------
    df_cleansed : DataFrame
        A Spark DataFrame containing cleansed records.

    df_conformed : DataFrame
        A Spark DataFrame containing conformed records.

    config : dict
        A configuration dictionary containing the following keys:
            - 'scd2_start_date_col': The name of the column to hold the start date for records.
            - 'scd2_end_date_col': The name of the column to hold the end date for records.
            - 'scd2_current_status_col': The name of the column holding the current status of the records.
            - 'scd2_partition_col': The name of the column to partition the DataFrame for processing.
            - 'scd2_order_col': The name of the column used for ordering records.
            - 'scd2_active_status': The status that indicates an active record (used for IsCurrent determination).
            - 'scd2_default_end_date': The default value for end dates to be used under certain conditions.

    Returns:
    -------
    DataFrame
        A Spark DataFrame with updated records that include correctly applied SCD2 logic, 
        representing the current status and historical changes based on the given configuration. 
        Returns None if an error occurs during processing.

    Raises:
    ------
    Exception
        Prints an error message if any exception occurs during the processing steps.
    """
    
    start_date_col = config['scd2_start_date_col']
    end_date_col = config['scd2_end_date_col']
    current_status_col = config['scd2_current_status_col']
    partition_col = config['scd2_partition_col']     
    order_col = config['scd2_order_col']

    try:
        # Combine cleansed and conformed dataframes
        df_union = df_cleansed.unionByName(df_conformed)
        
        # Create a window specification for ranking
        window_spec = Window.partitionBy(partition_col).orderBy(F.col(order_col).asc())

        # Add row numbers for ordering
        df_with_row_num = df_union.withColumn("row_num", F.row_number().over(window_spec))

        # Prepare to identify latest records
        df_latest = df_with_row_num.filter(F.col("row_num") == 1)

        # Join current records with previous statuses to determine changes
        df_with_status = df_with_row_num.join(
            df_latest.select(partition_col, F.col(current_status_col).alias("prev_" + current_status_col)),
            on=partition_col,
            how='left'
        ).fillna({'prev_' + current_status_col: 'New record'})

        # Update End Dates based on status changes
        df_updated = df_with_status.withColumn(
            end_date_col,
            F.when(F.col(current_status_col) != F.col("prev_" + current_status_col), current_date)
            .otherwise(F.col(end_date_col))
        )

        # Identify records that need to have EndDate closed
        df_to_close = df_updated.filter(F.col(current_status_col) != F.col("prev_" + current_status_col))

        # Update the EndDate for the existing records to close them out
        df_final = df_updated.withColumn(
            end_date_col,
            F.when(F.col(current_status_col) == "Inactive", current_date).otherwise(F.col(end_date_col))
        ).withColumn("IsCurrent", F.expr("case when {0} == '{1}' then True else False end".format(current_status_col, config['scd2_active_status'])))

        # Updating Start Dates for new records
        df_final = df_final.withColumn(
            # Set Start Date for new records
            start_date_col,
            F.when(F.col("row_num") == 1, current_date).otherwise(F.col(start_date_col))
        )

        # Set the Start Date of the previous record to current_date - 1 if CurrentDeviceStatus changes
        df_final = df_final.withColumn(
            start_date_col,
            F.when(
                (F.col("row_num") > 1) & 
                (F.col(current_status_col) != F.col("prev_" + current_status_col)),
                F.date_sub(F.lag(F.col(start_date_col)).over(window_spec), 1)
            ).otherwise(F.col(start_date_col))
        )

        # Set default end date logic
        df_final = df_final.withColumn(
            end_date_col,
            F.when(
                (F.col(start_date_col) == current_date) & 
                (F.col(end_date_col) == config['scd2_default_end_date']),
                F.date_sub(F.col(start_date_col), 1)
            ).otherwise(F.col(end_date_col))
        )

        return df_final

    except Exception as e:
        print(f"An error occurred during processing: {e}")
        return None


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def flatten_data(data):
    """
    Flattens a list of dictionaries by extracting the 'value' from each key-value pair.

    This function takes a list of dictionaries, where each dictionary may have nested structures,
    and flattens them into a list of dictionaries that contain only the extracted 'value' for each key.

    Args:
        data (list of dict): A list of dictionaries where each dictionary contains key-value pairs,
                             and the value is expected to be another dictionary with a 'value' key.

    Returns:
        list of dict: A list of flattened dictionaries, with keys from the original dictionaries,
                      and values taken from the 'value' key of each original value dictionary.

    Example:
        Input: [{'a': {'value': 1}, 'b': {'value': 2}}, {'a': {'value': 3}, 'b': {'value': 4}}]
        Output: [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
    """
    flattened_list = []
    for item in data:
        flattened_dict = {key: value['value'] for key, value in item.items()}
        flattened_list.append(flattened_dict)
    return flattened_list

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def invert_columns_to_rows(df: DataFrame, example_count=5) -> DataFrame:
    """
    Inverts the columns of a DataFrame into rows and creates example columns for a specified number of
    example data points per field.

    :param df: DataFrame with string columns to invert.
    :param example_count: Number of examples to collect per field.
    :return: New DataFrame with field names and example columns.
    """
    inverted_rows = []

    fields = df.columns

    for field in fields:

        examples = (df.select(field)
                    .distinct()
                    .limit(example_count)
                    .rdd.flatMap(lambda x: x)
                    .collect())


        while len(examples) < example_count:
            examples.append(None)


        inverted_row = [field] + examples
        inverted_rows.append(inverted_row)

    schema = ["Field"] + [f"Field_Example_{i+1}" for i in range(example_count)]
    
    df = spark.createDataFrame(inverted_rows, schema=schema)

    return df

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def generate_indexed_row_count(df, index_col_name):
    """
    Adds a new column to the DataFrame with a value based on the index of the row.

    Parameters:
    df (DataFrame): The input DataFrame to be processed.
    index_col_name (str): The name of the new column that will contain the row index.

    Returns:
    DataFrame: A new DataFrame with an additional column specified by index_col_name.
    """

    # Create RDD with index
    rdd_with_index = df.rdd.zipWithIndex()
    
    # Map the RDD to create the new DataFrame with the specified column name
    df = rdd_with_index.map(lambda x: (x[1],) + x[0]).toDF([index_col_name] + df.columns)
    
    return df

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def process_dlm_columns_from_config(df: DataFrame, column_expressions: dict) -> DataFrame:
    """
    Processes a Spark DataFrame by adding new columns based on specified expressions,
    categorizing them into filled columns (derived from existing data) and empty columns.

    The function takes in a dictionary with two sub-dictionaries:
    1. "filled_cols": A mapping of new column names to their expressions, which may
       either reference an existing column using the "col()" format or provide a literal value.
    2. "empty_cols": A mapping of new column names to empty values, indicating that
       these columns should be created with empty string values.

    Parameters:
    ----------
    df : DataFrame
        The Spark DataFrame to be processed.
    column_expressions : dict
        A dictionary containing two sub-dictionaries:
        - "filled_cols": A dictionary where keys are new column names and values are
          the expressions for filled values, which can be either a direct value or a 
          reference to an existing column.
        - "empty_cols": A dictionary where keys are column names to create and values
          should be empty strings, which indicates that these columns should be created
          with empty values.
    """
    # Process empty columns
    empty_columns = column_expressions.get("empty_cols", {})
    for col_name in empty_columns:
        df = df.withColumn(col_name, lit(""))
        
    # Process filled columns
    filled_columns = column_expressions.get("filled_cols", {})
    for col_name, expression in filled_columns.items():
        if isinstance(expression, str) and expression.startswith("col(") and expression.endswith(")"):
            # Extract the actual field name from the col function notation
            field_name = expression[4:-1]  # Get the string between col( and )
            df = df.withColumn(col_name, when(col(field_name).isNull(), "").otherwise(col(field_name)))
        else:
            # Use the expression directly for new columns
            df = df.withColumn(col_name, expression)

    # Selecting the relevant columns including 'Field' and 'ColPos'
    selected_columns = list(filled_columns.keys()) + list(empty_columns.keys()) + ["Field"]
    df = df.select(*selected_columns)
    
    return df

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def filter_by_column_names(df: DataFrame, column_name: str, filter_values: list) -> DataFrame:
    return df.filter(df[column_name].isin(filter_values))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def get_most_recent_value(df, group_col, value_col):
    """
    Get the most recent value for each unique group without dropping any columns from the input DataFrame.
    
    :param df: Input DataFrame
    :param group_col: Name of the column to group by
    :param value_col: Name of the timestamp column to evaluate
    :return: DataFrame with the most recent row for each unique group
    """
    # Define the window specification
    window_spec = Window.partitionBy(group_col).orderBy(col(value_col).desc())

    # Add a row number based on the window specification
    df_with_row_number = df.withColumn("row_num", row_number().over(window_spec))

    # Filter to keep only the rows where row_num is 1 (most recent)
    df = df_with_row_number.filter(col("row_num") == 1).drop("row_num")

    return df

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
