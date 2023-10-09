import pandas as pd
import matplotlib.pyplot as plt


# convierto csv a dataframe de pandas
df = pd.read_csv("tabla.csv")

df.sort_values(by='Pts', inplace=True, ascending=False)

equipos = df["Equipo"]
puntos = df["Pts"]
plt.bar(equipos, puntos)
plt.xticks(rotation=90)
plt.show()
