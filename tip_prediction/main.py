import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# Load data from CSV file
df = pd.read_csv('D:\Python\Python_Task\tip_prediction')  # Replace 'your_data_file.csv' with the actual file name

# Encoding categorical variables (sex and time) using LabelEncoder
label_encoder = LabelEncoder()
df['sex_encoded'] = label_encoder.fit_transform(df['sex'])
df['time_encoded'] = label_encoder.fit_transform(df['time'])

# Create and train the linear regression model
X = df[['total_bill', 'sex_encoded', 'time_encoded']]
y = df['tip']
model = LinearRegression()
model.fit(X, y)

# User input for prediction
total_bill = float(input("Enter the total bill amount: "))
gender = input("Enter gender (female/male): ").capitalize()
meal_time = input("Enter meal time (lunch/dinner): ").capitalize()

# Encoding user input
gender_encoded = label_encoder.transform([gender])[0]
meal_time_encoded = label_encoder.transform([meal_time])[0]

# Creating input features for prediction
user_input = np.array([[total_bill, gender_encoded, meal_time_encoded]])

# Make prediction
predicted_tip = model.predict(user_input)[0]
print(f"Predicted tip: ${predicted_tip:.2f}")
