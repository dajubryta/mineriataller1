import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('angelsdata.csv', low_memory=False)

# Códigos de armas específicas
codigos_armas = ['300', '310', '320', '330']

# Filtrar los incidentes que involucren esos códigos de armas
delitos_con_armas = df[df['Weapon Used Cd'].isin(codigos_armas)]

# Mostrar las primeras 5 filas del dataframe filtrado
print(delitos_con_armas.head())
