import pandas as pd

df = pd.read_csv("data.csv")

mapeo = {
    "No": 0,
    "Sí": 1,
}

change_columns = ['¿Has comprado productos por verlo promocionado en redes sociales de artistas?  ',
                  '¿Has asistido a eventos de un artista por verlo promocionado en redes sociales?  ']

for col in change_columns:
    df[col] = df[col].map(mapeo)

print(df.head())
df.to_csv("data.csv", index=False)