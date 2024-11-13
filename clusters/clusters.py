import pandas as pd

# Cargar el archivo CSV proporcionado por el usuario
file_path = 'data.csv'
data = pd.read_csv(file_path)

# Ver las primeras filas y obtener información básica sobre el archivo para entender su estructura
data.head(), data.info()
