import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('angelsdata.csv', low_memory=False)

# Filtrar las edades de las víctimas entre 18 y 30 años
delitos_por_edad = df[(df['Vict Age'] >= 18) & (df['Vict Age'] <= 30)]

# Mostrar las primeras 5 filas del dataframe filtrado
print(delitos_por_edad.head())
