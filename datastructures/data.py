import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#TO READ CSV
data= pd.read_csv('datastructures/fireData.csv')

#print(data.describe()) #provides mean,count,std,min,25,50,75,max
#print(data.head()) #prints first few tables

x_values = data['FIRE_NAME']
y_values = data['GIS_ACRES']

#THIS CREATES THE PLOT
plt.bar(x_values, y_values)

plt.title('Fires burnt')
plt.xlabel('Fire name')
plt.ylabel('# of burned acres')

#display graph
plt.show()