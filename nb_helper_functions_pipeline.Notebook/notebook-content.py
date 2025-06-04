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

def generate_activity(notebook: str, args: dict, activity_type: str = 'normal', dependencies: Optional[List[str]] = None, interval: tuple = None) -> dict:
    """Generates a dictionary representing a single activity."""
    activity_configs = globals()['orchestration_configs']['activity'][activity_type]

    if 'table_name' in args.keys() and interval:
        name = f"{notebook}_{args['table_name']}_{interval[0]}"
    elif 'table_name' in args.keys():
        name = f"{notebook}_{args['table_name']}"
    else:
        name = notebook

    layer = notebook.split('_')[2]

    if dependencies is None:
        dependencies = []

    if layer == 'cleansed' and not dependencies:
        dependencies.append(f"{notebook.replace('cleansed', 'sourced')}_{args['table_name']}")

    return {
        "name": name,
        "path": notebook,
        "args": args if args else {},
        "dependencies": dependencies,
        "timeoutPerCellInSeconds": activity_configs['timeout_per_cell'],
        "retry": activity_configs['retries'],
        "retryIntervalInSeconds": activity_configs['retry_interval'],
    }

def generate_pipeline_dag(asset_list: list, trigger_time: str, dag_and_activity_type: str = 'normal') -> dict:
    """Generates a full DAG taking into account all conformed asset list."""
    common_configs = globals()['global_configs']
    dag_configs = globals()['orchestration_configs']['dag'][dag_and_activity_type]

    sourced = []
    cleansed = []
    conformed = []

    for asset in asset_list:
        conformed_dependencies = []
        table_type = 'dimensions' if asset.startswith('dim') else 'facts'
        required_tables = globals()[table_type][asset]['required_tables']

        for layer in required_tables:
            if layer == 'cleansed':
                for source_system in required_tables[layer]:
                    for table in required_tables[layer][source_system]:
                        sourced_activity = generate_activity(common_configs['sourced_nb_name'].format(source_system), {'trigger_time': trigger_time, 'table_name': table}, dag_and_activity_type)
                        cleansed_activity = generate_activity(common_configs['cleansed_nb_name'].format(source_system), {'trigger_time': trigger_time, 'table_name': table}, dag_and_activity_type)
                        
                        sourced.append(sourced_activity) if sourced_activity not in sourced else None
                        cleansed.append(cleansed_activity) if cleansed_activity not in cleansed else None

                        conformed_dependencies.append(f"{common_configs['cleansed_nb_name'].format(source_system)}_{table}")
            elif layer == 'conformed':
                for table_type in required_tables[layer]:
                    for table in required_tables[layer][table_type]:
                        conformed_dependencies.append(f"{common_configs['conformed_nb_name'].format(table)}")

        
        conformed_activity = generate_activity(f"{common_configs['conformed_nb_name'].format(asset)}", {'trigger_time': trigger_time}, dag_and_activity_type, conformed_dependencies)
        conformed.append(conformed_activity)

    return {
        "activities": [activity for activity in sourced + cleansed + conformed], 
        "timeoutInSeconds": dag_configs['timeout_in_seconds'],
        "concurrency": len(sourced)
        }


def generate_date_tuples(from_date: str, to_date: str, interval_months: int = 2) -> list:
    """Generate a list of date tuples used for backfilling purposes.""" 
    start_date = datetime.strptime(from_date, '%Y-%m-%dT%H:%M:%SZ')
    end_date = datetime.strptime(to_date, '%Y-%m-%dT%H:%M:%SZ')
    
    date_tuples = []

    while start_date < end_date:
        # Calculate the next end date
        next_end_date = start_date + relativedelta(months=interval_months) - timedelta(seconds=1)
        
        # Ensure the next_end_date does not exceed the global end_date
        if next_end_date > end_date:
            next_end_date = end_date
        
        # Convert back to string format and add to the list
        date_tuples.append((
            start_date.strftime('%Y-%m-%dT%H:%M:%SZ'),
            next_end_date.strftime('%Y-%m-%dT%H:%M:%SZ')
        ))
        
        # Move to the next start date
        start_date = next_end_date + timedelta(seconds=1)

    return date_tuples

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
