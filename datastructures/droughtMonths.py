import pandas as pd
import matplotlib.pyplot as plt



def calculate_total_acre(file_path, week_column, people_column):
    # Read the CSV file
    data = pd.read_csv('datastructures/droughts1.csv')

    # Create a dictionary to store the total acreage for each name
    total_effected = {}
  
    # Iterate over the rows
    for index, row in data.iterrows():
        month = row[week_column]
        people = row[people_column]

        # Check if the name exists in the dictionary
        if month in total_effected:
            total_effected[month] += people
        else:
            total_effected[people] = people

    # Print the total acreage for each name
    for month, acre in total_effected.items():
        print(month, ":", people)
        print("done")

    names = list(total_effected.keys())
    acres = list(total_effected.values())

    plt.bar(month, people)
    plt.xlabel('Month')
    plt.ylabel('Total ppl') 
    plt.title('Total Acreage by Name')
    # # plt.xticks(rotation=90)
    plt.show()

# Call the function with the appropriate arguments
calculate_total_acre('droughts1.csv', 'Week', 'TotalPopulation')

