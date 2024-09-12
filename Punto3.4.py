import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('angelsdata.csv', low_memory=False)

# Convertir la columna de fecha a tipo datetime
df['DATE OCC'] = pd.to_datetime(df['DATE OCC'])

# Contar el número de incidentes por año
incidentes_por_anio = df.groupby(df['DATE OCC'].dt.year).size()

# Mostrar los resultados
print(incidentes_por_anio)
