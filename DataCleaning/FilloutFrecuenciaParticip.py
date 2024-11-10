import pandas as pd

df = pd.read_csv("data.csv")

df.fillna({
    '¿Con qué frecuencia participas en los grupos o comunidades de fans? [Blogs o páginas web creadas por fans]': 0,
    '¿Con qué frecuencia participas en los grupos o comunidades de fans? [Comunidades en Discord]': 0,
    '¿Con qué frecuencia participas en los grupos o comunidades de fans? [Grupos de facebook]': 0,
    '¿Con qué frecuencia participas en los grupos o comunidades de fans? [Canales de telegram]': 0,
    '¿Con qué frecuencia participas en los grupos o comunidades de fans? [Canales de instagram]': 0,
    '¿Con qué frecuencia participas en los grupos o comunidades de fans? [Eventos en vivo o meetups organizadas por fans]': 0,
    '¿Con qué frecuencia participas en los grupos o comunidades de fans? [Comunidades de fanfiction]': 0,
    '¿Con qué frecuencia participas en los grupos o comunidades de fans? [Canales de youtube]': 0,
    '¿Con qué frecuencia participas en los grupos o comunidades de fans? [Canales de twitch]': 0,
}, inplace=True)


df.to_csv("data.csv", index=False)