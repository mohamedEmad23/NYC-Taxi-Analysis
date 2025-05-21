from astrapy import DataAPIClient
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("ASTRA_DB_TOKEN")
if not token:
    raise ValueError("ASTRA_DB_TOKEN is not set or could not be loaded")
print(f"Loaded Token: {token[:10]}....")


# Initialize the client
client = DataAPIClient(token)
db = client.get_database_by_api_endpoint(
  "https://c780d9bd-4359-48d3-9a81-5294850cbfc2-us-east-2.apps.astra.datastax.com"
)

print(f"Connected to Astra DB: {db.name()}")
print(f"Connected to Astra DB: {db.list_collection_names()}")
