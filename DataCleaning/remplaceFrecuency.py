import pandas as pd

# Carga el archivo CSV en un DataFrame
df = pd.read_csv("data.csv")

# Define el diccionario de mapeo
mapeo = {
    'Nunca': 0,
    'Raramente': 1,
    'Ocasionalmente': 2,
    'Frecuentemente': 3
}

# Reemplaza los valores en la columna específica (cambia 'columna_encuesta' por el nombre de tu columna)
df['¿Con qué frecuencia participas en los grupos o comunidades de fans? [Blogs o páginas web creadas por fans]'] = df['¿Con qué frecuencia participas en los grupos o comunidades de fans? [Blogs o páginas web creadas por fans]'].map(mapeo)

# Guarda el DataFrame limpio en un nuevo archivo CSV
df.to_csv("datav1.csv", index=False)

print("Los datos han sido convertidos y guardados en 'datav1.csv'")
