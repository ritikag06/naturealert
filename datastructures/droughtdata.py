import pandas as pd
import matplotlib.pyplot as plt
import mplcursors
import mpld3

# Read the data from the CSV file
data = pd.read_csv('datastructures/droughts.csv')

# Remove commas from numeric values and convert them to integers
data['TotalPopulation'] = data['TotalPopulation'].str.replace(',', '').astype(int)
data['TotalArea'] = data['TotalArea'].str.replace(',', '').astype(int)

# Create a bar graph
fig, ax = plt.subplots(figsize=(10, 6))
bar_plot = ax.bar(data.index, data['TotalArea'])

# Set the x-axis tick labels as the weeks
ax.set_xticks(data.index)
ax.set_xticklabels(data['Week'], rotation=90)

# Set the title and axis labels
ax.set_title('Area (Sq. Miles) in Drought in California by Week since Jan 2023')
ax.set_xlabel('Weeks since Jan 2023')
ax.set_ylabel('Total Square Miles')

# Set the maximum width of the plot to 500 pixels
fig.set_size_inches(min(500, fig.get_size_inches()[0]), fig.get_size_inches()[1])

# Create a function to display the tooltip
def on_hover(event):
    index = int(event.target.index)
    week = data.loc[index, 'Week']
    population = data.loc[index, 'TotalPopulation']
    area = data.loc[index, 'TotalArea']
    plt.gca().set_title(f"Week: {week}\nTotal Population: {population}\nTotal Area: {area}")

# Connect the tooltip function to the bar graph
mplcursors.cursor(bar_plot).connect("add", on_hover)

# Create a function to handle the click event
def on_click(event):
    if event.artist in bar_plot:
        index = int(event.artist.get_x() + event.artist.get_width() / 2)
        area = data.loc[index, 'TotalArea']
        ax.annotate(str(area), (event.artist.get_x() + event.artist.get_width() / 2, event.artist.get_height()), 
                     xytext=(0, 5), textcoords='offset points', ha='center', va='bottom', color='black')

# Connect the click event to the bar graph
fig.canvas.mpl_connect('button_press_event', on_click)

# Convert the plot to an interactive HTML representation
html_fig = mpld3.fig_to_html(fig)

# Define the CSS styles
css_styles = '''
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
</style>
'''

# Create an HTML file and embed the interactive graph
html_content = f'''
<!DOCTYPE html>
<html>
<head>
  <title>NatureAlert</title>
  {css_styles}
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
      {html_fig}
    </div>
  </div>

  <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
  <script>
    // JavaScript code here
  </script>
</body>
</html>
'''

# Save the HTML content to a file
with open('templates/interactive_graph.html', 'w') as f:
    f.write(html_content)
