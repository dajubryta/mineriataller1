import pandas as pd

df = pd.read_csv('angelsdata.csv', low_memory=False)

codigos_graves = ['110', '120', '130', '140', '150', '160']


delitos_graves = df[df['Crm Cd 1'].isin(codigos_graves)]

# Mostrar las primeras 5 filas del dataframe filtrado

print(delitos_graves.head())
