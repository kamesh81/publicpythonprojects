import requests
import airtable

at = airtable.Airtable('BASE_ID', 'API_KEY')
at.get('TABLE_NAME')

# Set the base ID and API key for your Airtable
base_id = ""
api_key = ""

# Set the table name and field you want to query
table_name = "MyFirstTable"
field_name = "Name"

# Set the endpoint and headers for the API request
endpoint = "https://api.airtable.com/v0/{base_id}/{table_name}?api_key={api_key}"
headers = {"Content-Type": "application/json"}

# Set the search criteria for the query
# query = {
#    "filterByFormula": f"{field_name} = 'kamesh'",
#}

at.get(table_name, record_id=None, limit=0, offset=None,
       filter_by_formula=None, view=None, max_records=0, fields=[])

# Make the API request to Airtable
#response = requests.get(endpoint, headers=headers, params=query)

# Print the response to check the results
#print(response.json())
