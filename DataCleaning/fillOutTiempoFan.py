import pandas as pd

df = pd.read_csv("data.csv")

df.fillna({
    '¿Has comprado productos por verlo promocionado en redes sociales de artistas?  ': 0,
    '¿Has asistido a eventos de un artista por verlo promocionado en redes sociales?  ': 0
}, inplace=True)


df.to_csv("data.csv", index=False)