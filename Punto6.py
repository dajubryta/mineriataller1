import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('angelsdata.csv', low_memory=False)

# Verificar los nombres de las columnas
print(df.columns)

# Asegurarse de que las columnas de latitud y longitud existen y están correctamente nombradas
if 'lat' in df.columns and 'lon' in df.columns:
    # Crear una geometría de puntos a partir de latitudes y longitudes
    df['geometry'] = df.apply(lambda row: Point(row['lon'], row['lat']), axis=1)

    # Convertir el dataframe de pandas en un GeoDataFrame
    gdf = gpd.GeoDataFrame(df, geometry='geometry')

    # Establecer el CRS para el GeoDataFrame
    gdf.set_crs(epsg=4326, inplace=True)

    # Cargar el mapa base de Los Ángeles (puedes utilizar un shapefile o un mapa base desde GeoPandas)
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Reproyectar el mapa base al mismo CRS que el GeoDataFrame
    world = world.to_crs(epsg=4326)

    # Visualizar los puntos en el mapa
    ax = world[world.name == 'United States'].plot(color='white', edgecolor='black')
    gdf.plot(ax=ax, marker='o', color='red', markersize=5)
    plt.title('Incidentes en Los Ángeles')
    plt.show()
else:
    print("Las columnas 'lat' y 'lon' no se encuentran en el DataFrame.")
