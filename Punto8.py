import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('angelsdata.csv', low_memory=False)

# Verificar los nombres de las columnas
print(df.columns)

# Contar los incidentes según el código de arma utilizada
armas_utilizadas = df['Weapon Used Cd'].value_counts()

# Mostrar los resultados
print(armas_utilizadas)
