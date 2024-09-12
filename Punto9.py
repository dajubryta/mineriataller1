import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('angelsdata.csv', low_memory=False)

# Verificar los nombres de las columnas
print(df.columns)

# Asegurarse de que la columna 'date_occ' existe
if 'date_occ' in df.columns:
    # Convertir la columna de fecha a formato datetime
    df['date_occ'] = pd.to_datetime(df['date_occ'], format='%m/%d/%Y')

    # Filtrar incidentes ocurridos entre el 01/01/2023 y el 31/03/2023
    rango_fechas = (df['date_occ'] >= '2023-01-01') & (df['date_occ'] <= '2023-03-31')
    incidentes_en_rango = df[rango_fechas]

    # Ejemplo 1: Frecuencia de delitos por tipo de incidente (Crm Cd Desc)
    delitos_comunes_desc = df['Crm Cd Desc'].value_counts()
    print("Delitos más comunes por descripción:")
    print(delitos_comunes_desc.head(10))

      
else:
    print("La columna 'date_occ' no existe en el DataFrame.")
