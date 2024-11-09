import pandas as pd

df = pd.read_csv("data.csv")

df.fillna({
    '¿Con qué frecuencia juegas los siguientes tipos de videojuegos? [Role Playing Game]': 0,
    '¿Con qué frecuencia juegas los siguientes tipos de videojuegos? [Acción]	': 0,
    '¿Con qué frecuencia juegas los siguientes tipos de videojuegos? [Aventura]	': 0,
    '¿Con qué frecuencia juegas los siguientes tipos de videojuegos? [Arcade]': 0,
    '¿Con qué frecuencia juegas los siguientes tipos de videojuegos? [Deportivo]': 0,
    '¿Con qué frecuencia juegas los siguientes tipos de videojuegos? [Estrategia]': 0,
    '¿Con qué frecuencia juegas los siguientes tipos de videojuegos? [Simulación]	': 0,
    '¿Con qué frecuencia juegas los siguientes tipos de videojuegos? [Juegos de mesa]': 0,
    '¿Con qué frecuencia juegas los siguientes tipos de videojuegos? [Juegos musicales]	': 0,


}, inplace=True)


df.to_csv("data.csv", index=False)
