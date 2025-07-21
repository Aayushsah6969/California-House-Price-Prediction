# app/ml/predict.py
import joblib
import numpy as np
import os

MODEL_DIR = "app/ml/models"

def load_model(model_name: str):
    path = os.path.join(MODEL_DIR, f"{model_name}.pkl")
    if not os.path.exists(path):
        raise ValueError(f"Model '{model_name}' not found.")
    return joblib.load(path)

def predict_house_price(model_name: str, features: list):
    model = load_model(model_name)
    prediction = model.predict(np.array(features).reshape(1, -1))
    return prediction[0]
