import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('angelsdata.csv', low_memory=False)

# Contar el número de incidentes por código de arma utilizada
incidentes_por_arma = df.groupby('Weapon Used Cd').size()

# Mostrar los resultados
print(incidentes_por_arma)
