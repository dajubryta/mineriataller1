import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Cargar el archivo CSV
df = pd.read_csv('angelsdata.csv', low_memory=False)

# Verificar los nombres de las columnas
print(df.columns)

# Convertir las columnas de fechas a formato datetime
df['date_occ'] = pd.to_datetime(df['date_occ'], format='%m/%d/%Y')

# Filtrar incidentes ocurridos entre el 01/01/2023 y el 31/03/2023
rango_fechas = (df['date_occ'] >= '2023-01-01') & (df['date_occ'] <= '2023-03-31')
incidentes_en_rango = df[rango_fechas]

# Mostrar los resultados
print(incidentes_en_rango.head())
