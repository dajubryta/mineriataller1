import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('angelsdata.csv', low_memory=False)

# Géneros específicos de la víctima
generos = ['M', 'F']

# Filtrar incidentes donde el sexo de la víctima es masculino o femenino
delitos_por_genero = df[df['Vict Sex'].isin(generos)]

# Mostrar las primeras 5 filas del dataframe filtrado
print(delitos_por_genero.head())
