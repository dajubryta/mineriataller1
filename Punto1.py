import pandas as pd

df = pd.read_csv('angelsdata.csv', low_memory=False)

# Mostrar las primeras 5 filas del dataframe
print(df.head())

