import pandas as pd

df = pd.read_csv("data.csv")

mapeo = {
    "Ninguno": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5 o más": 5
}

change_columns = ['  ¿Cuántos automóviles hay en tu hogar?  ']

for col in change_columns:
    df[col] = df[col].map(mapeo).astype(int)

print(df.head())
df.to_csv("data.csv", index=False)
