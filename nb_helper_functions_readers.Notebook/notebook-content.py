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
# META     }
# META   }
# META }

# MARKDOWN ********************

# #### Helper Functions
# ---
# Notebook to host common classes / functions to support read activities across the medallion layers

# CELL ********************

def read_dataframe(lakehouse_name: str, data_provider: str = None, data_feed: str = None, schema_version: str = None, trigger_time: str = None, table_name: str = None, required_fields: list = None) -> DataFrame:
    """Reads parquet files into Spark Dataframes. Function supports reading from either parquet or delta format."""
    root_abfs_path = get_lakehouse_abfs_path(lakehouse_name)
    if lakehouse_name != globals()['global_configs']['conformed_lh_name']:
        meta_effective_date = trigger_time[:10].replace('-', '')
        read_path = f"{root_abfs_path}/Files/Lake/{data_provider}/{data_feed}/schema_version={schema_version}/meta_effective_date={meta_effective_date}" 
        try:
            return spark.read.format('parquet').load(read_path).select(*required_fields if required_fields else '*')
        except AnalysisException as e:
            # TODO - refactor the below
            delta_tables = ['incident', 'u_inf_generic_request', 'sc_req_item', 'sc_task', 'sys_audit', 'task_sla', 'cmdb_ci_appl', 'asmt_assessment_instance', 'asmt_assessment_instance_question']
            if ('PATH_NOT_FOUND' in e.stackTrace) and (data_feed in e.stackTrace) and (data_feed in delta_tables):
                # this is for cases where ServiceNow ticket tables generating no records in last 24 hours - prevents failure in pipelines
                print(f'No data for {data_feed} at {read_path}. Returning empty df')
                fields = [StructField(row['to'], row['dataType'], True) for row in globals()[f'schema_{data_feed}_v{schema_version}']]
                metadata_fields = [StructField(row, StringType() if row in ['SourceSystem', 'TableName'] else TimestampType(), True) for row in globals()['global_configs']['metadata_fields']]
                return spark.createDataFrame([], schema = StructType(fields + metadata_fields))
            else:
                raise Exception(f'Error reading {read_path}: {e}')
    else:
        table = f'{table_name}_sv_{schema_version}'
        read_path = f"abfss://{globals()['global_configs']['workspace_name']}@onelake.dfs.fabric.microsoft.com/{lakehouse_name}.Lakehouse/Tables/{table}"
        return DeltaTable.forPath(spark, read_path).toDF().select(*required_fields if required_fields else '*')


def read_all_required_dataframes(required_tables: dict, schema: list, trigger_time: str, all_fields: bool = True) -> dict:
  """Read all required tables into dataframes stored in a common dictionary. Used within Conformed layers to read cleansed tables or other conformed tables."""
  df_dicts = {}
  for layer in required_tables.keys():
      if required_tables[layer]:
          for provider in required_tables[layer].keys():
              for table in required_tables[layer][provider]:
                  if not required_tables[layer][provider][table].get('pii_sequence', None):
# Process schema configuration to determine which fields to read from the table:- Extracts field names from the schema configuration
# - If a field value is a list (multiple source fields map to one target), flatten it into individual fields
# - When all_fields=False, this creates an optimized read by selecting only needed columns from the source table
                      if not all_fields:
                          fields = []
                          for f in schema:
                              field = f['from'].get(table)
                              if field:
                                  if isinstance(field, list):
                                      fields.extend(field)
                                  else:
                                      fields.append(field)
                          required_fields = list(set(fields))  # Convert to list of unique fields
                      else:
                          required_fields = None

                      df_dicts[f'{table}'] = read_dataframe(
                          lakehouse_name = globals()['global_configs'][f'{layer}_lh_name'],
                          data_provider = globals()[provider]['name'] if layer == 'cleansed' else None,
                          data_feed = table if layer == 'cleansed' else None,
                          table_name = table if layer == 'conformed' else None,
                          schema_version= required_tables[layer][provider][table]['schema_version'],
                          trigger_time = trigger_time,
                          required_fields = required_fields
                      )
  return df_dicts


