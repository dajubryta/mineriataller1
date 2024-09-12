import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('angelsdata.csv', low_memory=False)

# Agrupar por código de arma utilizada (Weapon Used Cd) y contar el número de incidentes
incidentes_por_arma = df.groupby('Weapon Used Cd').size()

# Crear el gráfico de barras
incidentes_por_arma.plot(kind='bar', figsize=(10, 6))
plt.title('Número de incidentes por tipo de arma utilizada')
plt.xlabel('Código de arma')
plt.ylabel('Número de incidentes')
plt.show()
