import pandas as pd

from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split

import joblib


def train_model():

    data = pd.read_csv("data/fitness_data.csv")

    X = data[["current_weight", "target_weight"]]

    y = data["months"]

    model = LinearRegression()

    model.fit(X, y)

    joblib.dump(model, "models/weight_model.pkl")

    return model


def load_model():

    return joblib.load("models/weight_model.pkl")


def predict_months(current_weight, target_weight):

    model = load_model()

    prediction = model.predict(
        [[current_weight, target_weight]]
    )

    return round(prediction[0], 1)