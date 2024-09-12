import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('angelsdata.csv', low_memory=False)

# Agrupar por área y contar el número de incidentes
incidentes_por_area = df.groupby('AREA').size()

# Crear el gráfico de barras
incidentes_por_area.plot(kind='bar', figsize=(10, 6))
plt.title('Número de incidentes por área geográfica')
plt.xlabel('Área')
plt.ylabel('Número de incidentes')
plt.show()
