import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import base64

data = pd.read_csv('datastructures/fireDataCondense.csv')

# Assuming 'california.shp' is the shapefile for California
california = gpd.read_file('datastructures/map/cali.shp')

# Create a GeoSeries with the same length as the DataFrame
geometry = gpd.points_from_xy(data['LONGITUDE'], data['LATITUDE'])

# Create a GeoDataFrame with the GeoSeries as the geometry
gdf = gpd.GeoDataFrame(data, geometry=geometry)

# Plot the California map
california.plot(color='lightgray', edgecolor='black', figsize=(10, 8))
cmap = plt.cm.get_cmap('jet')

# Plot the bubbles and set the color based on the 'BUBBLESIZE' column
gdf.plot(ax=plt.gca(), marker='o', c=data['BUBBLESIZE'], cmap='jet', markersize=10, alpha=0.7)

# Add the area size as labels to the bubbles
for idx, row in gdf.iterrows():
    color = cmap(mcolors.Normalize()(row['BUBBLESIZE']))
    plt.gca().annotate(f'{row["ACRES"]:.2f}', xy=(row['LONGITUDE'], row['LATITUDE']), xytext=(3, 3),
                       textcoords='offset points', fontsize=8, color=color, weight='bold')

# Save the plot as an image
plt.savefig('templates/fires_plot.png', bbox_inches='tight')

# Generate the HTML content
html_content = '''
<!DOCTYPE html>
<html>
<head>
  <title>NatureAlert</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      background-color: #f5f0e1;
    }

    header {
      background-color: #e0c07f;
      padding: 20px;
      text-align: center;
    }

    h1 {
      margin: 0;
      font-size: 30px;
      color: black;
      border: None;
      text-decoration: None;
    }

    a {
      text-decoration: None;
    }

    .tabs {
      display: flex;
      justify-content: center;
      margin-top: 5px;
      padding: 5px;
    }

    .tabs a {
      display: inline-block;
      color: black;
      text-decoration: none;
      padding: 5px;
      padding-left: 20px;
      padding-right: 20px;
      background-color: #d1af6c;
    }

    .tabs a:hover {
      background-color: #b7944e;
      padding: 5px;
      padding-left: 20px;
      padding-right: 20px;
    }

    .content {
      margin-top: 20px;
      padding: 20px;
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
    }

    .content-box {
      width: 100%;
      background-color: #fff;
      padding: 20px;
      margin-bottom: 20px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
      text-align: center;
    }

    .content-box img {
      width: 30%;
      height: auto;
      float: right;
      margin: 0 0 10px 10px;
    }

    .content-box h2 {
      text-align: center;
      margin: 0px;
    }

    .content-box .btn {
      display: float;
      margin: 0 auto;
      padding: 10px 20px;
      background-color: #d1af6c;
      color: black;
      text-decoration: none;
      border-radius: 5px;
      margin-top: 10px;
      text-align: center;
    }

    .content-box p {
      text-align: left;
      margin-bottom: 20px;
      padding-left: inherit;
      padding-right: inherit;
    }
  </style>
</head>
<body>
  <header>
    <h1>NatureAlert</h1>
    <div class="tabs">
      <a href="/">Home</a>
      <a href="/droughts">Droughts</a>
      <a href="/fires">Fires</a>
    </div>
  </header>

  <div class="content">
    <div class="content-box">
      <h2>California Fire Spots</h2>
      <img src="data:image/png;base64,{image}">
      <h2>Predict Total Acres Burned in 2025</h2>
      <form>
        <button onclick="predict()">Predict</button>
      </form>
      <p id="prediction" style="display: none;"></p>
      <script>
        function predict() {
          var prediction = 10000;  // Replace with the actual prediction value
          document.getElementById('prediction').innerHTML = 'Total Acres Burned in 2025: ' + prediction.toFixed(2);
          document.getElementById('prediction').style.display = 'block';
        }
      </script>
    </div>
  </div>
</body>
</html>
'''.format(image=base64.b64encode(open('templates/fires_plot.png', 'rb').read()).decode())

# Save the HTML content to a file
with open('templates/fires.html', 'w') as f:
    f.write(html_content)
