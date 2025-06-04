# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "xxx",
# META       "default_lakehouse_name": "lh_cleansed",
# META       "default_lakehouse_workspace_id": "xxx"
# META     },
# META     "environment": {
# META       "environmentId": "xxx",
# META       "workspaceId": "00000000-0000-0000-0000-000000000000"
# META     }
# META   }
# META }

# MARKDOWN ********************

# #### Orchestration Notebook
# ---
# This notebook will be called by the `pl_master` pipeline defined within the `pipelines` folder and is specifically designed for the orchestration of a specific assets defined within the parameter `asset_list` passed from Data Factory. For example for the `Application` asset, the `asset_list` will be populated with `dim_application, dim_application_source, dim_application_map`. This will be used to generate a full end to end dag, from ingesting the required tables in Sourced, cleansing in Cleansed and building the conformed tables in Conformed.
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

# ###### **<u>Step 2: Define Parameters</u>**
# - The following cell is noted as a Parameter cell; default values can be overwritten when the notebook is executed either via DAG calls or Data Factory Pipelines. 
# - To 'parameterize' a code cell, click on the `...` 'more command' button on the right as you hover your cursor over the cell and click `[@] Toggle parameter cell`

# PARAMETERS CELL ********************

trigger_time = None
asset_list = None

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ###### **<u>Step 3: Extract configurations</u>**
# - Extract dag configurations

# CELL ********************

dag_configs = globals()['orchestration_configs']['dag']['normal']

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

# convert asset string to list
asset_list = [asset.strip() for asset in asset_list.split(',')]

# generate full dag
dag = generate_pipeline_dag(asset_list, trigger_time)

# print dag
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

mssparkutils.notebook.runMultiple(dag, {
    "displayDAGViaGraphviz": dag_configs['display_dag_via_graph_viz'], 
    "DAGLayout": dag_configs['dag_layout'], 
    "DAGSize": dag_configs['dag_size']
    }
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
