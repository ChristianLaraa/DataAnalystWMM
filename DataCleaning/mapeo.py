import pandas as pd


df = pd.read_csv("data.csv")

mapeo = {
    "Masculino": 0,
    "Femenino": 1
}

change_columns = ['¿Cuál es tu género?']

for col in change_columns:
    df[col] = df[col].map(mapeo)

print(df.head())

df.to_csv("data.csv", index=False)
