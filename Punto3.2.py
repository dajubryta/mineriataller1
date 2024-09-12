import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('angelsdata.csv', low_memory=False)

# Contar el número de incidentes por género de la víctima
incidentes_por_genero = df.groupby('Vict Sex').size()

# Mostrar los resultados
print(incidentes_por_genero)
