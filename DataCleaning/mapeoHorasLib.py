import pandas as pd

df = pd.read_csv("data.csv")

mapeo = {
    "1-3 horas": 0,
    "4-6 horas": 1,
    "6-8 horas": 2,
    "Más de 8 horas": 3,
}

change_columns = ['  ¿Cuánto tiempo libre tienes al día?  ']

for col in change_columns:
    df[col] = df[col].map(mapeo)

print(df.head())
df.to_csv("data.csv", index=False)
