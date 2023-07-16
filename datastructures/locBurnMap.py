import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.lines import Line2D


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


# #-------------
# # Plot the bubbles and set the color based on the 'BUBBLESIZE' column
# # Use 'viridis' colormap to map the values to colors
# gdf.plot(ax=plt.gca(), marker='o', c=data['BUBBLESIZE'], cmap='viridis', markersize=10, alpha=0.7)

# # Add the hex number of each bubble as labels
# for idx, row in gdf.iterrows():
#     color = cmap(mcolors.Normalize()(row['BUBBLESIZE']))
#     plt.gca().text(row['LONGITUDE'], row['LATITUDE'], f'{row["ACRES"]:.2f}', ha='center', va='bottom', fontsize=8, color=color)
# #---------
gdf.plot(ax=plt.gca(), marker='o', c=data['BUBBLESIZE'], cmap='jet', markersize=10, alpha=0.7)

# Add the hex number of each bubble as labels
for idx, row in gdf.iterrows():
    color = cmap(mcolors.Normalize()(row['BUBBLESIZE']))
    plt.gca().annotate(f'{row["ACRES"]:.2f}', xy=(row['LONGITUDE'], row['LATITUDE']), xytext=(3, 3),
                       textcoords='offset points', fontsize=8, color=color, weight='bold')

   # plt.gca().annotate(f'{row["ACRES"]:.2f}', xy=(row['LONGITUDE'], row['LATITUDE']), xytext=(3, 3), textcoords='offset points', fontsize=8, color=color)

# Plot the bubbles
gdf.plot(ax=plt.gca(), marker='o', cmap='jet', markersize=data['BUBBLESIZE'], alpha=0.7)


# #legend
# # Create custom legend entries for name and acres burnt
# legend_elements = [Line2D([], [], marker='o', color='none', markersize=10, alpha=0.7),
#                    Line2D([], [], linestyle='', marker='o', markersize=0, label='Name'),
#                    Line2D([], [], linestyle='', marker='o', markersize=0, label='Acres Burnt')]

# # Add custom legend entries to the upper right corner
# plt.legend(handles=legend_elements, loc='upper right')

# Plot the bubbles and use a colormap to set the color based on the 'BUBBLESIZE' column


plt.title('California Fire Spots')
plt.axis('off')

plt.show()
#mplleaflet.display() #i dont have Ipython

