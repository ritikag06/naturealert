import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import webbrowser

# Step 1: Load the data
data_2014 = pd.read_csv('datastructures/firesdata/2014.csv')
data_2015 = pd.read_csv('datastructures/firesdata/2015.csv')
data_2016 = pd.read_csv('datastructures/firesdata/2016.csv')
data_2017 = pd.read_csv('datastructures/firesdata/2017.csv')

# Step 2: Concatenate the data
all_data = pd.concat([data_2014, data_2015, data_2016, data_2017])

# Step 3: Data preprocessing
all_data['GIS ACRES'] = all_data['GIS ACRES'].str.replace(',', '').astype(float)

# Step 4: Handle missing values by dropping rows with missing values
all_data.dropna(subset=['GIS ACRES'], inplace=True)

# Step 5: Splitting the data into training and testing sets
X = all_data[['YEAR']]
y = all_data['GIS ACRES']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Model selection
model = LinearRegression()

# Step 7: Model training
model.fit(X_train, y_train)

# Step 8: Model evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

# Step 9: Predicting for the next year
next_year_X = pd.DataFrame({'YEAR': [2025]})
next_year_prediction = model.predict(next_year_X)

# Generate the HTML content
html_content = f'''
<!DOCTYPE html>
<html>
<head>
  <title>Prediction Result</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 20px;
    }}

    .result-box {{
      display: none;  /* Initially hide the result box */
      margin-bottom: 20px;
    }}

    .button {{
      padding: 10px 20px;
      background-color: #d1af6c;
      color: black;
      text-decoration: none;
      border-radius: 5px;
      font-weight: bold;
    }}
  </style>
</head>
<body>
  <h1>Predicted Total Acres Burned in 2025</h1>
  <div class="result-box" id="result-box">
    <h2 id="prediction-result"></h2>
  </div>
  <a href="javascript:void(0);" class="button" onclick="predict()">Predict the Total Acres that will Burn in 2025</a>

  <script>
    function predict() {{
      var resultBox = document.getElementById('result-box');
      var predictionResult = document.getElementById('prediction-result');
      var button = document.querySelector('.button');
      
      // Make a request to the server or perform any necessary computations here
      
      // Update the result
      predictionResult.innerHTML = 'Loading...';
      
      // Simulate delay for demonstration purposes
      setTimeout(function() {{
        predictionResult.innerHTML = '{next_year_prediction[0]}';
        resultBox.style.display = 'block';  // Show the result box
      }}, 2000);
      
      // Disable the button after clicking
      button.disabled = true;
    }}
  </script>
</body>
</html>
'''

# Save the HTML content to a file
with open('templates/fires.html', 'w') as f:
    f.write(html_content)
