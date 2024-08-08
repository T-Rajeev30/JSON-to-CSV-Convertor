import requests
import json
# JavaScript object notation


api_url = "https://www.planit.org.uk/api/applics/json?auth=Hertfordshire&start_date=2024-07-01&end_date=2024-08-01&"

response = requests.get(api_url)

data = response.json()
json_path = 'planitData.json'
with open(json_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"JSON data saved to {json_path}")
