# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "environment": {
# META       "environmentId": "xxx",
# META       "workspaceId": "00000000-0000-0000-0000-000000000000"
# META     }
# META   }
# META }

# MARKDOWN ********************

# #### Testing notebook for BAs - Smartsheet API
# ---
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

import requests
import pandas as pd

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# PARAMETERS CELL ********************

table_name = '64254'  # Replace with the desired table_name

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

global_configs = globals()['global_configs']
source_configs = globals()['smartsheet']
table_configs = source_configs['source_tables'][table_name]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ###### **<u>Step 2: Configuration without using source_configs</u>**
# 
# - configs for api call
# - make api call
# - convert to dataframe for queries

# CELL ********************

# # Smartsheet configuration
# smartsheet_config = {
#   'name': 'Smartsheet',
#   'kv_api_token_name': 'api-api',
#   'api_base_url': 'https://api.ssheet.com/2.0',
#   'timeout': 30
# }

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

class SmartsheetReaderTest:
  def __init__(self, api_token, table_name):
      self.api_token = api_token
      self.table_name = table_name
      self.base_url = source_configs['api_base_url']
      self.timeout = source_configs['timeout']

  def get_sheet_data(self):
      url = f"{self.base_url}/sheets/{self.table_name}"
      headers = {
          "Authorization": f"Bearer {self.api_token}",
          "Content-Type": "application/json"
      }
      
      response = requests.get(url, headers=headers, timeout=self.timeout)
      response.raise_for_status()
      
      return response.json()

  def sheet_to_dataframe(self, sheet_data):
      if 'rows' not in sheet_data or 'columns' not in sheet_data:
          return pd.DataFrame()
      
      columns = [col['title'] for col in sheet_data['columns']]
      rows = []
      for row in sheet_data['rows']:
          row_data = [cell.get('value', '') for cell in row['cells']]
          rows.append(row_data)
      
      df = pd.DataFrame(rows, columns=columns)
      df['table_name'] = sheet_data['id']
      df['sheet_name'] = sheet_data['name']
      return df

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

try:
  # Initialize SmartsheetReader
  api_token = extract_secret(source_configs['kv_api_token_name'])
  reader = SmartsheetReaderTest(api_token, table_name)
  
  # Get sheet data
  sheet_data = reader.get_sheet_data()
  
  # Convert sheet data to DataFrame
  df = reader.sheet_to_dataframe(sheet_data)
  
  if not df.empty:
      print(f"Successfully retrieved data for sheet '{sheet_data['name']}' (ID: {table_name}) with {len(df)} rows.")
      
      # Convert pandas DataFrame to Spark DataFrame
      df = spark.createDataFrame(df)
      
      # Display the Spark DataFrame
      display(df)
  else:
      print(f"No data found in sheet {table_name}.")

except Exception as e:
  print(f"An error occurred while processing sheet {table_name}: {str(e)}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run nb_helpers_automated_dlm_schema_generator

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
