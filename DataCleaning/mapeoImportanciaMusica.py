import pandas as pd

df = pd.read_csv("data.csv")

mapeo = {
    "No es importante": 0,
    "Poco importante": 1,
    "Importante": 2,
    "Muy importante": 3
}

change_columns = ['¿Qué tan importante es la música en tu vida diaria?  ']

for col in change_columns:
    df[col] = df[col].map(mapeo)

print(df.head())
df.to_csv("data.csv", index=False)
