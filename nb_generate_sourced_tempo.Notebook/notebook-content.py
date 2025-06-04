# Fabric notebook source - Tempo API Integration Example
# This is an anonymized example for demonstration purposes
# Replace all placeholder values with your actual configuration#
# IMPORTANT: This code contains multiple implementations of TempoReader class
# for different Tempo deployment types (Server/Data Center vs Cloud)
# Choose the appropriate implementation for your environment
#
# Security Note: Never commit actual API keys or credentials to version control
# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

%run nb_helper_functions_parent_caller

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#%run nb_schema_sourced_tempo

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

trigger_time = '2025-01-14'
table_name = 'tempo_accounts'
from_date = None  # Format: YYYY-MM-DD
to_date = None    # Format: YYYY-MM-DD

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

global_configs = globals()['global_configs']
source_configs = globals()['tempo']

table_configs = source_configs['source_tables'][table_name]
#source_schema = globals()[f"schema_{table_name}_v{table_configs['schema_version']}"]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Initialize TempoReader with the base URL (without the configuration part)
reader = TempoReader(
    username=api_username,# NOTE: Replace api_username, api_password with your actual credentials
# These should be stored securely (e.g., in Azure Key Vault, environment variables, etc.)    password=api_password,
    api_base_url='https://your-company.atlassian.net/plugins/servlet/ac/io.tempo.jira/tempo-app'
)

try:
    # Validate table_name
    if table_name not in reader.endpoints:
        raise ValueError(f"Invalid table_name: {table_name}. Must be one of {list(reader.endpoints.keys())}")

    # Get endpoint path for the specified table
    endpoint_path = reader.endpoints[table_name]

    # Get data for specific endpoint
    params = {}
    if table_name == 'worklogs' and from_date and to_date:
        params.update({
            "from": from_date,
            "to": to_date,
            "limit": 1000
        })

    data = reader.make_api_call(endpoint_path, params)

    if data:
        print(f"\nProcessing {table_name}:")
        df = spark.createDataFrame(data)
        display(df)
    else:
        print(f"No data retrieved for {table_name}")

