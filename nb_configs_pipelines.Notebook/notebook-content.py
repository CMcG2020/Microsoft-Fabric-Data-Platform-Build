# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# #### Orchestration Configs
# ---
# Notebook to store all configurations for pipeline orchestrations.
# 
# 1. activity
# - timeout_per_cell: the timeout for every cell, the default is 60 seconds
# - retries: how many times the notebook should be executed if an error occurs
# - retry_interval: the interval between every try, the default is 0 so retry will start instantly
# 
# 2. dag
# - concurrency: Number of notebooks to run in parallel
# - timeout_in_seconds: Time out in seconds of entire DAG.
# - dag_size: Max number of nodes to display on the DAG visual
# - dag_layout: Defaults to spectral
# - display_dag_via_graph_viz: Determines if DAG is visually displayed
# 
# Fine tuning required down the line.


# CELL ********************

orchestration_configs = {
    'activity': {
        'normal': {
            'timeout_per_cell': 3600, 
            'retries': 2,
            'retry_interval': 10
        },
        'backfill': {
            'timeout_per_cell': 3600, 
            'retries': 1,
            'retry_interval': 10
        },
        'integration_test': {
            'timeout_per_cell': 300, 
            'retries': 1,
            'retry_interval': 10
        }
    },
    'dag': {
        'normal':{
            'concurrency': 5,
            'timeout_in_seconds': 5400,
            'dag_size': 20,
            'dag_layout': 'spectral',
            'display_dag_via_graph_viz': True
        },
        'backfill':{
            'concurrency': 5,
            'timeout_in_seconds': 5400,
            'dag_size': 20,
            'dag_layout': 'spectral',
            'display_dag_via_graph_viz': True
        },
        'integration_test':{
            'concurrency': 5,
            'timeout_in_seconds': 600,
            'dag_size': 20,
            'dag_layout': 'spectral',
            'display_dag_via_graph_viz': True
        }
    }
}

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
