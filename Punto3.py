import pandas as pd

df = pd.read_csv('angelsdata.csv', low_memory=False)

# Contar el número de incidentes por área
incidentes_por_area = df.groupby('AREA').size()

# Mostrar los resultados
print(incidentes_por_area)



