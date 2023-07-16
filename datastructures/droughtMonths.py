import pandas as pd
import matplotlib.pyplot as plt



def calculate_total_acre(file_path, week_column, people_column):

    data = pd.read_csv('datastructures/droughts1.csv')

    
    month_mapping = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
       
    }

    
    data['Month'] = data['Month'].map(month_mapping)
    data['Month'] = pd.Categorical(data['Month'], categories=list(month_mapping.values()), ordered=True)


    monthly_population = data.groupby('Month')['TotalPopulation'].sum()
 
  
    plt.figure(figsize=(10, 6))
    monthly_population.plot(kind='line', marker='o', color='blue')
    

    plt.xlabel('Month')
    plt.ylabel('Total Population Affected')
    plt.title('Total Population Affected by Each Month (Line Plot)')
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

calculate_total_acre('datastructures/droughts1.csv', 'Month', 'TotalPopulation')

