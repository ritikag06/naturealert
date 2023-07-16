import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

data = pd.read_csv('datastructures/fireData.csv')

# Assuming 'california.shp' is the shapefile for California
california = gpd.read_file('caCounty.shp')

# Create a GeoSeries with the same length as the DataFrame
geometry = gpd.points_from_xy(data['Longitude'], data['Latitude'])

# Create a GeoDataFrame with the GeoSeries as the geometry
gdf = gpd.GeoDataFrame(data, geometry=geometry)

# Plot the California map
california.plot(color='lightgray', edgecolor='black', figsize=(10, 8))

# Plot the bubbles
gdf.plot(ax=plt.gca(), marker='o', color='red', markersize=data['BubbleSizeColumn'], alpha=0.7)

plt.title('Bubble Map of California')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show() 