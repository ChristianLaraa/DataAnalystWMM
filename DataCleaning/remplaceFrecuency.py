import pandas as pd


df = pd.read_csv("data.csv")

# Define el diccionario de mapeo
mapeo = {
    'Nunca': 0,
    'Raramente': 1,
    'Ocasionalmente': 2,
    'Frecuentemente': 3
}

# Lista de columnas a convertir (coloca aquí los nombres exactos de las columnas)
columnas_a_convertir = [
    #Frecunencia en tiempo libre y hobbies
    '¿Con qué frecuencia realizas las siguientes actividades en tu tiempo libre? [Hacer ejercicio]',
    '¿Con qué frecuencia realizas las siguientes actividades en tu tiempo libre? [Leer]',
    '¿Con qué frecuencia realizas las siguientes actividades en tu tiempo libre? [Jugar videojuegos]',
    '¿Con qué frecuencia realizas las siguientes actividades en tu tiempo libre? [Ver películas o series]',
    '¿Con qué frecuencia realizas las siguientes actividades en tu tiempo libre? [Asistir a conciertos o festivales]',
    '¿Con qué frecuencia realizas las siguientes actividades en tu tiempo libre? [Salir a bares o centros nocturnos]',
    '¿Con qué frecuencia realizas las siguientes actividades en tu tiempo libre? [Escuchar música]',
    #Frecuencia videojuego, tipos
    '¿Con qué frecuencia juegas los siguientes tipos de videojuegos? [Role Playing Game]',
    '¿Con qué frecuencia juegas los siguientes tipos de videojuegos? [Acción]',
    '¿Con qué frecuencia juegas los siguientes tipos de videojuegos? [Aventura]',
    '¿Con qué frecuencia juegas los siguientes tipos de videojuegos? [Arcade]',
    '¿Con qué frecuencia juegas los siguientes tipos de videojuegos? [Deportivo]',
    '¿Con qué frecuencia juegas los siguientes tipos de videojuegos? [Estrategia]',
    '¿Con qué frecuencia juegas los siguientes tipos de videojuegos? [Simulación]',
    '¿Con qué frecuencia juegas los siguientes tipos de videojuegos? [Juegos de mesa]',
    '¿Con qué frecuencia juegas los siguientes tipos de videojuegos? [Juegos musicales]',
    #Frecuencia escucha de musica tipo, streaming
    '¿Con qué frecuencia escuchas la música en plataformas de las siguientes maneras?   [Listas personalizadas]',
    '¿Con qué frecuencia escuchas la música en plataformas de las siguientes maneras?   [Listas de la plataforma]',
    '¿Con qué frecuencia escuchas la música en plataformas de las siguientes maneras?   [Playlists populares]',
    '¿Con qué frecuencia escuchas la música en plataformas de las siguientes maneras?   [Algoritmo (modo descubrimiento)]',
    #Frecuencia videos musicales
    '¿Con qué frecuencia ves los videos musicales de las canciones que escuchas?',
    #Frecuencia consumo de redes sociales
    '¿Con qué frecuencia ocupas las siguientes redes sociales?  [Instagram]',
    '¿Con qué frecuencia ocupas las siguientes redes sociales?  [TikTok]',
    '¿Con qué frecuencia ocupas las siguientes redes sociales?  [Twitter/X]',
    '¿Con qué frecuencia ocupas las siguientes redes sociales?  [YouTube]',
    '¿Con qué frecuencia ocupas las siguientes redes sociales?  [Facebook]',
    #participacion de fans
    '¿Con qué frecuencia participas en los grupos o comunidades de fans? [Blogs o páginas web creadas por fans]',
    '¿Con qué frecuencia participas en los grupos o comunidades de fans? [Comunidades en Discord]',
    '¿Con qué frecuencia participas en los grupos o comunidades de fans? [Grupos de facebook]',
    '¿Con qué frecuencia participas en los grupos o comunidades de fans? [Canales de telegram]',
    '¿Con qué frecuencia participas en los grupos o comunidades de fans? [Canales de instagram]',
    '¿Con qué frecuencia participas en los grupos o comunidades de fans? [Eventos en vivo o meetups organizadas por fans]',
    '¿Con qué frecuencia participas en los grupos o comunidades de fans? [Comunidades de fanfiction]',
    '¿Con qué frecuencia participas en los grupos o comunidades de fans? [Canales de youtube]',
    '¿Con qué frecuencia participas en los grupos o comunidades de fans? [Canales de twitch]',
    #Frecuencia de consumo y compras
    '¿Con qué frecuencia compras los siguientes productos (relacionados con la industria musical: artistas, bandas, etc.)? [Boletos a conciertos]',
    '¿Con qué frecuencia compras los siguientes productos (relacionados con la industria musical: artistas, bandas, etc.)? [Discos o viniles]',
    '¿Con qué frecuencia compras los siguientes productos (relacionados con la industria musical: artistas, bandas, etc.)? [Playeras]',
    '¿Con qué frecuencia compras los siguientes productos (relacionados con la industria musical: artistas, bandas, etc.)? [Sudaderas]',
    '¿Con qué frecuencia compras los siguientes productos (relacionados con la industria musical: artistas, bandas, etc.)? [Gorras]',
    '¿Con qué frecuencia compras los siguientes productos (relacionados con la industria musical: artistas, bandas, etc.)? [Pulseras, collares o accesorios]',
    '¿Con qué frecuencia compras los siguientes productos (relacionados con la industria musical: artistas, bandas, etc.)? [Cobijas o Toallas]',
    '¿Con qué frecuencia compras los siguientes productos (relacionados con la industria musical: artistas, bandas, etc.)? [Peluches]',
    '¿Con qué frecuencia compras los siguientes productos (relacionados con la industria musical: artistas, bandas, etc.)? [Figuras de colección]',
    '¿Con qué frecuencia compras los siguientes productos (relacionados con la industria musical: artistas, bandas, etc.)? [Tazas, vasos o termos]',
    '¿Con qué frecuencia compras los siguientes productos (relacionados con la industria musical: artistas, bandas, etc.)? [Stickers]',
    '¿Con qué frecuencia compras los siguientes productos (relacionados con la industria musical: artistas, bandas, etc.)? [Posters]',
    '¿Con qué frecuencia compras los siguientes productos (relacionados con la industria musical: artistas, bandas, etc.)? [Bolsas o tote bags]',
    '¿Con qué frecuencia compras los siguientes productos (relacionados con la industria musical: artistas, bandas, etc.)? [Llaveros o pines]',
]

# Aplica el mapeo a cada columna en la lista
for columna in columnas_a_convertir:
    df[columna] = df[columna].map(mapeo)

# Guarda el DataFrame limpio en un nuevo archivo CSV
df.to_csv("data.csv", index=False)

print("Los datos han sido convertidos y guardados en 'data.csv'")
