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
# META     },
# META     "environment": {
# META       "environmentId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
# META       "workspaceId": "yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy"
# META     }
# META   }
# META }

# MARKDOWN ********************

# #### Backfill Notebook
# ---
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

# MARKDOWN ********************

# ###### **<u>Step 2: Define Backfill Variables</u>**
# - The following cell is noted as a Parameter cell; default values can be overwritten when the notebook is executed either via DAG calls or Data Factory Pipelines. 
# - To 'parameterize' a code cell, click on the `...` 'more command' button on the right as you hover your cursor over the cell and click `[@] Toggle parameter cell`

# PARAMETERS CELL ********************

trigger_time = None # '2024-08-09T00:00:00Z'
from_date = None # '2022-08-01T00:00:00Z'
to_date = None # '2024-08-09T23:59:59Z'
source_system = None # 'example_system'
table_name = None # 'example_table'

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ###### **<u>Step 3: Extract configurations</u>**
# - Extract dag configurations

# CELL ********************

dag_configs = globals()['orchestration_configs']['dag']['backfill']

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ###### **<u>Step 4: Build pipeline DAG</u>**
# ---
# - Build full DAG via `generate_pipeline_dag` helper function. 
# - Only steps required is to define the asset list and pass it in as a parameter within the `generate_pipeline_dag` function
# - This generates a the activity with required dependencies appended from the Sourced Layer through to the Conformed Layer
# - Output will be printed out for de-bugging purposes

# CELL ********************

# generate date tuples
dates_intervals = generate_date_tuples(from_date, to_date, 2)

# for each interval generate a sourced activity and the relevant dependency for cleansed
sourced = []
dependencies = []
for interval in dates_intervals:
    sourced.append(
        generate_activity(
            notebook = globals()['global_configs']['sourced_nb_name'].format(source_system),
            args = {'trigger_time': trigger_time, 'from_date': interval[0], 'to_date': interval[1], 'table_name': table_name},
            activity_type = 'backfill',
            interval = interval
        )
    )
    dependencies.append(f"{globals()['global_configs']['sourced_nb_name'].format(source_system)}_{table_name}_{interval[0]}")

# generate a single cleansed activity with all sourced dependencies passed
cleansed = [
    generate_activity(
            notebook = globals()['global_configs']['cleansed_nb_name'].format(source_system),
            args = {'trigger_time': trigger_time, 'table_name': table_name},
            activity_type = 'backfill',
            dependencies = dependencies
            )
    ]

# generate full dag
dag = {"activities": [activity for activity in sourced + cleansed], "timeoutInSeconds": dag_configs['timeout_in_seconds'], "concurrency": len(sourced)}
pprint(dag)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ###### **<u>Step 5: Run Pipeline</u>**
# ---
# - Run the below cell to validate asset pipeline works correctly.

# CELL ********************

mssparkutils.notebook.runMultiple(dag)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
