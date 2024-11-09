import pandas as pd

df = pd.read_csv("data.csv")

df.fillna({
    '¿Con qué frecuencia juegas los siguientes tipos de videojuegos? [Role Playing Game]': 0,
}, inplace=True)


df.to_csv("data.csv", index=False)
