import pandas as pd


df = pd.read_csv("data.csv")

mapeo = {
    "No": 0,
    "Sí": 1
}

change_columns = ['  ¿Tienes acceso a Internet en tu hogar?  ']

for col in change_columns:
    df[col] = df[col].map(mapeo)

print(df.head())
df.to_csv("data.csv", index=False)
