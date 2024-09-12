import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt


df = pd.read_csv('angelsdata.csv', low_memory=False)

# Verificar los nombres de las columnas
print(df.columns)

# Crear una geometría de puntos a partir de latitudes y longitudes
df['geometry'] = df.apply(lambda row: Point(row['lon'], row['lat']), axis=1)

# Convertir el dataframe de pandas en un GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry='geometry')

# Cargar el mapa base de Los Ángeles
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Visualizar los puntos en el mapa
ax = world[world.name == 'United States'].plot(color='white', edgecolor='black')
gdf.plot(ax=ax, marker='o', color='red', markersize=5)
plt.show()
