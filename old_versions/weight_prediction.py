import pandas as pd

from sklearn.linear_model import LinearRegression

# Load Dataset
data = pd.read_csv("data/fitness_data.csv")
# Input Features
X = data[["age", "weight", "height", "calories", "workout_hours"]]

# Output Target
y = data["target_weight"]

# Create AI Model
model = LinearRegression()

# Train Model
model.fit(X, y)

print("AI Model Trained Successfully 🔥")

# User Inputs
age = int(input("Enter age: "))

weight = float(input("Enter current weight: "))

height = float(input("Enter height (cm): "))

calories = int(input("Enter daily calories: "))

workout = float(input("Enter workout hours/day: "))

# Prediction
prediction = model.predict([[age, weight, height, calories, workout]])

# Final Output
print("\nPredicted Future Weight:", round(prediction[0], 2), "kg")