import pandas as pd

df = pd.read_csv("data.csv")

mapeo = {
    "0": 0,
    "Nada importante": 1,
    "Poco importante": 2,
    "Importante": 3,
    "Muy importante": 4,
}

change_columns = ['¿Qué tan importante es para ti es que tus artistas o bandas favoritos tengan presencia en redes sociales? ']

for col in change_columns:
    df[col] = df[col].map(mapeo)

print(df.head())
df.to_csv("data.csv", index=False)