import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('angelsdata.csv', low_memory=False)

# Agrupar por tipo de delito (Crm Cd) y contar el número de incidentes
incidentes_por_tipo_delito = df.groupby('Crm Cd').size()

# Crear el gráfico de barras
incidentes_por_tipo_delito.plot(kind='bar', figsize=(10, 6))
plt.title('Número de incidentes por tipo de delito')
plt.xlabel('Código de delito')
plt.ylabel('Número de incidentes')
plt.show()
