import json
import requests
import pandas as pd

# Read the machine data from the metrics.json file
with open('metrics.json', 'r') as f:
    machine_data = json.load(f)
# Convert the json data into a pandas DataFrame
df_machine = pd.DataFrame(machine_data)
# Remove duplicate rows based on the "id", "val", and "time" columns
df_machine = df_machine.drop_duplicates(subset=['id', 'val', 'time'])

# Convert the DataFrame back into a json object
machine_update_data = df_machine.to_dict('records')

# Send the filtered machine data to the /ingestion endpoint
response = requests.post('http://localhost:5000/ingestion', json=machine_update_data)
print(response.status_code)

# Read the production data from the workorder.json file
with open('workorder.json', 'r') as f:
    production_data = json.load(f)

# Convert the json data into a pandas DataFrame
df_prod = pd.DataFrame(production_data)
# Remove duplicate rows based on the "product", and "time" columns
df_prod = df_prod.drop_duplicates(subset=['product','time'])
# Convert the DataFrame back into a json object
production_update_data = df_prod.to_dict('records')

# Send the production data to the /ingestion endpoint
response = requests.post('http://localhost:5000/ingestion', json=production_update_data)
print(response.status_code)
