import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('angelsdata.csv', low_memory=False)

# Verificar los nombres de las columnas
print(df.columns)

# Asegurarte de que la columna 'vict_age' existe
if 'vict_age' in df.columns:
    # Convertir Vict Age a numérico, ignorando valores que no se pueden convertir
    df['vict_age'] = pd.to_numeric(df['vict_age'], errors='coerce')

    # Filtrar las víctimas de género femenino
    females = df[df['Vict Sex'] == 'F']

    # Visualizar la distribución de las edades de las víctimas femeninas con un histograma
    females['vict_age'].plot(kind='hist', bins=20, figsize=(10, 6))
    plt.title('Distribución de edades de víctimas femeninas')
    plt.xlabel('Edad')
    plt.ylabel('Frecuencia')
    plt.show()
else:
    print("La columna 'vict_age' no existe en el DataFrame.")
