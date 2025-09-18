import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Train the model
def train_model():
    data = pd.read_csv("Crop_recommendation.csv")

    X = data.iloc[:, :-1]  # All columns except the label
    y = data.iloc[:, -1]   # The label column

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    print("Model trained with accuracy:", accuracy)

    # Save the model to model.pkl
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)

# Predict using the model
def predict_crop(input_data):
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    prediction = model.predict([np.array(input_data)])
    return prediction[0]

# Run this file to train and save model
if __name__ == "__main__":
    train_model()