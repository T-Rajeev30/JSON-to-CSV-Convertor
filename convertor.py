import pandas as pd

obj = pd.read_json('planitData.json', orient='values')
print(obj)
obj.to_csv('planitData.csv')