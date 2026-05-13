import pandas as pd

import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_absolute_error

# Load Dataset
data = pd.read_csv("data/fitness_data.csv")

# Features
X = data[["age", "weight", "height", "calories", "workout_hours"]]

# Target
y = data["target_weight"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Model
model = LinearRegression()

# Train Model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy Check
error = mean_absolute_error(y_test, predictions)

print("Model Error:", round(error, 2))

# Graph
plt.scatter(y_test, predictions)

plt.xlabel("Actual Weight")

plt.ylabel("Predicted Weight")

plt.title("Actual vs Predicted Weight")

plt.show()