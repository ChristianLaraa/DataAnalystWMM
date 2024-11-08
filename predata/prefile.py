import pandas as pd

# Lee el archivo Excel
df = pd.read_excel('data.xlsx', sheet_name=None)  # Si el archivo tiene múltiples hojas

# Convierte el dataframe a JSON
df.to_json('data.json', orient='records', lines=True)
