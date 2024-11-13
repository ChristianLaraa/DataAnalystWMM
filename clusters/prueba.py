import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el DataFrame desde un archivo CSV
df = pd.read_csv('data.csv')

# Asegúrate de que las columnas que quieres usar para el clustering están en el DataFrame
features = ['edad', 'nivel_socioeconomico']

# Verificar si hay valores nulos
print(df[features].info())
print(df[features].head())

# Eliminar filas con valores nulos
df = df.dropna(subset=features)

# Definir el número de clusters
num_clusters = 3

# Crear el modelo KMeans
kmeans = KMeans(n_clusters=num_clusters, random_state=42)

# Ajustar el modelo a los datos
kmeans.fit(df[features])

# Añadir los clusters al DataFrame
df['cluster'] = kmeans.labels_

# Visualizar los clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='edad', y='nivel_socioeconomico', hue='cluster', palette='viridis')
plt.title('Clusters de Audiencias')
plt.xlabel('Edad')
plt.ylabel('Ingresos')
plt.show()
