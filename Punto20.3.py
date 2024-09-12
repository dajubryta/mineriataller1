import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('angelsdata.csv', low_memory=False)

# Agrupar por día de la semana y contar el número de incidentes
incidentes_por_dia = df.groupby('Day of Week').size()

# Crear el gráfico de barras
incidentes_por_dia.plot(kind='bar', figsize=(10, 6))
plt.title('Número de incidentes por día de la semana')
plt.xlabel('Día de la semana')
plt.ylabel('Número de incidentes')
plt.show()
