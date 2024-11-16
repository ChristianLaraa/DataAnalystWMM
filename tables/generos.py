import pandas as pd
from collections import Counter

# Cargar el DataFrame desde el archivo CSV
df = pd.read_csv('data.csv')

# Combina todas las palabras de la columna de géneros musicales en una sola lista
all_genres = ' '.join(df['razon_fan_artista']).split()

# Cuenta la frecuencia de cada género
genre_counts = Counter(all_genres)

# Convierte el resultado a un DataFrame
genre_df = pd.DataFrame(genre_counts.items(), columns=['act', 'Frecuencia'])

# Ordena el DataFrame por frecuencia en orden descendente
genre_df = genre_df.sort_values(by='Frecuencia', ascending=False).reset_index(drop=True)

# Guardar el DataFrame en un archivo CSV
genre_df.to_csv('razonBanda.csv', index=False)

print(genre_df)
