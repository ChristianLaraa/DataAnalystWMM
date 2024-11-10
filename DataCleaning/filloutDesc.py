import pandas as pd

df = pd.read_csv("data.csv")

df.fillna({
    '¿Por qué?': 'Sin consumo',
    '¿Cuáles son los videogames que juegas con mayor frecuencia? (máximo 3)': 'Sin consumo',
    '¿En qué medio juegas videojuegos?  (Seleccionar todas las que apliquen)': 'Sin consumo',
    '¿Qué tipo de música escuchas mientras juegas videojuegos?': 'No aplica',
    '¿De qué eres fanático?': 'Sin fanatismo',
    '¿Por qué eres fan de eso?': 'No aplica',
    '¿De qué artistas o bandas eres fanático? (mencionar 3)': 'Sin fanatismo',
    '¿Por qué eres fan de tus artistas o bandas favoritas? (seleccionar máximo 3)': 'No aplica',
    '¿Por qué otros motivos eres fanático de esos artistas o bandas?': 'Sin motivos',
    '¿Cuáles son los principales factores que te hacen seguir a un artista en redes sociales?  (seleccionar máximo 3 opciones)': 'No aplica',
    '¿Cuáles son los principales factores que te hacen dejar de seguir a un artista en redes sociales?  ': 'Sin motivos',
    '¿Qué dinámica te gustaría que realizara tu artista o banda favorita?': 'Sin dinamica',
    '¿Qué otro tipo de productos compras de tus artistas o bandas favoritas?': 'Ninguno',
}, inplace=True)


df.to_csv("data.csv", index=False)