def read_csv_from_abfs(abfs_path, folder_path):
    """
    Reads a CSV file from Azure Blob File System (ABFS) into a Spark DataFrame.

    Parameters:
    abfs_path (str): The base path to the ABFS.
    folder_path (str): The specific folder path within the ABFS where the CSV file is located.

    Returns:
    DataFrame: A Spark DataFrame containing the data from the CSV file.

    Raises:
    ValueError: If there is an issue with reading the CSV file.
    """

    file_path = f"{abfs_path}{folder_path}"

    try:
        df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(file_path)

        return df
    except Exception as e:
        raise ValueError(f"An error occurred while reading the CSV file from {file_path}: {e}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def read_dataframe_batches(  
  lakehouse_name: str,   
  data_provider: str,   
  data_feed: str,   
  schema_version: str,   
  trigger_time: str  
) -> DataFrame:  
  """  
  Reads all batch parquet files for a given data feed and combines them into a single DataFrame.  

  Args:  
      lakehouse_name (str): Name of the lakehouse  
      data_provider (str): Name of the data provider (e.g., 'ActiveDirectory')  
      data_feed (str): Name of the data feed (e.g., 'users')  
      schema_version (str): Schema version  
      trigger_time (str): Trigger time in format 'YYYY-MM-DD HH:MM:SS'  

  Returns:  
      DataFrame: Combined DataFrame from all batch files  
  """  
  try:  
      root_abfs_path = get_lakehouse_abfs_path(lakehouse_name)  
      meta_effective_date = trigger_time[:10].replace('-', '')  
      base_path = f"{root_abfs_path}/Files/Lake/{data_provider}"  

      # Set the appropriate batch pattern based on data_feed  
      if data_feed.lower() == 'users':  
          batch_pattern = f"{base_path}/users_batch_*/schema_version={schema_version}/meta_effective_date={meta_effective_date}/*"  
      elif data_feed.lower() == 'groups':  
          batch_pattern = f"{base_path}/groups_batch_*/schema_version={schema_version}/meta_effective_date={meta_effective_date}/*"  
      else:  
          raise ValueError(f"Unsupported data_feed: {data_feed}. Supported values are 'users' and 'groups'")  

      print(f"Reading from path: {batch_pattern}")  # Debug print  

      # Try to read all batch files  
      try:  
          df = spark.read.format('parquet').load(batch_pattern)  

          # Count total records  
          total_records = df.count()  
          print(f"Successfully read all batch files")  
          print(f"Total records: {total_records}")  
          print(f"Columns in DataFrame: {df.columns}")  # Debug print  

          return df  

      except AnalysisException as e:  
          if 'PATH_NOT_FOUND' in str(e):  
              print(f"No batch data found at {batch_pattern}")  
              # Create empty DataFrame with appropriate schema  
              schema_var = f'schema_{data_feed}_v{schema_version}'  
              if schema_var in globals():  
                  fields = [  
                      StructField(row['to'], row['dataType'], True)   
                      for row in globals()[schema_var]  
                  ]  
                  metadata_fields = [  
                      StructField(row,   
                                StringType() if row in ['SourceSystem', 'TableName'] else TimestampType(),   
                                True)   
                      for row in globals()['global_configs']['metadata_fields']  
                  ]  
                  schema = StructType(fields + metadata_fields)  
              else:  
                  raise ValueError(f"Cannot determine schema for {data_feed}. Schema variable {schema_var} not found.")  

              return spark.createDataFrame([], schema=schema)  
          else:  
              raise Exception(f"Error reading batch data from {batch_pattern}: {str(e)}")  

  except Exception as e:  
      raise Exception(f"Failed to read batch data: {str(e)}")  

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### <u>Service Now API Reader</u>

# CELL ********************

class ServiceNowReader:
    def __init__(self, user_name: str, password: str, table_name: str, load_type: str, historical: bool = False):
        """
        Initialize ServiceNowReader instance.

        :param user_name: Username.
        :param password: Password.
        :param table_name: The name of the ServiceNow table to read.
        :param load_type: Accepts either 'full' or 'delta' loads
        :param historical: Boolean to determine if historical
        """

        env_mappings = {
            'dev': 'dev',
            'sit': 'test',
            'uat': '',
            'prd': '',
        }

        # define attributes
        self.table_name = table_name
        self.load_type = load_type
        self.historical = historical
        self.api_record_limit = 1000
        self.limit_non_prod = 5000
        self.retries = 10
        self.env = globals()['global_configs']['env']
        self.base_url = f"https://informa{env_mappings.get(self.env, 'dev')}.service-now.com/api/now/"
        self.auth = HTTPBasicAuth(user_name, password)
        self.headers = {"Accept": "application/json"}

 
    def get_data_paged(self, required_fields: list, from_date: str, to_date: str) -> List[Dict[str, str]]:
        """Get paged data from the ServiceNow API."""
        
        if self.historical:
            sysparm_query = f'sys_created_onBETWEEN{from_date}@{to_date}^ORDERBYsys_id'
        elif self.load_type == 'delta':
            sysparm_query = f'sys_created_onBETWEEN{from_date}@{to_date}^ORsys_updated_onBETWEEN{from_date}@{to_date}^ORDERBYsys_id'
        elif self.load_type == 'full':
            sysparm_query = ''
        else:
            raise Exception(f'Unknown load type {self.load_type}')

        # Add u_active=True filter for cmdb_rel_ci table and active=True for cmdb_ci_service table
        if self.table_name in ['cmdb_rel_ci', 'cmdb_ci_service']:
            filter_condition = 'u_active=true' if self.table_name == 'cmdb_rel_ci' else 'active=true'
            if sysparm_query:
                sysparm_query += f'^{filter_condition}'
            else:
                sysparm_query = filter_condition

        # Add ORDERBYsys_id at the end of the query
        sysparm_query += '^ORDERBYsys_id'

        # define query parameters
        query_params = {
            'sysparm_limit': self.api_record_limit, 
            'sysparm_display_value': 'all', 
            'sysparm_fields': [required_fields], 
            'sysparm_suppress_pagination_header': True, 
            'sysparm_query': sysparm_query
            }
        print(f"{self.table_name.upper()} ingestion method: {self.historical if self.historical else self.load_type.upper()}. Filtered for: '{query_params['sysparm_query']}'")
        
        # count number of records to ingest
        count = int(requests.get(
            f"{self.base_url}/stats/{self.table_name}", 
            headers=self.headers, 
            auth=self.auth, 
            params={'sysparm_count': True, 'sysparm_query': query_params['sysparm_query']}
            ).json()['result']['stats']['count'])
        print(f'Total records to ingest: {count}')
        
        # extracting paginated data from API
        results = []

        while True:
            if self.env in ('dev', 'sit') and len(results) >= self.limit_non_prod:
                print(f'Extraction in {self.env} environment limited to {self.limit_non_prod} records')
                break

            attempts = 0
            while attempts < self.retries:
                try:
                    response = requests.get(f"{self.base_url}/table/{self.table_name}", headers=self.headers, auth=self.auth, params=query_params)

                    if response.status_code != 200:
                        raise Exception(f"{response.status_code}, {response.text}")

                    data = response.json().get('result', [])
                    break  # Exit the retry loop on success

                except Exception as e:
                    attempts += 1
                    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Attempt {attempts} failed at offset {query_params.get('sysparm_offset', 0)}: {e}")
                    if attempts >= self.retries:
                        try:
                            data = json.loads(response.text.replace(',""', '')).get('result', [])
                            print(f"Fixing malformed json at offset {query_params.get('sysparm_offset', 0)}")
                            break
                        except Exception as e:
                            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Max retries reached. Exiting.")
                            raise e
                    else:
                        time.sleep(10)  # Optional: Add delay before retrying
            
            results.extend(data)

            is_pagination_complete = not data
            if is_pagination_complete:
                print(f"Completed ingestion of: {len(results)} records")     
                break

            query_params['sysparm_offset'] = query_params.get('sysparm_offset', 0) + self.api_record_limit
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Records retrieved for offset {query_params.get('sysparm_offset', len(data))}: {len(data)} / Total records ingested so far: {len(results)} / Remaining: {count - len(results)}")

        return results


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### <u>LeanIX API Reader</u>

