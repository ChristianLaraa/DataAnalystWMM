import pandas as pd

# Lee el archivo Excel. Cambia 'tus_datos.xlsx' por el nombre de tu archivo
df = pd.read_excel('db.xlsx')

# Convierte el DataFrame a JSON
data_json = df.to_json(orient='records', indent=4, force_ascii=False)

# Guarda el JSON en un archivo
with open('data.json', 'w', encoding='utf-8') as json_file:
    json_file.write(data_json)

print("Conversión completada. Los datos se han guardado en 'data.json'")
