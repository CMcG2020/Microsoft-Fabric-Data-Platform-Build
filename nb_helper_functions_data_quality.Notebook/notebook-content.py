# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# #### Helper Functions for Data Quality Checks
# ---
# Helper functions for supporting soda data quality checks.

# CELL ********************

%run nb_schema_dq_checks

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

class DataQualityHelper:
    """
    DataQualityHelper is a utility class for running data quality checks using Soda Core 
    and writing the results to a Delta Lake table in the Conformed lakehouse.
    """
    def __init__(
        self,
        scan_definition_name: str,
        data_source_name: str,
        source_system: str,
        checks_yaml_file_path: str,
        yaml_variables: dict,
        lakehouse_name: str,
        dq_table_name: str,
        dq_schema: List,
        dq_schema_version: int,
        delta_writer_func,
        partition_by: list,
        trigger_time: str
    ):
        """
        Initializes the DataQualityHelper with common parameters.

        Parameters:
        - scan_definition_name: Name of the DQ scan.
        - data_source_name: Name of the Table for which the data will be written into (either cleansed table/ conformed table name).
        - source_system: Which Source system the data is coming from. 
        - checks_yaml_file_path: Path to the YAML file with DQ checks.
        - yaml_variables: Variables for the YAML file.
        - lakehouse_name: Name of the lakehouse.
        - dq_table_name: Name of the DQ table.
        - dq_schema: schema of the data quality checks table
        - dq_schema_version: Schema Version of the DQ table.
        - delta_writer_func: Function to write data using Delta Lake.
        - partition_by: List of columns to partition by.
        - trigger_time: Time that the pipeline ran.
        """
        self.scan_definition_name = scan_definition_name
        self.data_source_name = data_source_name
        self.source_system = source_system
        self.checks_yaml_file_path = checks_yaml_file_path
        self.yaml_variables = yaml_variables
        self.lakehouse_name = lakehouse_name
        self.dq_table_name = dq_table_name
        self.dq_schema = dq_schema
        self.dq_schema_version = dq_schema_version
        self.delta_writer_func = delta_writer_func
        self.partition_by = partition_by
        self.trigger_time = trigger_time

    def _execute_sql_dq_checks(self) -> dict:
        """
        Internal method to execute data quality checks using Soda Core.

        Returns:
        - Dictionary containing the status, logs, and dq_results_df.
        """
        # Create a Scan object, set a scan definition, and attach a Spark session
        scan = Scan()
        scan.set_scan_definition_name(self.scan_definition_name)
        scan.set_data_source_name(self.data_source_name)
        scan.add_spark_session(spark, data_source_name=self.data_source_name)

        # Add variables to the scan if they have been defined
        if self.yaml_variables:
            scan.add_variables(self.yaml_variables)

        # Add checks from the YAML file
        scan.add_sodacl_yaml_file(self.checks_yaml_file_path)

        # Execute the scan
        scan.execute()

        # Get the scan results (as a dictionary)
        scan_results = scan.get_scan_results()

        # Collect check results
        check_results_list = []
        for check_result in scan_results['checks']:
            # Extract check record count value from diagnostics if it exists
            record_count = int(check_result.get('diagnostics', {}).get('value')) if check_result.get('diagnostics') else None

            result = {
                'TableName': self.data_source_name,
                'SourceSystem': self.source_system,
                'CheckName': check_result.get('name'),
                'CheckLayer': self.scan_definition_name,
                'CheckDescription': check_result.get('definition'),
                'CheckOutcome': check_result.get('outcome').lower(),  # 'pass', 'fail', 'skip'
                'ExecutionTime': datetime.now(),
                'AdditionalInfo': str(check_result.get('diagnostics')) if check_result.get('diagnostics') else None,
                'RecordCount': record_count
            }
            check_results_list.append(result)

        # Extract the schema for the dq_checks table from nb_schema_dq_checks notebook run above
        dq_schema = self.dq_schema

        # Create a DataFrame from the results
        if check_results_list:
            dq_results_df = spark.createDataFrame(check_results_list)
        else:
            # Create an empty DataFrame with the expected schema
            dq_results_df = spark.createDataFrame([], schema=dq_schema)

        logs_text = scan.get_logs_text()

        # Determine status based on 'hasErrors' or 'hasFailures' in scan_results
        status = "failure" if scan_results.get('hasErrors') or scan_results.get('hasFailures') else "success"

        # Return a dictionary with the status, logs, and dq_results_df
        dq_results = {
            "status": status,
            "logs": logs_text,
            "dq_results_df": dq_results_df
        }

        return dq_results

    def add_dq_checks_to_table(self) -> dict:
        """
        Executes data quality checks and writes logs and summary results to a table in the conformed layer.

        Returns:
        - Dictionary with 'status' and 'logs'.
        """
        #Extract Trigger Date to use as the scan date
        scan_date = self.trigger_time[:10]
        # Execute DQ checks
        dq_results = self._execute_sql_dq_checks()

        # Prepare dq_results_df with additional metadata columns
        dq_results_df = dq_results['dq_results_df'] \
             .withColumn('ScanDate', F.lit(scan_date)) \
             .withColumn('CheckType', F.lit('')) \
             .withColumn('OnFailure', F.lit('log_and_fail')) # TODO: Extract this from soda yaml

        # Write the DQ results to the conformed layer using delta_writer_func
        self.delta_writer_func(
            df=dq_results_df,
            lakehouse_name=self.lakehouse_name,
            dq_table_name=self.dq_table_name,
            data_source_name = self.data_source_name,
            source_system=self.source_system,
            scan_date = scan_date,
            schema_version = self.dq_schema_version,
            partition_by=self.partition_by
        )

        return {'status': dq_results['status'], 'logs': dq_results['logs']}

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def _run_data_quality_checks_and_write_logs_to_table(df:DataFrame, layer: str, pii_enabled: bool = False ) -> dict :
    """
    Runs the Data Quality Checks by calling the DataQualityHelper Class and adding the checks to a table.
    Parameters:
        - df: Name of the df to run the dq checks on.
        - layer: Name of the layer the checks are performed on.
        - pii_enabled: whether the associated df has pii data or not.
    Returns:
        - Dictionary containing the dq_results logs.

    ***NOTE***: This function is only meant to be called within 'execute_write_to_lakehouse_with_dq_checks' defined below.
    
    """
    # Prepare variables
    #TODO: Refactor this function to have explicit dependancies rather than having to reference global/local variables implicitly.
    # Extract schema of data quality checks table
    dq_schema = [col['field'] for col in dq_checks_v1]
    # Set the correct data source name based on PII flag
    if pii_enabled:
      data_source_name = f"{table_name}_pii"
    else:
      data_source_name = table_name  # Use the original table name for non-PII
      
    # Extract the layer the checks are performed on
    if layer == 'Cleansed':
        scan_definition_name = global_configs['cleansed_scan_definition_name']
        source_system = source_configs['name']
        table_configs = table_config # This attaches the table_config values from the notebook
        non_nullable_cols_list = table_configs.get('non_nullable_cols', [])
    elif layer == 'Conformed':
        scan_definition_name = global_configs['conformed_scan_definition_name']
        table_configs = target_table_configs
        if pii_enabled:
            non_nullable_cols_list = table_configs.get('non_nullable_cols_pii', [])
            data_source_name = f"{table_name}_pii" 
            source_system = '' # Not defined for PII tables
            logging.info(f"Extracted non-nullable columns: {non_nullable_cols_list} and table name: {data_source_name}")
        else:
            non_nullable_cols_list = table_configs.get('non_nullable_cols', [])
            source_system = ", ".join([row[0] for row in df.select("SourceSystem").distinct().collect()]) # Some Tables load from more than 1 Source System Per Load.
            logging.info(f"Extracted non-nullable columns: {non_nullable_cols_list} and source system/s: {source_system}")

    # If a dq check file is not specified, we use the generic checks yaml file
    if 'dq_check_file' in table_configs:
        dq_check_file = table_configs.get('dq_check_file')
        yaml_variables = {
            "table_name": data_source_name
        }
    else:
        dq_check_file = global_configs['soda_generic_checks_yaml_file_path']
        # Extract PK and non-nullable columns from table_configs
        primary_key = table_configs.get('primary_key')
        # Create the WHERE condition to check if any column is NULL
        null_check_condition = " OR ".join([f"{col} IS NULL" for col in non_nullable_cols_list])
        # Prepare variables for the YAML file
        yaml_variables = {
            "table_name": data_source_name,
            "primary_key": primary_key,
            "null_check_condition": null_check_condition
        }

    # Create temporary view for the data source
    df.createOrReplaceTempView(f"{data_source_name}")
    
    # Initialize the DataQualityHelper
    dq_helper = DataQualityHelper(
        scan_definition_name=scan_definition_name,
        source_system=source_system,
        data_source_name=data_source_name,
        checks_yaml_file_path=dq_check_file,
        yaml_variables=yaml_variables,
        lakehouse_name=global_configs['conformed_lh_name'],
        dq_table_name=globals()['dq_checks']['name'],
        dq_schema=dq_schema,
        dq_schema_version = globals()['dq_checks']['schema_version'], 
        delta_writer_func=dq_delta_writer,
        partition_by=globals()['dq_checks']['partition_by'],
        trigger_time =trigger_time
    )

    dq_results = dq_helper.add_dq_checks_to_table()

    return dq_results

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def execute_write_to_lakehouse_with_dq_checks(
    df: DataFrame,
    layer: str,
    write_mode_cleansed: str = None,
    partition_by: list = None,
    pii_enabled: bool = False
):
    """
    Writes data to the lakehouse, performing data quality checks.
    If DQ checks failed and we're in 'dev' or 'sit', data will still be written to cleansed/conformed layers.
    If DQ checks failed in other environments, exception will been raised and no data will be written.

    Parameters:
        - df: The DataFrame to write.
        - layer: The layer to write to ('Cleansed' or 'Conformed').
        - write_mode_cleansed: Write mode for Cleansed layer (default: 'overwrite').
        - partition_by: List of columns to partition by (for Conformed layer).
        - pii_enabled: Indicates if PII data is present and should be handled.

    ***Note***:
        This function is only meant to be called within an asset notebook & 
        depends on:
        - global variables: env, global_configs
        - local variables defined in asset notebook/Table configs (in nb_configs): table_configs (source or target),
        primary_key, attributes_key, table_name, trigger_time, partition_by.

    """
    #TODO: Refactor this function to have explicit dependancies rather than having to reference global/local variables implicitly.
    
    def write_conformed_data(df_to_write: DataFrame, lakehouse_name: str, table_name: str):
        """Helper function to write data to the Conformed Lakehouse."""
        delta_writer(
            df=df_to_write,
            lakehouse_name=lakehouse_name,
            table=table_name,
            schema_version=target_table_configs['schema_version'],
            write_type=target_table_configs['write_type'],
            primary_key=primary_key,
            attributes_key=attributes_key,
            partition_by=partition_by
        )

    def write_cleansed_data(df_to_write: DataFrame, lakehouse_name: str, write_mode_cleansed: str = None):
        """Helper function to write data to the Cleansed Lakehouse."""
        write_parquet_to_lakehouse(
            df_to_write,
            lakehouse_name=lakehouse_name,
            data_provider=source_configs['name'], 
            data_feed=table_name,
            schema_version=table_config['schema_version'],
            trigger_time=trigger_time,
            write_mode=write_mode_cleansed
        )

    def handle_dq_failure(logs: str, layer_name: str):
        """Helper function to handle data quality check failures."""
        logging.error(f"Data quality checks failed for {layer_name} layer.")
        logging.error(f"Logs:\n{logs}")
        if env not in ('dev', 'sit'):
            logging.error(f"Data will not be written to the {layer_name} Lakehouse due to DQ failures.")
            raise Exception("Data quality checks failed. Please review the logs for more details.")
        else:
            logging.warning(f"Continuing despite data quality check failures in {env} environment.")

    def perform_data_quality_checks(df_to_check: DataFrame, layer_name: str, pii: bool = False) -> bool:
        """Helper function to perform data quality checks and determine if data should be written."""
        dq_results = _run_data_quality_checks_and_write_logs_to_table(df=df_to_check, layer=layer_name, pii_enabled=pii)
        if dq_results['status'] == 'success':
            return True
        else:
            handle_dq_failure(dq_results['logs'], f"{layer_name}{' PII' if pii else ''}")
            # In 'dev' or 'sit', we proceed even if DQ checks fail.
            return env in ('dev', 'sit')

    # Start of the main function logic
    if layer == 'Conformed':
        if pii_enabled:
            if perform_data_quality_checks(df, layer, pii=True):
                write_conformed_data(df, global_configs['conformed_pii_lh_name'], f"{target_table_configs['name']}_pii")
        else:
            if perform_data_quality_checks(df, layer):
                write_conformed_data(df, global_configs['conformed_lh_name'], target_table_configs['name'])

    elif layer == 'Cleansed':
        if perform_data_quality_checks(df, layer):
            write_cleansed_data(df, global_configs['cleansed_lh_name'])

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
