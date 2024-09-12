import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('angelsdata.csv', low_memory=False)

# Verificar los nombres de las columnas
print(df.columns)

# Asegurarte de que las columnas 'vict_age' y 'AREA' existen
if 'vict_age' in df.columns and 'AREA' in df.columns:
    # Convertir Vict Age a numérico, ignorando valores que no se pueden convertir
    df['vict_age'] = pd.to_numeric(df['vict_age'], errors='coerce')

    # Eliminar valores nulos en 'vict_age' y 'AREA'
    df = df.dropna(subset=['vict_age', 'AREA'])

    # Filtrar las víctimas que se encuentran en un área específica, por ejemplo, área '1'
    area_1_victims = df[df['AREA'] == 1]

    # Visualizar la distribución de las edades de las víctimas en el área 1 con un histograma
    area_1_victims['vict_age'].plot(kind='hist', bins=20, figsize=(10, 6))
    plt.title('Distribución de edades de las víctimas en el Área 1')
    plt.xlabel('Edad')
    plt.ylabel('Frecuencia')
    plt.show()
else:
    print("Las columnas 'vict_age' o 'AREA' no existen en el DataFrame.")
