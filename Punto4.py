import pandas as pd

df = pd.read_csv('angelsdata.csv', low_memory=False)

# Contar los incidentes según el género de la víctima
delitos_por_genero = df['Vict Sex'].value_counts()


print(delitos_por_genero)