# CELL ********************

class GraphQLAPIClient:
    def __init__(self, api_token: str, graphql_query: str):
        """
        Initialize GraphQL API client.

        Args:
        - api_token (str): API token for authentication.
        - graphql_query (str): GraphQL query to execute.
        """

        self.api_token = api_token
        self.graphql_query = graphql_query
        self.session = requests.Session()
        self.access_token = self._obtain_access_token()
        
        # Initialize Spark session
        self.spark = SparkSession.builder.appName("GraphQLAPIClient").getOrCreate()

    def _obtain_access_token(self) -> str:
        """Obtains an access token using the API token."""
        oauth2_url = f'https://informa.leanix.net/services/mtm/v1/oauth2/token'
        response = self.session.post(
            oauth2_url,
            auth=("apitoken", self.api_token),
            data={"grant_type": "client_credentials"},
        )
        response.raise_for_status()
        return response.json().get('access_token')

    def execute_graphql_query(self) -> dict:
        """Executes the stored GraphQL query and returns the response."""
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        response = self.session.post(
            url="https://informa.leanix.net/services/pathfinder/v1/graphql",
            headers=headers,
            json={'query': self.graphql_query}
        )
        response.raise_for_status()
        return response.json()

    def extract_edges_to_spark_dataframe(self, data: dict):
        """
        Extracts edges from the GraphQL response data and converts them into a Spark DataFrame.

        Args:
        - data (dict): The response data from a GraphQL query.

        Returns:
        - pyspark.sql.DataFrame: Spark DataFrame containing the extracted edges.
        """
        # Extract edges from the input dictionary
        edges = data.get('data', {}).get('allFactSheets', {}).get('edges', [])
        
        # Prepare a list to hold node data
        node_list = []
        
        # Loop through each edge and extract node data
        for edge in edges:
            node = edge.get('node', {})
            node_str = {}
            
            # Loop through each key-value pair in the node and cast to string
            for key, value in node.items():
                if isinstance(value, (dict, list)):
                    node_str[key] = str(value)
                elif value is None:
                    node_str[key] = ''
                else:
                    node_str[key] = str(value)
            
            node_list.append(Row(**node_str))
        
        # Create a Spark DataFrame from the list of node data
        df = self.spark.createDataFrame(node_list)
        
        return df

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### <u>Coupa API Reader</u>

# CELL ********************

