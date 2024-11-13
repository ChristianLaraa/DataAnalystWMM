import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos desde el CSV
df = pd.read_csv('data.csv')
columna = df['consumo_videojuegos']  # Selecciona la columna específica que deseas graficar

# Colores personalizados para el gráfico
colors = ['#ff7330','#66b3ff','#99ff49','#ffcc99','#c2c2f0','#ffb3e6','#c4e17f','#76d7c4','#f7b7a3','#d4a5a5']

plt.figure(figsize=(8, 8))
columna.value_counts().plot(kind='pie', autopct='%1.1f%%', colors=colors, startangle=140, pctdistance=0.85, wedgeprops={'edgecolor': 'black'})

# Dibujar un círculo en el centro para hacer un gráfico de dona

fig = plt.gcf()


# Estilo del título y etiquetas
plt.title('Consumo de Videojuegos', fontsize=15, fontweight='bold')
plt.ylabel('')
plt.axis('equal')  # Asegura que el gráfico sea un círculo

# Mostrar la gráfica
plt.show()