except Exception as e:
    print(f"Error processing Tempo API data: {str(e)}")
    raise

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import base64
import pandas as pd
from typing import List, Dict, Any
import json
# Example TempoReader class for Atlassian Server/Data Center installations
# This class demonstrates how to authenticate using Client ID and Access Keyclass TempoReader:
    def __init__(self, client_id: str, access_key: str, base_url: str):
        """
        Initialize TempoReader with Client ID and Access Key authentication.

        Args:
            client_id (str): The Client ID from Tempo
            access_key (str): The Access Key from Tempo
            base_url (str): The base URL for the Tempo API
        """
        self.client_id = client_id
        self.access_key = access_key
        self.base_url = self._clean_base_url(base_url)
        self.session = self._create_session()

        # Create authentication header using Client ID and Access Key
        credentials = base64.b64encode(f"{self.client_id}:{self.access_key}".encode()).decode()
        self.headers = {
            "Authorization": f"Basic {credentials}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def _clean_base_url(self, url: str) -> str:
        """Clean the base URL by removing unnecessary parts."""
        return url.split('#!/')[0].rstrip('/')

    def _create_session(self) -> requests.Session:
        """Create a session with retry strategy."""
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
        Make API call to Tempo endpoint with detailed error handling and debugging.

        Args:
            endpoint (str): API endpoint to call
            params (dict): Query parameters for the API call

        Returns:
            List[Dict[str, Any]]: List of response data
        """
        url = f"{self.base_url}/{endpoint}"
        results = []

        print(f"\nMaking request to URL: {url}")
        print(f"With params: {params}")

        try:
            response = self.session.get(
                url,
                headers=self.headers,
                params=params,
                timeout=(10, 60)
            )

            print(f"Response status code: {response.status_code}")
            print(f"Response headers: {dict(response.headers)}")

            # Print first 500 characters of response for debugging
            print(f"Response preview: {response.text[:500]}...")

            response.raise_for_status()

            try:
                data = response.json()

                # Handle different response formats
                if isinstance(data, dict):
                    if "results" in data:
                        results.extend(data["results"])
                    elif "content" in data:
                        results.extend(data["content"])
                    else:
                        results.append(data)
                elif isinstance(data, list):
                    results.extend(data)

                return results

            except json.JSONDecodeError as e:
                print(f"Failed to parse JSON response: {str(e)}")
                print(f"Full response content: {response.text}")
                raise

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {str(e)}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Error response content: {e.response.text}")
            raise Exception(f"Failed to fetch data from {endpoint}: {str(e)}")

def ingest_tempo_data(client_id: str, access_key: str, base_url: str, output_path: str = None):
    """
    Ingest data from Tempo API and save to CSV.

    Args:
        client_id (str): Tempo Client ID
        access_key (str): Tempo Access Key
        base_url (str): Tempo API base URL
        output_path (str): Optional path for saving CSV files
    """
    try:
        # Initialize reader
        reader = TempoReader(client_id, access_key, base_url)

        # Define endpoints to fetch data from
        endpoints = {
            'accounts': 'rest/tempo-accounts/1/account',
            'teams': 'rest/tempo-teams/2/team',
            'worklogs': 'rest/tempo-timesheets/4/worklogs',
            'customers': 'rest/tempo-core/1/customers',
            'plans': 'rest/tempo-planning/1/plans'
        }

        # Store all dataframes
        dataframes = {}

        # Fetch data from each endpoint
        for name, endpoint in endpoints.items():
            print(f"\nFetching data from {name} endpoint...")
            try:
                data = reader.make_api_call(endpoint)
                if data:
                    df = pd.DataFrame(data)
                    dataframes[name] = df

                    # Save to CSV if output_path is provided
                    if output_path:
                        csv_path = f"{output_path}/tempo_{name}.csv"
                        df.to_csv(csv_path, index=False)
                        print(f"Saved {name} data to {csv_path}")

                    print(f"Successfully retrieved {len(df)} records for {name}")
                    # Display first few rows
                    display(df.head())
                else:
                    print(f"No data retrieved for {name}")

            except Exception as e:
                print(f"Error fetching {name} data: {str(e)}")
                continue

        return dataframes

    except Exception as e:
        print(f"Error during data ingestion: {str(e)}")
        raise

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Usage example - Configuration Section
if __name__ == "__main__":
    # Configuration - Replace with your actual values
    CLIENT_ID = "your_tempo_client_id_here"  # Get from Tempo App Management
    ACCESS_KEY = "your_tempo_access_key_here"  # Get from Tempo App Management
    BASE_URL = "https://your-company.atlassian.net/plugins/servlet/ac/io.tempo.jira/tempo-app"  # Replace with your Atlassian domain

    try:
        # Ingest data
        dataframes = ingest_tempo_data(
            client_id=CLIENT_ID,
            access_key=ACCESS_KEY,
            base_url=BASE_URL,
        )

        # Work with the returned dataframes
        for name, df in dataframes.items():
            print(f"\nDataframe for {name}:")
            display(df)

    except Exception as e:
        print(f"Failed to ingest Tempo data: {str(e)}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import pandas as pd
from typing import List, Dict, Any
import json

class TempoReader:
# Example TempoReader class for Tempo Cloud API
# This class demonstrates how to authenticate using Bearer token        """
        Initialize TempoReader with Tempo Cloud API authentication.

        Args:
            client_id (str): The Client ID from Tempo
            access_key (str): The Access Key from Tempo
        """
        self.client_id = client_id
        self.access_key = access_key
        self.base_url = "https://api.tempo.io/core/3"  # Tempo Cloud API endpoint
        self.session = self._create_session()

        # Set up OAuth Bearer token authentication
        self.headers = {
            "Authorization": f"Bearer {self.access_key}",
            "Content-Type": "application/json"
        }

    def _create_session(self) -> requests.Session:
        """Create a session with retry strategy."""
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
        """Make API call to Tempo endpoint."""
        url = f"{self.base_url}/{endpoint}"
        results = []

        print(f"\nMaking request to URL: {url}")
        print(f"With params: {params}")

        try:
            response = self.session.get(
                url,
                headers=self.headers,
                params=params,
                timeout=(10, 60)
            )

            print(f"Response status code: {response.status_code}")

            response.raise_for_status()
            data = response.json()

            # Handle pagination
            if isinstance(data, dict):
                if "results" in data:
                    results.extend(data["results"])
                elif "content" in data:
                    results.extend(data["content"])
                else:
                    results.append(data)
            elif isinstance(data, list):
                results.extend(data)

            return results

        except Exception as e:
            print(f"Error making API call: {str(e)}")
            if hasattr(e, 'response'):
                print(f"Response content: {e.response.text[:500]}")
            raise

def ingest_tempo_data(client_id: str, access_key: str, output_path: str = None):
    """
    Ingest data from Tempo Cloud API.

    Args:
        client_id (str): Tempo Client ID
        access_key (str): Tempo Access Key
        output_path (str): Optional path for saving CSV files
    """
    try:
        reader = TempoReader(client_id, access_key)

        # Define endpoints to fetch data from
        endpoints = {
            'accounts': 'accounts',
            'teams': 'teams',
            'worklogs': 'worklogs',
            'customers': 'customers',
            'plans': 'plans/customer',
            'work-attributes': 'work-attributes'
        }

        dataframes = {}

        # Fetch data from each endpoint
        for name, endpoint in endpoints.items():
            print(f"\nFetching data from {name} endpoint...")
            try:
                # Add date range for worklogs
                params = None
                if name == 'worklogs':
                    from datetime import datetime, timedelta
                    end_date = datetime.now()
                    start_date = end_date - timedelta(days=30)  # Last 30 days
                    params = {
                        'from': start_date.strftime('%Y-%m-%d'),
                        'to': end_date.strftime('%Y-%m-%d')
                    }

                data = reader.make_api_call(endpoint, params)

                if data:
                    df = pd.DataFrame(data)
                    dataframes[name] = df

                    if output_path:
                        csv_path = f"{output_path}/tempo_{name}.csv"
                        df.to_csv(csv_path, index=False)
                        print(f"Saved {name} data to {csv_path}")

                    print(f"Successfully retrieved {len(df)} records for {name}")
                    display(df.head())
                else:
                    print(f"No data retrieved for {name}")

            except Exception as e:
                print(f"Error fetching {name} data: {str(e)}")
                continue

        return dataframes

    except Exception as e:
        print(f"Error during data ingestion: {str(e)}")
        raise

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Usage
if __name__ == "__main__":
    # Configuration
    CLIENT_ID = "your_tempo_client_id_here"  
    ACCESS_KEY = "your_tempo_access_key_here" 

    try:
        dataframes = ingest_tempo_data(
            client_id=CLIENT_ID,
            access_key=ACCESS_KEY,
        )

        # Work with the returned dataframes
        for name, df in dataframes.items():
            print(f"\nDataframe for {name}:")
            display(df)

    except Exception as e:
        print(f"Failed to ingest Tempo data: {str(e)}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

class TempoReader:
    def __init__(self, access_key: str):
        """
# Simplified TempoReader class for Tempo Cloud API
# This is a minimal example showing basic API authentication        """
        self.access_key = access_key
        self.base_url = "https://api.tempo.io/core/3"  # Tempo Cloud API base URL
        self.session = self._create_session()

        # Set up Bearer token authentication
        self.headers = {
            "Authorization": f"Bearer {self.access_key}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def _create_session(self) -> requests.Session:
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
        """Make API call to Tempo endpoint."""
        url = f"{self.base_url}/{endpoint}"
        print(f"Making request to URL: {url}")
        try:
            response = self.session.get(
                url,
                headers=self.headers,
                params=params,
                timeout=(10, 60)
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {str(e)}")
            raise

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

if __name__ == "__main__":
    ACCESS_KEY = "your_tempo_access_key_here"  # Replace with your Tempo Cloud API Access Key

    reader = TempoReader(ACCESS_KEY)
    try:
        accounts = reader.make_api_call("accounts")
        print("Accounts data:", accounts)
    except Exception as e:
        print(f"Failed to fetch accounts: {str(e)}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
