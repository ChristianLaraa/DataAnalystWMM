import pandas as pd

df = pd.read_csv("data.csv")

mapeo = {
    "Menos de $4,000 MXN": 0,
    "Entre $4,001 y $8,000 MXN": 1,
    "Entre $8,001 y $13,500 MXN": 2,
    "Entre $13,500 -$22,000 MXN": 3,
    "Entre $22,001 y $38,000 MXN": 4,
    "Entre $38,001 y $75,000 MXN": 5,
    "Más de $75,000 MXN": 6
}

change_columns = ['¿Cuál es el ingreso mensual aproximado en tu hogar?']

for col in change_columns:
    df[col] = df[col].map(mapeo)

print(df.head())
df.to_csv("data.csv", index=False)
