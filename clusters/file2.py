import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Cargar el archivo de datos
file_path = 'data.csv'
data = pd.read_csv(file_path)

# 2. Seleccionar columnas relevantes para clustering
selected_columns = [
    'edad',
    'genero',
    'ingreso_mensual_hogar',
    'nivel_socioeconomico',
    'acceso_internet',
    'tiempo_libre_dia',
    'frecuencia_ejercicio',
    'frecuencia_leer',
    'frecuencia_videojuegos',
    'frecuencia_peliculas',
    'frecuencia_conciertos',
    'frecuencia_bares',
    'frecuencia_escuchar_musica',
    'consumo_videojuegos',
    'consumo_simultaneo_musica_videojuego',
    'frecuencia_consumo_musica',
    'importancia_musica_diaria',
    'frecuencia_consumo_musica_listas_personalizadas',
    'frecuencia_consumo_musica_listas_plataformas',
    'frecuencia_consumo_musica_playlist_populares',
    'frecuencia_consumo_musica_algoritmo_descubrimiento',
    'frecuencia_consumo_videos_musicales',
    'frecuencia_consumo_instagram',
    'frecuencia_consumo_tiktok',
    'frecuencia_consumo_twitter',
    'frecuencia_consumo_youtube',
    'frecuencia_consumo_facebook',
    'importancia_seguimiento_tendencias_musicales',
    'es_fan',
    'tiempo_fanatico',
    'tiempo_fan_artista',
    'importancia_artista_redes',
    'compra_productos_promocion_redes',
    'asistencia_eventos_artista_promocion',
    'frecuencia_compra_boletos_conciertos',
    'frecuencia_consumo_musica'
]
data_cluster = data[selected_columns].dropna()

# 3. Escalar los datos
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_cluster)

# 4. Método del codo para determinar el número óptimo de clusters
sse = []
silhouette_scores = []
k_range = range(2, 11)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data_scaled)
    sse.append(kmeans.inertia_)
    silhouette_avg = silhouette_score(data_scaled, kmeans.labels_)
    silhouette_scores.append(silhouette_avg)

plt.figure(figsize=(14, 6))

# Gráfica del método del codo
plt.subplot(1, 2, 1)
plt.plot(k_range, sse, marker='o')
plt.xlabel('Número de clusters (k)')
plt.ylabel('Inercia (SSE)')
plt.title('Método del Codo para Selección de k')

# Gráfica del índice de silueta
plt.subplot(1, 2, 2)
plt.plot(k_range, silhouette_scores, marker='o', color='orange')
plt.xlabel('Número de clusters (k)')
plt.ylabel('Índice de Silueta')
plt.title('Índice de Silueta para Selección de k')

plt.tight_layout()
plt.show()

# 5. Aplicar K-Means con el número óptimo de clusters (por ejemplo, k=3)
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
data_cluster['cluster'] = kmeans.fit_predict(data_scaled)

# 6. Reducción de dimensiones con PCA para visualización 2D
pca = PCA(n_components=2)
data_pca = pca.fit_transform(data_scaled)
data_cluster['pca1'] = data_pca[:, 0]
data_cluster['pca2'] = data_pca[:, 1]

# 7. Paleta personalizada con amarillo incluido
custom_palette = ['#1f77b4', '#ff7f0e', '#ffcc00']  # Azul, Naranja, Amarillo

# Graficar los clusters en 2D
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=data_cluster,
    x='pca1',
    y='pca2',
    hue='cluster',
    palette=custom_palette,
    s=100,
    alpha=0.7
)
plt.xlabel('Preferencias de Entretenimiento (Componente 1)')
plt.ylabel('Interacciones Digitales (Componente 2)')
plt.title('Clusters de Usuarios')
plt.legend(
    title='Perfil del Cluster',
    labels=[
        "Fanáticos Digitales",
        "Entusiastas de Entretenimiento Activo",
        "Consumidores Tradicionales de Música"
    ]
)
plt.show()


