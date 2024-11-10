import pandas as pd

df = pd.read_csv("data.csv")

df.fillna({
'¿Escuchas música mientras juegas videojuegos?': 'No'
}, inplace=True)


df.to_csv("data.csv", index=False)