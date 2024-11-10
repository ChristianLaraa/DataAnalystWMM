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

change_columns = ['  ¿Cuántas computadoras o laptops hay en tu hogar?  ',
                  '  ¿Cuántas teléfonos inteligentes hay en tu hogar?  ']

for col in change_columns:
    df[col] = df[col].map(mapeo).astype(int)

print(df.head())
df.to_csv("data.csv", index=False)
