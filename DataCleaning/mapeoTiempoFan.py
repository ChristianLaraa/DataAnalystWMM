import pandas as pd

df = pd.read_csv("data.csv")

mapeo = {
    "0": 0,
    "Menos de un año": 1,
    "1-2 años": 2,
    "3-4 años": 3,
    "5-6 años": 4,
    "Más de 6 años": 5
}

change_columns = ['¿Cuánto tiempo has sido fanático de esos artistas o bandas?']

for col in change_columns:
    df[col] = df[col].map(mapeo)

print(df.head())
df.to_csv("data.csv", index=False)