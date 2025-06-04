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
# Notebook to host common classes / functions to support read activities across the medallion layers

# CELL ********************

def write_parquet_to_lakehouse(data: Union[list, DataFrame], lakehouse_name: str, data_provider: str, data_feed: str, schema_version: str, trigger_time: str, write_mode: str = None, is_batch: bool = False) -> None:
  """Function to write data to either the Sourced or Cleansed Lakehouse in parquet format."""
  try:
      # validate lakehouse
      if lakehouse_name not in {globals()['global_configs']['sourced_lh_name'], globals()['global_configs']['cleansed_lh_name']}:
          raise ValueError(f"Unsupported lakehouse: {lakehouse_name}. Only '{globals()['global_configs']['sourced_lh_name']}' and '{globals()['global_configs']['cleansed_lh_name']}' are supported by this writer.")

      # construct write path
      root_abfs_path = get_lakehouse_abfs_path(lakehouse_name)
      meta_effective_date = trigger_time[:10].replace('-', '')

      if is_batch:
          # Path format for batch processing
          write_path = f"{root_abfs_path}/Files/Lake/{data_provider}/{data_feed}/schema_version={schema_version}/meta_effective_date={meta_effective_date}/{data_feed}"
      else:
          # Original path format
          write_path = f"{root_abfs_path}/Files/Lake/{data_provider}/{data_feed}/schema_version={schema_version}/meta_effective_date={meta_effective_date}"

      # construct dataframe
      df = spark.createDataFrame(pd.DataFrame(data).astype(str)).dropDuplicates() if isinstance(data, list) else data

      # write 
      df.write.mode(write_mode if write_mode else 'overwrite').parquet(write_path)

      print(f"{data_provider}'s {data_feed} DataFrame written to {lakehouse_name} at {write_path}.")

  except Exception as e:
      print(f"Failed to write data: {e}")
      raise e

def delta_writer(df: DataFrame, lakehouse_name: str, table: str, schema_version: int, write_type: str, primary_key: str = None, attributes_key: str = None, partition_by: str = None) -> None:
    """Delta Lake Writer based on Slowly Changing Dimension 1 Modeller. Only supports writing to the Conformed Lakehouse."""
    table_name = f"{table}_sv_{schema_version}"
    delta_path = f"{get_lakehouse_abfs_path(lakehouse_name)}/Tables/{table_name}"

    if not DeltaTable.isDeltaTable(spark, delta_path) or write_type == 'overwrite':
        if partition_by:
            df.write.mode("overwrite").format("delta").partitionBy(partition_by).save(f'{delta_path}')
        else:
            df.write.mode("overwrite").format("delta").save(f'{delta_path}')
        print(f"Created / Overwrite table '{table_name}' in the Conformed Lakehouse at '{delta_path}'")
    else:
        full_dict = {col: f"source.{col}" for col in df.columns}
        dt = DeltaTable.forPath(spark, delta_path)

        if write_type == 'merge':
            print(f"Merging to '{table_name}' table on primary key: '{primary_key}'")
            merge_key = primary_key 
            dt.alias("target") \
                .merge(df.alias("source"), f"target.{merge_key} = source.{merge_key}") \
                .whenMatchedUpdate(condition=f"target.{attributes_key} != source.{attributes_key}", set=full_dict) \
                .whenNotMatchedInsert(values=full_dict) \
                .execute()
        elif write_type == 'append':
            print(f"Idempotent appending to '{table_name}' table on attributes key: '{attributes_key}'")
            merge_key = attributes_key
            dt.alias("target") \
                .merge(df.alias("source"), f"target.{merge_key} = source.{merge_key}") \
                .whenNotMatchedInsert(values=full_dict) \
                .execute()
        else:
            raise ValueError(f'{write_type} write type not defined.')


