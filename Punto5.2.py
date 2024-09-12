import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('angelsdata.csv', low_memory=False)

# Agrupar por género de la víctima (Vict Sex) y contar el número de incidentes
incidentes_por_genero = df.groupby('Vict Sex').size()

# Crear el gráfico de barras
incidentes_por_genero.plot(kind='bar', figsize=(10, 6))
plt.title('Número de incidentes por género de la víctima')
plt.xlabel('Género')
plt.ylabel('Número de incidentes')
plt.show()
