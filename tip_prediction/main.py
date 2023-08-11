import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load data from CSV file
df = pd.read_csv('D:/Python/Python_Task/tip_prediction/tips.csv')  # Replace with the actual file path

# Create and train the linear regression model
X = df[['total_bill', 'sex', 'time']]
y = df['tip']
model = LinearRegression()
model.fit(X, y)

while True:
    try:
        # User input for prediction
        total_bill = float(input("Enter the total bill amount: "))
        if total_bill < 0:
            print("Total bill amount cannot be negative. Please enter a valid amount.")
            continue
        
        gender_input = int(input("Enter gender (0 for female, 1 for male): "))
        if gender_input not in [0, 1]:
            print("Invalid gender input. Please enter 0 for female or 1 for male.")
            continue
        
        meal_time_input = int(input("Enter meal time (0 for lunch, 1 for dinner): "))
        if meal_time_input not in [0, 1]:
            print("Invalid meal time input. Please enter 0 for lunch or 1 for dinner.")
            continue
        
        # Make prediction
        user_input = np.array([[total_bill, gender_input, meal_time_input]])
        predicted_tip = model.predict(user_input)[0]
        print(f"Predicted tip: ${predicted_tip:.2f}")
        break  # Exit the loop if all inputs are valid
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")





