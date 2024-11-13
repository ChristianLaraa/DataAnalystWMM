import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

# 1. Cargar el archivo de datos
file_path = 'data.csv'
data = pd.read_csv(file_path)

# 2. Seleccionar columnas relevantes para clustering
selected_columns = [
    'edad',
    'acceso_internet',
    'frecuencia_compra_cobijas_artistas',
    'frecuencia_compra_peluches_artistas',
    'frecuencia_compra_figuras_coleccion_artistas',
    'frecuencia_compra_tazas_vasos_artistas',
    'frecuencia_compra_stickers_artistas',
    'frecuencia_compra_posters_artistas',
    'frecuencia_compra_bolsas_totes_artistas',
    'frecuencia_compra_llaveros_pines_artistas'
]
data_cluster = data[selected_columns].dropna()

# 3. Escalar los datos
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_cluster)

# 4. Método del codo para determinar el número óptimo de clusters
sse = []
k_range = range(1, 11)
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data_scaled)
    sse.append(kmeans.inertia_)

plt.figure(figsize=(10, 6))
plt.plot(k_range, sse, marker='o')
plt.xlabel('Número de clusters (k)')
plt.ylabel('Inercia (SSE)')
plt.title('Método del Codo para Selección de k')
plt.show()

# 5. Aplicar K-Means con el número óptimo de clusters (k=3)
kmeans = KMeans(n_clusters=3, random_state=42)
data_cluster['cluster'] = kmeans.fit_predict(data_scaled)

# 6. Reducción de dimensiones con PCA para visualización 2D
pca = PCA(n_components=2)
data_pca = pca.fit_transform(data_scaled)
data_cluster['pca1'] = data_pca[:, 0]
data_cluster['pca2'] = data_pca[:, 1]

# 7. Graficar los clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data_cluster, x='pca1', y='pca2', hue='cluster', palette='viridis', s=100, alpha=0.7)
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.title('Visualización de Clusters de Usuarios con K-Means (k=3)')
plt.legend(title='Cluster')
plt.show()
