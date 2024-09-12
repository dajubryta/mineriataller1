import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('angelsdata.csv', low_memory=False)

df['DATE OCC'] = pd.to_datetime(df['DATE OCC'])

# Filtrar incidentes ocurridos entre 2019 y 2021
delitos_por_anio = df[(df['DATE OCC'].dt.year >= 2019) & (df['DATE OCC'].dt.year <= 2021)]

# Mostrar las primeras 5 filas del dataframe filtrado
print(delitos_por_anio.head())
