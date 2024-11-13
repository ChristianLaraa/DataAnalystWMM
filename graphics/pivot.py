# Importamos las bibliotecas necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Suponiendo que tu dataframe se llama `df`
df = pd.read_csv('data.csv')
# 1. Analizar el consumo de videojuegos por edad y género
pivot_videojuegos = df.pivot_table(values='consumo_videojuegos', index='edad', columns='genero', aggfunc='mean')
pivot_videojuegos.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Consumo promedio de videojuegos por edad y género')
plt.xlabel('Edad')
plt.ylabel('Consumo de Videojuegos')
plt.show()

# 2. Analizar el consumo de música por frecuencia y lugar de descubrimiento
pivot_musica = df.pivot_table(values='frecuencia_consumo_musica', index='donde_consumo_musica', columns='genero', aggfunc='mean')
pivot_musica.plot(kind='bar', stacked=True, colormap='viridis', figsize=(10, 6))
plt.title('Frecuencia de consumo de música por lugar y género')
plt.xlabel('Lugar de Consumo')
plt.ylabel('Frecuencia de Consumo')
plt.show()


# 4. Frecuencia de compra de productos de artistas por tipo de producto y frecuencia
pivot_productos = df.pivot_table(
    values=['frecuencia_compra_boletos_conciertos', 'frecuencia_compra_playeras_artistas', 'frecuencia_compra_discos_viniles'],
    index='nivel_socioeconomico',
    aggfunc='mean'
)
pivot_productos.plot(kind='bar', figsize=(10, 6))
plt.title('Frecuencia de compra de productos de artistas según nivel socioeconómico')
plt.xlabel('Nivel Socioeconómico')
plt.ylabel('Frecuencia de compra')
plt.legend(title="Productos")
plt.show()

# 5. Comparativa de participación en comunidades de fanáticos por plataforma
pivot_comunidades = df.pivot_table(
    values=['frecuencia_participacion_comunidad_instagram', 'frecuencia_participacion_youtube', 'frecuencia_participacion_discord'],
    index='edad',
    aggfunc='mean'
)
pivot_comunidades.plot(kind='line', marker='o', figsize=(10, 6))
plt.title('Participación en comunidades de fanáticos por edad')
plt.xlabel('Edad')
plt.ylabel('Frecuencia de participación')
plt.legend(title="Plataformas")
plt.show()