class CoupaReader:  
    def __init__(self, client_id: str, api_token: str, table_name: str):  
        """  
        Initialize CoupaReader instance with improved retry and timeout handling.  
        """  
        env_mappings = {  
            'dev': '-test',  
            'sit': '-test',  
            'uat': '',  
            'prd': '',  
        }  

        self.env = globals()['global_configs']['env']  
        self.base_url = f"https://informa{env_mappings.get(self.env, 'dev')}.coupahost.com"  
        self.client_id = client_id  
        self.api_token = api_token  
        self.table_name = table_name  
        self.limit_non_prod = 1000  
        self.batch_size = 50  

        # Configure retry strategy  
        self.session = self._create_session()  
        self.access_token = self.get_api_token()  

    def _create_session(self) -> requests.Session:  
        """Create a session with retry strategy."""  
        session = requests.Session()  

        retry_strategy = Retry(  
            total=3,  # number of retries  
            backoff_factor=1,  # wait 1, 2, 4 seconds between retries  
            status_forcelist=[429, 500, 502, 503, 504],  # HTTP status codes to retry on  
            allowed_methods=["GET", "POST"]  
        )  

        adapter = HTTPAdapter(max_retries=retry_strategy)  
        session.mount("https://", adapter)  
        session.mount("http://", adapter)  

        return session  

    def get_api_token(self) -> str:  
        """Retrieves an API token with improved error handling."""  
        headers = {  
            "Content-Type": "application/x-www-form-urlencoded",  
            "Authorization": f"Basic {base64.b64encode(f'{self.client_id}:{self.api_token}'.encode()).decode()}"  
        }  

        data = {  
            "grant_type": "client_credentials",  
            "scope": f"core.{self.table_name[:-1]}.read",  
            "client_id": self.client_id,  
            "client_secret": self.api_token  
        }  

        try:  
            response = self.session.post(  
                f"{self.base_url}/oauth2/token",  
                headers=headers,  
                data=data,  
                timeout=(10, 30)  # (connect timeout, read timeout)  
            )  
            response.raise_for_status()  
            return response.json()["access_token"]  
        except requests.exceptions.RequestException as e:  
            print(f"Error getting API token: {e}")  
            raise  

    def make_api_call(self, fields: List[str]) -> List[Dict[str, Any]]:  
        """Makes API calls with improved error handling and retry logic."""  
        headers = {'Authorization': f'Bearer {self.access_token}', 'Accept': 'application/json'}  

        offset = 0  
        results = []  
        max_iterations = 1000  
        current_iteration = 0  
        max_retries = 3  

        while current_iteration < max_iterations:  
            if self.env in ('dev', 'sit') and len(results) >= self.limit_non_prod:  
                print(f'Extraction in {self.env} environment limited to {self.limit_non_prod} records.')  
                break  

            retry_count = 0  
            while retry_count < max_retries:  
                try:  
                    response = self.session.get(  
                        f'{self.base_url}/api/{self.table_name}',  
                        params={  
                            'offset': offset,  
                            'fields': json.dumps(fields),  
                            'limit': self.batch_size  
                        },  
                        headers=headers,  
                        timeout=(10, 120)  # Increased timeouts (connect, read)  
                    )  
                    response.raise_for_status()  
                    data = response.json()  

                    if not data:  
                        print(f"No more data to fetch. Total records ingested: {len(results)}")  
                        return results  

                    results.extend(data)  

                    if len(data) < self.batch_size:  
                        print(f"Completed the ingestion of {self.table_name} records: {len(results)}")  
                        return results  

                    offset += self.batch_size  
                    current_iteration += 1  
                    print(f"Records ingested so far: {len(results)}")  

                    # Adaptive delay based on environment  
                    delay = 0.5 if self.env in ('dev', 'sit') else 0.2  
                    time.sleep(delay)  

                    break  # Success, exit retry loop  

                except requests.exceptions.Timeout:  
                    retry_count += 1  
                    if retry_count == max_retries:  
                        print(f"Failed after {max_retries} retries due to timeout")  
                        raise  
                    print(f"Timeout occurred. Retry attempt {retry_count} of {max_retries}")  
                    time.sleep(retry_count * 2)  # Exponential backoff  

                except requests.exceptions.RequestException as e:  
                    print(f"Error during API call: {e}")  
                    raise  

        print("Reached maximum iterations. Stopping ingestion to prevent infinite loop.")  
        return results  

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### <u>Smartsheet API Reader</u>

# CELL ********************

class SmartsheetReader:
  def __init__(self, api_token, sheet_id):
      self.api_token = api_token
      self.sheet_id = sheet_id
      self.base_url = source_configs['api_base_url']
      self.timeout = source_configs['timeout']

  def get_sheet_data(self):
      url = f"{self.base_url}/sheets/{self.sheet_id}"
      headers = {
          "Authorization": f"Bearer {self.api_token}",
          "Content-Type": "application/json"
      }
      
      response = requests.get(url, headers=headers, timeout=self.timeout)
      response.raise_for_status()
      
      return response.json()

  def process_sheet_data(self, sheet_data):
      """
      Process sheet data into a list of dictionaries suitable for lakehouse writing.
      """
      if 'rows' not in sheet_data or 'columns' not in sheet_data:
          return []
      
      columns = [col['title'] for col in sheet_data['columns']]
      processed_data = []
      
      for row in sheet_data['rows']:
          row_dict = {columns[i]: cell.get('value', '') for i, cell in enumerate(row['cells'])}
          row_dict['sheet_id'] = sheet_data['id']
          row_dict['sheet_name'] = sheet_data['name']
          processed_data.append(row_dict)
      
      return processed_data

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def check_table_exists(table_path: str) -> bool:
    """
    Check if a specified table exists within a given ABFS path.

    This function attempts to check the existence of a table by using the Delta Lake API.
    If the table exists, it returns True; otherwise, it returns False. In the case of exceptions,
    meaningful messages are printed to provide context.

    Args:
        table_path (str): The full ABFS path to the table, including lakehouse and table name.
    
    Returns:
        bool: True if the table exists, False if it does not or if an error occurs.
    """
    
    print(f"Checking existence at: {table_path}")

    try:
        DeltaTable.forPath(spark, table_path)
        return True
    except AnalysisException as e:
        if 'Table or view not found' in str(e):
            print(f"Table does not exist at {table_path}.")
            return False
        else:
            print(f"Error checking existence for {table_path}: {str(e)}")
            return False

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### <u>Service Now Test API Reader - used by BAs</u>

