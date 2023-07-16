import pandas as pd


def calculate_total_acre(file_path, name_column, acre_column):
    # Read the CSV file
    data = pd.read_csv('datastructures/fireData.csv')

    # Create a dictionary to store the total acreage for each name
    total_acreage = {}
  
    # Iterate over the rows
    for index, row in data.iterrows():
        name = row[name_column]
        acre = row[acre_column]

        # Check if the name exists in the dictionary
        if name in total_acreage:
            # Add the acreage to the existing total
            total_acreage[name] += acre
        else:
            # Add a new entry in the dictionary for the name
            total_acreage[name] = acre

    # Print the total acreage for each name
    for name, acre in total_acreage.items():
        print(name, ":", acre)

    names = list(total_acreage.keys())
    acreages = list(total_acreage.values())

    # plt.bar(names, acreages)
    # plt.xlabel('Name')
    # plt.ylabel('Total Acreage') 
    # plt.title('Total Acreage by Name')
    # plt.xticks(rotation=90)
    # plt.show()

# Call the function with the appropriate arguments
calculate_total_acre('fireData.csv', 'UNIT_ID', 'GIS_ACRES')




    # (santaclar:60, santaclara:60, tuscane:80)