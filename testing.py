import pandas as pd
import json

# Define the search list of keys we want to extract
search_list = ['address', 'area_id', 'area_name', 'link', 'agent_name', 'agent_company']

# Initialize a list to store the extracted data
data = []

# Load the JSON data from the file
json_file_path = 'planitData.json'

with open(json_file_path, 'r') as file:
    json_data = json.load(file)
    
    # Loop through each record in the 'records' list
    for record in json_data['records']:
        # Extract the relevant fields based on the search_list
        extracted_data = {key: record.get(key) for key in search_list}
        data.append(extracted_data)

# Convert the list of extracted data to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('output.csv', index=False)

print("Data has been successfully converted to CSV format.")