# CELL ********************

class ServiceNowTestReader:
    def __init__(self, user_name: str, password: str, table_name: str, load_type: str, historical: bool = False):
        """
        Initialize ServiceNowReader instance.

        :param user_name: Username.
        :param password: Password.
        :param table_name: The name of the ServiceNow table to read.
        :param load_type: Accepts either 'full' or 'delta' loads
        :param historical: Boolean to determine if historical
        """

        env_mappings = {
            'dev': 'dev',
            'sit': 'test',
            'uat': '',
            'prd': '',
        }

        # define attributes
        self.table_name = table_name
        self.load_type = load_type
        self.historical = historical
        self.api_record_limit = 1000
        self.limit_non_prod = 500
        self.retries = 10
        self.env = globals()['global_configs']['env']
        self.base_url = f"https://informa{env_mappings.get(self.env, 'dev')}.service-now.com/api/now/"
        self.auth = HTTPBasicAuth(user_name, password)
        self.headers = {"Accept": "application/json"}

 
    def get_data_paged(self, from_date: str, to_date: str) -> List[Dict[str, str]]:
        """Get paged data from the ServiceNow API."""
        
        if self.historical:
            sysparm_query = f'sys_created_onBETWEEN{from_date}@{to_date}^ORDERBYsys_id'
        elif self.load_type == 'delta':
            sysparm_query = f'sys_created_onBETWEEN{from_date}@{to_date}^ORsys_updated_onBETWEEN{from_date}@{to_date}^ORDERBYsys_id'
        elif self.load_type == 'full':
            sysparm_query = ''
        else:
            raise Exception(f'Unknown load type {self.load_type}')

        # Add u_active=True filter for cmdb_rel_ci table and active=True for cmdb_ci_service table
        if self.table_name in ['cmdb_rel_ci', 'cmdb_ci_service']:
            filter_condition = 'u_active=true' if self.table_name == 'cmdb_rel_ci' else 'active=true'
            if sysparm_query:
                sysparm_query += f'^{filter_condition}'
            else:
                sysparm_query = filter_condition

        # Add ORDERBYsys_id at the end of the query
        sysparm_query += '^ORDERBYsys_id'

        # define query parameters
        query_params = {
            'sysparm_limit': self.api_record_limit, 
            'sysparm_display_value': 'all', 
            'sysparm_suppress_pagination_header': True, 
            'sysparm_query': sysparm_query
            }
        print(f"{self.table_name.upper()} ingestion method: {self.historical if self.historical else self.load_type.upper()}. Filtered for: '{query_params['sysparm_query']}'")
        
        # count number of records to ingest
        count = int(requests.get(
            f"{self.base_url}/stats/{self.table_name}", 
            headers=self.headers, 
            auth=self.auth, 
            params={'sysparm_count': True, 'sysparm_query': query_params['sysparm_query']}
            ).json()['result']['stats']['count'])
        print(f'Total records to ingest: {count}')
        
        # extracting paginated data from API
        results = []

        while True:
            if self.env in ('dev', 'sit') and len(results) >= self.limit_non_prod:
                print(f'Extraction in {self.env} environment limited to {self.limit_non_prod} records')
                break

            attempts = 0
            while attempts < self.retries:
                try:
                    response = requests.get(f"{self.base_url}/table/{self.table_name}", headers=self.headers, auth=self.auth, params=query_params)

                    if response.status_code != 200:
                        raise Exception(f"{response.status_code}, {response.text}")

                    data = response.json().get('result', [])
                    break  # Exit the retry loop on success

                except Exception as e:
                    attempts += 1
                    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Attempt {attempts} failed at offset {query_params.get('sysparm_offset', 0)}: {e}")
                    if attempts >= self.retries:
                        try:
                            data = json.loads(response.text.replace(',""', '')).get('result', [])
                            print(f"Fixing malformed json at offset {query_params.get('sysparm_offset', 0)}")
                            break
                        except Exception as e:
                            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Max retries reached. Exiting.")
                            raise e
                    else:
                        time.sleep(10)  # Optional: Add delay before retrying
            
            results.extend(data)

            if query_params.get('sysparm_offset', 0) >= count:
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Completed ingestion of: {len(results)} records. Remaining records not accounted for: {count - len(results)}")
                break

            query_params['sysparm_offset'] = query_params.get('sysparm_offset', 0) + self.api_record_limit
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Records retrieved for offset {query_params.get('sysparm_offset', len(data))}: {len(data)} / Total records ingested so far: {len(results)} / Remaining: {count - len(results)}")

        return results


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### <u>Oracle HR API Reader</u>

# CELL ********************

