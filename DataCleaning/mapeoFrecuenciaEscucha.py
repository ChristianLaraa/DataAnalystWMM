import pandas as pd

df = pd.read_csv("data.csv")

mapeo = {
    "Menos de 1 hora al día": 0,
    "1 a 2 horas diario": 1,
    "3 a 4 horas diario": 2,
    "5 o más horas diarias": 3
}

change_columns = ['¿Con qué frecuencia escuchas música?  ']

for col in change_columns:
    df[col] = df[col].map(mapeo)

print(df.head())
df.to_csv("data.csv", index=False)