def mask_personal_and_sensitive_fields(df: DataFrame, lakehouse: str, source_system: str, table: str, schema: dict, schema_version: int, trigger_time: str) -> None:
    """Handles the masking of personal or sensitive fields from either the Sourced or Cleansed layer."""
    
    origin = 'from' if 'sourced' in lakehouse else 'to'
    schema = expand_nested_schema(schema) if 'cleansed' in lakehouse else schema

    personal_and_sensitive_fields = [row for row in schema if row['personal'] or row['sensitive']]
    for row in personal_and_sensitive_fields:
        if 'sourced' in lakehouse:
            df = df.withColumn(row[origin], F.lit(None).cast('string'))
        else:
            df = df.withColumn(row[origin], F.lit(None).cast(row['dataType']))

    write_parquet_to_lakehouse(df, lakehouse, source_system, table, schema_version, trigger_time)
    print(f'Personal and sensitive in {table} within {lakehouse} has been masked\n')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def dq_delta_writer(
    df: DataFrame,
    lakehouse_name: str,
    dq_table_name: str,
    data_source_name: str,
    source_system: str,
    scan_date: str,
    schema_version: int,
    partition_by: list
) -> None:
    """Delta Lake Writer for Data Quality Checks.
    """
    table_name = f"{dq_table_name}_sv_{schema_version}"
    delta_path = f"{get_lakehouse_abfs_path(lakehouse_name)}/Tables/{table_name}"

    if DeltaTable.isDeltaTable(spark, delta_path):
        # Table exists, perform merge
        delta_table = DeltaTable.forPath(spark, delta_path)

        # Additional conditions based on partition_by columns
        merge_condition = ' AND '.join([f"target.{col} = source.{col}" for col in partition_by])
        
        # Explicit merge condition for source_system, data_source_name, and scan_date to alleviate ConcurrentAppend Exception
        merge_condition_with_additional_conditions = f"""
            {merge_condition} AND
            target.SourceSystem = '{source_system}' AND
            target.TableName = '{data_source_name}' AND
            target.ScanDate = '{scan_date}'
        """
        
        # Perform the merge operation and ignore updates if data has already been written to the existing partitions.
        # This is so that we preserve history of 1st data quality check run for the SourceSystem, TableName & ScanDate partitions(including failures/warnings, if any). 
        delta_table.alias("target").merge(
            source=df.alias("source"),
            condition=merge_condition_with_additional_conditions
        ).whenNotMatchedInsertAll() \
         .execute()

        print(f"Merged data into '{table_name}' in the Lakehouse at '{delta_path}' using merge condition: {merge_condition_with_additional_conditions}.")
    else:
        # Table doesn't exist, write the entire DataFrame
        df.write.mode("overwrite") \
            .format("delta") \
            .option("mergeSchema", "true") \
            .partitionBy(partition_by) \
            .save(delta_path)
        print(f"Written data to '{table_name}' in the Lakehouse at '{delta_path}'.")
        

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def create_new_empty_table(schema, table_path):
    """
    Creates a new empty table at the specified path using the provided schema.

    This function checks if a table already exists at the specified path. If the table does not exist,
    it creates a new DataFrame based on the input schema and writes this DataFrame to the specified 
    location using the Delta Lake format. If the table already exists, it does not perform any action.

    Parameters:
    ----------
    schema : list of dict
        A list of dictionary objects representing the schema for the new table. Each dictionary should
        contain at least 'field' and 'dataType' keys to define the columns and their data types.

    table_path : str
        The path where the table should be created. This path is checked to determine if the table
        already exists.

    Returns:
    -------
    str
        A message indicating the outcome of the operation. It returns 
        - "Data processed successfully." if the table was created,
        - "Table already exists. No action taken." if the table already exists,
        - An error message if any exception occurs during the operation.

    Raises:
    ------
    Exception
        This function handles exceptions internally and returns an error message if an error occurs
        during the processing steps.
    """
    
    table_exists = check_table_exists(table_path)

    if not table_exists:
        try:
            df = create_empty_df_if_needed(schema, table_exists)
            attributes = [f['field'] for f in target_schema if f['field'] not in metadata_fields + [primary_key]]

            df = df \
                .select(*[F.col(f['field']).cast(f['dataType']) for f in target_schema]) \
                .transform(lambda df: add_hash_key(df, attributes_key, attributes))

            delta_writer(
                df=df, 
                lakehouse_name=global_configs['conformed_lh_name'], 
                table=target_table_configs['name'], 
                schema_version=target_table_configs['schema_version'], 
                write_type=target_table_configs['write_type'], 
                primary_key=primary_key, 
                attributes_key=attributes_key
            )
            return "Data processed successfully."
        except Exception as e:
            return f"An error occurred: {e}"
    else:
        return "Table already exists. No action taken."

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
