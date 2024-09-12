import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('angelsdata.csv', low_memory=False)

# Áreas geográficas específicas
areas = ['1', '2', '3', '4', '5']

# Filtrar incidentes que ocurrieron en esas áreas
delitos_por_area = df[df['AREA'].isin(areas)]

# Mostrar las primeras 5 filas del dataframe filtrado
print(delitos_por_area.head())
