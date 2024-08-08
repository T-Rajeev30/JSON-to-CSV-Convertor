import pandas as pd
import json
#Comma-separated values 
required_list_to_search = ['address', 'area_id', 'area_name', 'link', 'agent_name', 'agent_company']

data = []

json_file = 'planitData.json'

with open(json_file, 'r') as file:
    json_data = json.load(file)
    
for record in json_data['records']:
        obtained_data = {key: record.get(key) for key in required_list_to_search}
        data.append(obtained_data)

df = pd.DataFrame(data)

df.to_csv('output.csv', index=False)

print("the JSon is converted into CSV file")
