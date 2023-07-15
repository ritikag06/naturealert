import csv
import matplotlib.pyplot as plt
import mpld3
from matplotlib.ticker import FuncFormatter
import mpld3.plugins as plugins

# Data extraction
week = []
total_population = []
total_area = []

with open('datastructures/droughts.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        week.append(row['Week'])
        total_population.append(int(row['TotalPopulation'].replace(',', '')))
        total_area.append(int(row['TotalArea'].replace(',', '')))

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(week, total_area)
ax.set_xlabel('Week')
ax.set_ylabel('Total Area')
ax.set_title('Drought Area in California by Week 2023 (Sq. Miles)')

# Define custom formatter for y-axis labels
def population_formatter(x, pos):
    """Format the y-axis labels without '2023'"""
    return f'{x:,}'.replace('2023', '')

ax.yaxis.set_major_formatter(FuncFormatter(population_formatter))

# Add interactive tooltips showing the total area
tooltip_labels = [f'Total Area: {area:,}' for area in total_area]
plugins.connect(fig, plugins.PointLabelTooltip(bars, labels=tooltip_labels))

# Convert the plot to an interactive HTML
html_plot = mpld3.fig_to_html(fig)

# Save the interactive HTML plot to a file
with open('interactive_plot.html', 'w') as file:
    file.write(html_plot)
