import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('angelsdata.csv', low_memory=False)

# Contar el número de incidentes por tipo de delito (Crm Cd)
incidentes_por_tipo_delito = df.groupby('Crm Cd').size()

# Mostrar los resultados
print(incidentes_por_tipo_delito)
