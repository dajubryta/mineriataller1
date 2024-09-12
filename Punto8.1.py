import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('angelsdata.csv', low_memory=False)

# Verificar los nombres de las columnas
print(df.columns)

#1 Contar los incidentes según el tipo de delito
tipos_de_delitos = df['Crm Cd Desc'].value_counts()

# Mostrar los resultados
print(tipos_de_delitos)

#2 Contar los incidentes según el área geográfica
incidentes_por_area = df['AREA'].value_counts()

# Mostrar los resultados
print(incidentes_por_area)

#3 Contar los incidentes según el día de la semana
incidentes_por_dia = df['Day of Week'].value_counts()

# Mostrar los resultados
print(incidentes_por_dia)

#4 Contar los incidentes según la hora del día
incidentes_por_hora = df['Time Occ'].value_counts()

# Mostrar los resultados
print(incidentes_por_hora)

