import pandas as pd

df = pd.read_csv("data.csv")

mapeo = {
    "Bajo - bajo": 0,
    "Bajo": 1,
    "Medio-bajo": 2,
    "Medio": 3,
    "Medio-alto": 4,
    "Alto - Medio": 5,
    "Alto": 6
}

change_columns = ['¿Cuál consideras que es tu nivel socioeconómico?']

for col in change_columns:
    df[col] = df[col].map(mapeo)

print(df.head())
df.to_csv("data.csv", index=False)