class OracleReader:
  def __init__(self, client_id, api_token, table_name):
      """
      Initialize OracleReader instance.
 
      :param client_id: The client ID for the Oracle API.
      :param api_token: The API token (client secret) for the Oracle API.
      :param table_name: The table to extract from Oracle API.
      """
      self.client_id = client_id
      self.api_token = api_token
      self.table_name = table_name
      self.access_token = None
      
      # Oracle API setup - get values from KeyVault
      self.scope = extract_secret(source_configs['api-oracle-scope'])
      self.base_url = extract_secret(source_configs['api-oracle-url'])
      self.token_url = extract_secret(source_configs['api-oracle-token-url'])
 
  def get_access_token(self):
      """Retrieves an access token using the provided credentials."""
      data = {
          'grant_type': 'client_credentials',
          'scope': self.scope
      }
      response = requests.post(self.token_url, auth=HTTPBasicAuth(self.client_id, self.api_token), data=data)
      if response.status_code == 200:
          self.access_token = response.json()['access_token']
      else:
          raise Exception(f"Failed to retrieve access token: {response.text}")
 
  def make_api_call(self):
      """Makes an API call to the specified endpoint."""
      if not self.access_token:
          self.get_access_token()
 
      headers = {
          'Authorization': f'Bearer {self.access_token}',
          'Accept': 'application/json'
      }
      
      # Construct the API URL based on the table name
      api_url = f"{self.base_url}/EMPLOYEEDETAILSINTERFACE/1.0/{self.table_name.capitalize()}"
     
      
      response = requests.get(api_url, headers=headers)
      if response.status_code == 200:
          return response.json()
      else:
          raise Exception(f"API call failed for {self.table_name}: {response.status_code} - {response.text}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### <u>Sap HR API Reader</u>

# CELL ********************

class SapHrReader:
  def __init__(self, username, password, api_base_url):
      """
      Initialize SapHrReader instance.
      
      :param username: The username for SAP HR API authentication
      :param password: The password for SAP HR API authentication
      :param api_base_url: The base URL for the SAP HR API
      """
      self.auth = HTTPBasicAuth(username, password)
      self.api_base_url = api_base_url
      self.headers = {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
      }

  def make_api_call(self):
      """
      Makes an API call to the specified endpoint.
      
      :return: JSON response from the API
      :raises: Exception if the API call fails
      """
      try:
          response = requests.get(
              self.api_base_url,
              auth=self.auth,
              headers=self.headers
          )
          response.raise_for_status()
          return response.json()
      except requests.exceptions.RequestException as e:
          raise Exception(f"Failed to fetch data: {str(e)}")

  def get_data(self):
      """
      Gets data from the SAP HR API and returns it in the required format.
      
      :return: List of results from the API
      :raises: Exception if the response format is unexpected
      """
      response_data = self.make_api_call()
      try:
          if 'd' in response_data and 'results' in response_data['d']:
              return response_data['d']['results']
          else:
              raise Exception("Unexpected API response format")
      except (KeyError, TypeError) as e:
          raise Exception(f"Failed to parse API response: {str(e)}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### <u>Azure Active Directory API Reader</u>

# CELL ********************

class ActiveDirectoryReader:
  API_BASE_URL = "https://graph.microsoft.com/v1.0"
  TIMEOUT = 300
  PAGE_SIZE = 999  # Microsoft Graph API limits to 999 items per page
  MAX_WORKERS = 5 # Number of concurrent threads for processing users

  def __init__(self, tenant_id, client_id, client_secret, max_workers=None):
      if not all([tenant_id, client_id, client_secret]):
          raise ValueError("tenant_id, client_id, and client_secret are required")

      self.tenant_id = tenant_id
      self.client_id = client_id
      self.client_secret = client_secret
      self.token = None
      self.headers = None
      self.token_url = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token"
      self.retries = 3
      self.max_workers = max_workers or self.MAX_WORKERS # Allow override of default MAX_WORKERS through constructor

      # Setup session with retry strategy. Retry these status codes up to 3 times with exponential backoff (1s, 2s, 4s between retries)
      self.session = requests.Session()
      retry_strategy = Retry(
          total=3,
          backoff_factor=1,
          # Setup session with retry strategy for handling common HTTP errors:
          status_forcelist=[429, 500, 502, 503, 504]
      )
      self.session.mount("https://", HTTPAdapter(max_retries=retry_strategy))

  def get_access_token(self):
      """Get access token for Microsoft Graph API."""
      payload = {
          'client_id': self.client_id,
          'scope': 'https://graph.microsoft.com/.default',
          'client_secret': self.client_secret,
          'grant_type': 'client_credentials'
      }

      try:
          response = self.session.post(
              self.token_url, 
              data=payload, 
              timeout=self.TIMEOUT
          )
          response.raise_for_status()

          token_data = response.json()
          if 'access_token' not in token_data:
              raise ValueError("No access token in response")

          self.token = token_data['access_token']
          self.headers = {
              'Authorization': f'Bearer {self.token}',
              'Content-Type': 'application/json'
          }
          return self.token

      
      except requests.exceptions.HTTPError as e:
          print(f"HTTP Error occurred: {e}")
          print(f"Response content: {response.text}")
          raise
      except requests.exceptions.RequestException as e:
          print(f"Error occurred while getting access token: {e}")
          raise
      except ValueError as e:
          print(f"Error in token response: {e}")
          raise

  def get_user_groups(self, user_principal_name):
      """Get detailed group information for a specific user."""
      groups_url = f"{self.API_BASE_URL}/users/{user_principal_name}/memberOf"
      params = {
          '$select': 'displayName'
      }

      try:
          response = self.session.get(
              groups_url, 
              headers=self.headers, 
              params=params,
              timeout=self.TIMEOUT
          )
          response.raise_for_status()
          return response.json().get('value', [])
      except requests.exceptions.RequestException:
          return []

  def get_user_manager(self, user_id):
      """Get manager for a specific user."""
      manager_url = f"{self.API_BASE_URL}/users/{user_id}/manager"
      try:
          response = self.session.get(
              manager_url, 
              headers=self.headers, 
              timeout=self.TIMEOUT
          )
          if response.status_code == 404:
              return None
          response.raise_for_status()
          manager = response.json()
          return manager.get('userPrincipalName')
      except requests.exceptions.RequestException:
          return None

  def get_user_extension_attributes(self, user_principal_name):
      """Get extension attributes for a specific user."""
      url = f"{self.API_BASE_URL}/users/{user_principal_name}"
      params = {'$select': 'onPremisesExtensionAttributes'}

      try:
          response = self.session.get(
              url, 
              headers=self.headers, 
              params=params, 
              timeout=self.TIMEOUT
          )
          response.raise_for_status()
          user_data = response.json()
          return user_data.get('onPremisesExtensionAttributes', {}).get('extensionAttribute10')
      except requests.exceptions.RequestException:
          return None

  def _get_paginated_data(self, url, params=None):
      """Helper method to handle pagination for Microsoft Graph API."""
      if not self.headers:
          self.get_access_token()

      all_data = []
      next_link = url

      while next_link:
          attempts = 0
          while attempts < self.retries:
              try:
                  if params and next_link == url:  # Only add params for the first request
                      response = self.session.get(
                          next_link,
                          headers=self.headers,
                          params=params,
                          timeout=self.TIMEOUT
                      )
                  else:
                      response = self.session.get(
                          next_link,
                          headers=self.headers,
                          timeout=self.TIMEOUT
                      )

                  response.raise_for_status()
                  data = response.json()

                  # Add the current page of results
                  if 'value' in data:
                      all_data.extend(data['value'])

                  # Update the next_link for pagination
                  next_link = data.get('@odata.nextLink')

                  print(f"Retrieved {len(all_data)} records so far...")
                  break  # Exit retry loop on success

              except requests.exceptions.RequestException as e:
                  attempts += 1
                  print(f"Attempt {attempts} failed: {str(e)}")
                  if attempts >= self.retries:
                      print("Max retries reached. Moving to next page.")
                      break
                  time.sleep(5)  # Wait before retrying

      return all_data

  def get_all_groups_data(self):  
        """Get all groups data from Azure AD with their members using batch requests"""  
        if not self.headers:  
            self.get_access_token()  

        # Get all groups first  
        groups_url = f"{self.API_BASE_URL}/groups"  
        params = {  
            '$select': 'id,displayName',  
            '$top': self.PAGE_SIZE  
        }  

        groups = self._get_paginated_data(groups_url, params)  
        processed_groups = []  

        # Process groups in larger batches  
        batch_size = 20  # Number of groups to process in parallel  
        for i in range(0, len(groups), batch_size):  
            group_batch = groups[i:i + batch_size]  

            # Create batch request for members  
            batch_requests = []  
            for group in group_batch:  
                if group.get('id'):  
                    batch_requests.append({  
                        'url': f"/groups/{group.get('id')}/members?$select=userPrincipalName",  
                        'method': 'GET',  
                        'id': group.get('id')  
                    })  

            # Execute batch request  
            if batch_requests:  
                batch_url = f"{self.API_BASE_URL}/$batch"  
                batch_payload = {'requests': batch_requests}  

                try:  
                    response = self.session.post(  
                        batch_url,  
                        headers=self.headers,  
                        json=batch_payload,  
                        timeout=self.TIMEOUT  
                    )  
                    response.raise_for_status()  
                    batch_responses = response.json().get('responses', [])  

                    # Process batch responses  
                    for resp in batch_responses:  
                        if resp.get('status') == 200:  
                            group_id = resp.get('id')  
                            group_name = next((g['displayName'] for g in group_batch if g['id'] == group_id), None)  

                            members = resp.get('body', {}).get('value', [])  
                            for member in members:  
                                if 'userPrincipalName' in member:  
                                    processed_groups.append({  
                                        'UserPrincipalName': member.get('userPrincipalName'),  
                                        'GroupDisplayName': group_name  
                                    })  

                except Exception as e:  
                    print(f"Error processing batch: {str(e)}")  
                    continue  

        return processed_groups      

  def process_user(self, user):
      """Process a single user"""
      try:
          upn = user.get('userPrincipalName')
          if not upn:
              return None

          # Only get additional data if user is not deleted
          if not user.get('deletedDateTime'):
              groups = self.get_user_groups(upn)
              groups_str = ';'.join([g.get('displayName', '') for g in groups]) if groups else None
              manager_upn = self.get_user_manager(user.get('id'))
              ext_attr = self.get_user_extension_attributes(upn)
          else:
              groups_str = None
              manager_upn = None
              ext_attr = None

          return {
              'UserPrincipalName': upn,
              'DisplayName': user.get('displayName'),
              'DeletedDateTime': user.get('deletedDateTime'),
              'ManagerUPN': manager_upn,
              'ExtensionAttribute10': ext_attr,
              'AllGroups': groups_str
          }
      except Exception as e:
          print(f"Error processing user {upn}: {str(e)}")
          return None

  def get_all_users_data_batched(self, batch_size=2000):
    """Get all users data in batches with parallel processing"""
    if not self.headers:
        self.get_access_token()

    # Get deleted users first
    print("Fetching deleted users...")
    deleted_users = self._get_paginated_data(
        f"{self.API_BASE_URL}/directory/deletedItems/microsoft.graph.user",
        {'$select': 'userPrincipalName,displayName,deletedDateTime'}
    )
    print(f"Total deleted users found: {len(deleted_users)}")

    # Get active users
    print("Fetching active users...")
    active_users = self._get_paginated_data(
        f"{self.API_BASE_URL}/users",
        params={
            '$select': 'id,userPrincipalName,displayName',
            '$top': self.PAGE_SIZE
        }
    )
    print(f"Total active users found: {len(active_users)}")

    # Prepare combined user list
    all_users = [
        {**user, 'deletedDateTime': user.get('deletedDateTime')}
        for user in deleted_users
    ] + active_users

    # Process and yield users in batches
    total_processed = 0
    with ThreadPoolExecutor(max_workers=self.max_workers) as executor:  # Recommended number of workers
        for i in range(0, len(all_users), batch_size):
            batch_users = all_users[i:i + batch_size]
            print(f"Processing batch {(i//batch_size)+1} of {len(all_users)//batch_size + 1}")

            # Process batch in parallel
            futures = [executor.submit(self.process_user, user) 
                        for user in batch_users]

            # Collect results for current batch
            batch_results = []
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:
                    batch_results.append(result)

            total_processed += len(batch_results)
            print(f"Processed {total_processed} users out of {len(all_users)}")

            if batch_results:
                yield batch_results

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

class TempoReader:
    def __init__(self, username: str, password: str, api_base_url: str):
        """
        Initialize TempoReader instance with Basic Auth authentication.
        """
        self.username = username
        self.password = password
        self.api_base_url = api_base_url.split('#!/')[0].rstrip('/')
        self.session = self._create_session()

        credentials = base64.b64encode(f"{self.username}:{self.password}".encode()).decode()
        self.headers = {
            "Authorization": f"Basic {credentials}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        self.endpoints = {
            'tempo_worklogs': 'rest/tempo-timesheets/4/worklogs',
            'tempo_accounts': 'rest/tempo-accounts/1/account',
            'tempo_teams': 'rest/tempo-teams/2/team',
            'tempo_customers': 'rest/tempo-core/1/customers',
            'tempo_plans': 'rest/tempo-planning/1/plans',
            'tempo_programs': 'rest/tempo-core/1/programs'
        }

    def _create_session(self) -> requests.Session:
        """
        Create a session with retry strategy.
        """
        session = requests.Session()
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("https://", adapter)
        return session

    def make_api_call(self, endpoint: str, params: dict = None) -> List[Dict[str, Any]]:
        """
        Make API call to Tempo endpoint with pagination handling.
        """
        url = f"{self.api_base_url}/{endpoint}"
        results = []

        # Debug logging
        print(f"Making request to URL: {url}")
        print(f"Headers: {self.headers}")
        print(f"Params: {params}")

        while url:
            try:
                response = self.session.get(
                    url,
                    headers=self.headers,
                    params=params,
                    timeout=(10, 60)
                )

                # Debug response
                print(f"Response status code: {response.status_code}")
                print(f"Response headers: {response.headers}")
                print(f"Response content: {response.text[:500]}...")

                response.raise_for_status()

                try:
                    data = response.json()
                except ValueError as e:
                    print(f"Failed to parse JSON response: {str(e)}")
                    print(f"Full response content: {response.text}")
                    raise

                # Handle pagination
                if isinstance(data, dict) and "results" in data:
                    results.extend(data["results"])
                    # Check for next page
                    if "metadata" in data and "next" in data["metadata"]:
                        url = data["metadata"]["next"]
                        params = None  # Parameters are included in the next URL
                    else:
                        url = None
                elif isinstance(data, list):
                    results.extend(data)
                    url = None
                else:
                    results.append(data)
                    url = None

            except requests.exceptions.RequestException as e:
                print(f"Full error response: {e.response.text if hasattr(e, 'response') else 'No response text'}")
                raise Exception(f"Failed to fetch data from {endpoint}: {str(e)}")

        return results

    def get_endpoint_data(self, table_name: str, from_date: str = None, to_date: str = None) -> List[Dict[str, Any]]:
        """
        Get data for a specific endpoint.

        Args:
            table_name: Name of the table/endpoint to fetch data from
            from_date: Start date in YYYY-MM-DD format (for time-based endpoints)
            to_date: End date in YYYY-MM-DD format (for time-based endpoints)

        Returns:
            List of dictionaries containing the endpoint data
        """
        if table_name not in self.endpoints:
            raise ValueError(f"Invalid table_name: {table_name}. Must be one of {list(self.endpoints.keys())}")

        endpoint_path = self.endpoints[table_name]
        params = {}

        if table_name == 'tempo_worklogs' and from_date and to_date:
            params.update({
                "from": from_date,
                "to": to_date,
                "limit": 1000
            })

        return self.make_api_call(endpoint_path, params)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
