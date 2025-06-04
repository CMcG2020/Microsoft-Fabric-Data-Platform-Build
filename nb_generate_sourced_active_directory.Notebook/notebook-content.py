# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "environment": {
# META       "environmentId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
# META       "workspaceId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
# META     }
# META   }
# META }

# MARKDOWN ********************

# #### Generate Sourced - Example Data Source
# ---
# Generic notebook to extract records via REST API from an external data source's tables, before storing the raw data within the `Sourced` Lakehouse as parquet format.
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

%run nb_schema_sourced_example_data_source

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ###### **<u>Step 2: Define Parameters</u>**
# The following cell is noted as a Parameter cell; default values can be overwritten when the notebook is executed either via DAG calls or Data Factory Pipelines. To 'parameterize' a code cell, click on the `...` 'more command' button on the right as you hover your cursor over the cell and click `[@] Toggle parameter cell`

# PARAMETERS CELL ********************

trigger_time = None
table_name = None
from_date = None
to_date = None

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
source_configs = globals()['example_data_source']
table_configs = source_configs['source_tables'][table_name]
source_schema = globals()[f"schema_{table_name}_v{table_configs['schema_version']}"]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Main Code Block
# ---
# ###### **<u>Step 4: Perform ETL</u>**
# - extract API token for external data source system stored in environment based Azure Key Vault
# - initiate data source reader class and query
# - retrieve records from table specified from parameter cell
# - write records in batches to Sourced Lakehouse

# CELL ********************

load_type = table_configs['load_type']
if load_type == 'delta':
    print(f'Delta load for table: {table_name}')
    from_date = (datetime.strptime(trigger_time, '%Y-%m-%dT%H:%M:%SZ') - timedelta(days=table_configs['delta_days'])).strftime('%Y-%m-%dT00:00:00Z')
    to_date = (datetime.strptime(trigger_time, '%Y-%m-%dT%H:%M:%SZ') - timedelta(days=1)).strftime('%Y-%m-%dT23:59:59Z')
elif load_type == 'full':
    print(f'Full load for table: {table_name}')
    from_date = to_date = None
else: 
    raise Exception(f"Unknown load type: {load_type}")

# Extract secrets
tenant_id = extract_secret(source_configs['kv_tenant_id'])
client_id = extract_secret(source_configs['kv_client_id'])
client_secret = extract_secret(source_configs['kv_client_secret'])

# Initialize reader
data_source_reader = ExternalDataSourceReader(
  tenant_id=tenant_id,
  client_id=client_id,
  client_secret=client_secret,
  max_workers=5
)
 
# Track successfully processed batches  
processed_batches = []  
batch_counter = 1  # counter for file naming  

try:  
    if table_name == 'users':  
        # Process users data using existing batched method  
        data_generator = data_source_reader.get_all_users_data_batched(batch_size=2000)  
    elif table_name == 'groups':  
        # Process groups data  
        groups_data = data_source_reader.get_all_groups_data()  
        # Create a generator to yield batches of group data  
        def group_data_generator(data, batch_size):  
            for i in range(0, len(data), batch_size):  
                yield data[i:i + batch_size]  
        data_generator = group_data_generator(groups_data, 2000)  
    else:  
        raise ValueError(f"Unknown table name: {table_name}")  

    # Process and write batches one at a time  
    for batch_data in data_generator:  
        try:  
            batch_name = f"{table_name}_batch_{batch_counter}"  
            print(f"Writing {batch_name} with {len(batch_data)} records...")  

            write_parquet_to_lakehouse(  
                batch_data,  
                global_configs['sourced_lh_name'],  
                source_configs['name'],  
                batch_name,  
                table_configs['schema_version'],  
                trigger_time,  
                is_batch=True  
            )  

            # Track successful batch  
            processed_batches.append(batch_counter)  
            print(f"Successfully wrote batch {batch_counter}")  
            batch_counter += 1  

        except Exception as e:  
            print(f"Error writing batch {batch_counter}: {str(e)}")  
            # Continue with next batch even if current fails  
            batch_counter += 1  
            continue  

except Exception as e:  
    print(f"Error during processing: {str(e)}")  
finally:  
    print(f"Processing completed. Successfully wrote {len(processed_batches)} batches.")  
    if processed_batches:  
        print(f"Batch numbers written: {processed_batches}")  

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
