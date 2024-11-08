import pandas as pd

# Carga el archivo CSV en un DataFrame
df = pd.read_csv("data.csv")

# Muestra las primeras filas
print(df.head())

# Verifica el tipo de datos en cada columna
print(df.info())

# Resumen estadístico de los datos numéricos
print(df.describe())
