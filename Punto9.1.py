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

    # Ejemplo 2: Frecuencia de delitos por área geográfica (AREA)
    delitos_por_area = df['AREA'].value_counts()
    print("\nDelitos por área geográfica:")
    print(delitos_por_area.head(10))

    # Ejemplo 3: Frecuencia de delitos por día de la semana (Day of Week)
    delitos_por_dia = df['Day of Week'].value_counts()
    print("\nDelitos por día de la semana:")
    print(delitos_por_dia)

    # Ejemplo 4: Frecuencia de delitos por hora del día (Time Occ)
    delitos_por_hora = df['Time Occ'].value_counts()
    print("\nDelitos por hora del día:")
    print(delitos_por_hora.head(10))

    # Ejemplo 5: Frecuencia de delitos por código de delito (Crm Cd)
    delitos_comunes = df['crm_cd'].value_counts()
    print("\nDelitos más comunes por código:")
    print(delitos_comunes.head(10))

    # Ejemplo 6: Frecuencia de delitos por tipo de arma utilizada (Weapon Used Cd)
    armas_utilizadas = df['Weapon Used Cd'].value_counts()
    print("\nFrecuencia de delitos por tipo de arma utilizada:")
    print(armas_utilizadas)
else:
    print("La columna 'date_occ' no existe en el DataFrame.")

