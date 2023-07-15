import pandas as pd

#--------------------------------------
#aggregate data
#step 1: make categories

# totalacres=np.array()
# acrecount=0

# def locAcre(file_name, column1, column 2)
# for name1 in data['UNIT_ID']:
#     for names in data['UNIT_ID']:
#         if name1==names:
            

#     if name==
# if data['UNIT_ID']
#-------------------------------------


# def calculate_total_acre(file_path, name_column, acre_column):
    # Read the CSV file
data = pd.read_csv('datastructures/fireData.csv')
# print(data.head())
print(3)

    # Create a dictionary to store the total acreage for each name
total_acreage = {}

    # Iterate over the rows
for index, row in data.iterrows():
    name = row[data['UNIT_ID']]
    acre = row[data['GIS_ACRES']]

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