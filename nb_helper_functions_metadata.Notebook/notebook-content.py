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
# To host common functions created to support metadata aspects of a data pipeline

# CELL ********************

def get_lakehouse_id(lakehouse_name: str) -> str:
    """Extracts the lakehouse id for based on workspace code executed in."""
    return mssparkutils.lakehouse.get(lakehouse_name)['id']
    

def get_lakehouse_abfs_path(lakehouse_name: str) -> str:
    """Extracts the lakehouse abfs path for based on workspace code executed in."""
    return mssparkutils.lakehouse.get(lakehouse_name)['properties']['abfsPath']


def extract_secret(key_name: str) -> str:
    """Extracts a secret from Azure Key Vault."""
    try:
        secret_value = tl.get_secret_with_token(globals()['global_configs']['key_vault_url'], key_name, globals()['global_configs']['access_token'])
        if not secret_value:
            raise ValueError(f"Failed to retrieve secret: {key_name}")

        return secret_value

    except Exception as e:
        raise ValueError(f"Error retrieving secret {key_name}: {e}")


def expand_nested_schema(schema: list) -> list:
    """Expand nested schema."""
    # TODO - needs refactoring
    final_schema = []

    def add_to_final_schema(entry):
        """Add entry to final_schema if not already present."""
        if entry not in final_schema:
            final_schema.append(entry)
    
    for row in schema:
        if row.get('nested'):
            sub_fields = row['nested']['sub_fields']
            for sub_field in sub_fields:
                if row['nested'].get('multi'):
                    add_to_final_schema(
                        {
                            'from': '-'.join([row['from'], sub_field['name']]),
                            'to': row['to'] + ''.join(part.capitalize() for part in sub_field['name'].split('-')),
                            'dataType': sub_field['dataType'],
                            'personal': sub_field['personal'],
                            'sensitive': sub_field['sensitive']
                        }
                    )
                elif row['nested'] and row['nested'].get('gql_string'):
                    add_to_final_schema(
                        {
                            'from': sub_field['name'],
                            'to': sub_field['name'],
                            'dataType': sub_field['dataType'],
                            'personal': row['personal'] if len(sub_fields) == 1 else sub_field['personal'],
                            'sensitive': row['sensitive'] if len(sub_fields) == 1 else sub_field['sensitive']
                        }
                    )
                else:
                    add_to_final_schema(row)
        else:
            add_to_final_schema(row)
    
    return final_schema


def extact_required_fields(schema: list, table: str, layer: str = None) -> set:
  """Function to return the required fields from a given schema."""
  required_fields = set()
  
  for field in schema:
      from_field = field['from']
      
      if isinstance(from_field, dict):
          # Check if the table is in the dictionary
          if table in from_field:
              # Add all fields from the list to the set
              required_fields.update(from_field[table])
      
      elif isinstance(from_field, str):
          if layer:
              # Add the field specified by the layer
              required_fields.add(field[layer])
          else:
              raise ValueError('Layer needs to be set')
  
  return required_fields


def generate_graphql_query(fact_sheet_name: str, schema: list) -> str:
    """Function to create graphql query for a given LeanIX schema."""
    def process_field(field):
        field_name = field['from']
        nested = field.get('nested')
        if nested:
            return f"{field_name} {nested['gql_string']}"
        else:
            return field_name

    query_fields = [process_field(field) for field in schema]
    query_body = "\n".join(query_fields)
    
    query = f"""
    {{
        allFactSheets(factSheetType: {fact_sheet_name}) {{
            edges {{
                node {{
                    ... on {fact_sheet_name} {{
{textwrap.indent(query_body, ' ' * 20)}
                    }}
                }}
            }}
        }}
    }}
    """
    return query


def generate_date_range(start_date, end_date) -> list:
    """Function to generate date range"""
    date_list = []
    current_date = start_date
    while current_date <= end_date:
        date_key = int(current_date.strftime('%Y%m%d'))
        date_list.append({
            "DateKey": date_key,
            "Date": current_date,
            "Day": current_date.day,
            "Month": current_date.month,
            "Year": current_date.year,
            "DayOfWeek": current_date.strftime('%A'),
            "Quarter": (current_date.month - 1) // 3 + 1,
            "Half": 1 if current_date.month <= 6 else 2
        })
        current_date += timedelta(days=1)
    return date_list

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def collect_field_values(field_list):
    """
    Collects all the 'field' values from a list of dictionaries.

    Args:
    field_list (list of dict): List containing field information.

    Returns:
    list: A list of field values extracted from the dictionaries.
    """
    return [item['field'] for item in field_list]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def get_api_token(tenant_id, client_id, client_secret, scope):
    """
    Retrieve an API token for the given scope using the provided client ID, client secret and tenant id credentials.
    """
    payload = {
        'client_id': client_id,
        'scope': scope,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }
    token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

    try:
        response = requests.post(token_url, data=payload)
        response.raise_for_status()
        token = response.json().get("access_token")
        logging.info("Access token successfully retrieved.")
        return token
    except requests.exceptions.HTTPError as err:
        logging.error(f"Error retrieving token: {err}")
        logging.error(f"Response content: {response.text}")
        raise

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
