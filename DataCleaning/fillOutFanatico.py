import pandas as pd

df = pd.read_csv("data.csv")

df.fillna({
    '¿Cuánto tiempo has sido fanático de eso?': 0,
}, inplace=True)


df.to_csv("data.csv", index=False)