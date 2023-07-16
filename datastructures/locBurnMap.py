import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

data = pd.read_csv('datastructures/fireDataCondense.csv')

# Assuming 'california.shp' is the shapefile for California
california = gpd.read_file('datastructures/map/cali.shp')

# Create a GeoSeries with the same length as the DataFrame
geometry = gpd.points_from_xy(data['LONGITUDE'], data['LATITUDE'])

# Create a GeoDataFrame with the GeoSeries as the geometry
gdf = gpd.GeoDataFrame(data, geometry=geometry)

# Plot the California map
california_color = (213/255, 213/255, 196/255) 
california.plot(color=california_color, edgecolor='black', figsize=(10, 8))
cmap = plt.cm.get_cmap('jet')

# Plot the bubbles and set the color based on the 'BUBBLESIZE' column
gdf.plot(ax=plt.gca(), marker='o', c=data['BUBBLESIZE'], cmap='jet', markersize=10, alpha=0.7)

# Add the hex number of each bubble as labels
for idx, row in gdf.iterrows():
    color = cmap(mcolors.Normalize()(row['BUBBLESIZE']))
    plt.gca().annotate(f'{row["ACRES"]:.2f}', xy=(row['LONGITUDE'], row['LATITUDE']), xytext=(3, 3),
                       textcoords='offset points', fontsize=8, color=color, weight='bold')

# Plot the bubbles
gdf.plot(ax=plt.gca(), marker='o', cmap='jet', markersize=data['BUBBLESIZE'], alpha=0.7)

plt.title('California Fire Spots')
plt.axis('off')

# Save the plot as an image (e.g., PNG)
plt.savefig('map.png', bbox_inches='tight', pad_inches=0)

# Close the plot
plt.close()
