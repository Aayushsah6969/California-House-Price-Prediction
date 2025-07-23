from fastapi import APIRouter
from pydantic import BaseModel
import joblib
import numpy as np
import os

router = APIRouter()

# Load models once
models_dir = "app/ml/models"
model_files = {
    "LinearRegression": "LinearRegression.pkl",
    "DecisionTree": "DecisionTree.pkl",
    "RandomForest": "RandomForest.pkl",
    "GradientBoosting": "GradientBoosting.pkl",
    "SVR": "SVR.pkl"
}
models = {}

for name, file in model_files.items():
    model_path = os.path.join(models_dir, file)
    models[name] = joblib.load(model_path)

# Input schema
class HouseFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@router.post("/predict")
def predict_price(features: HouseFeatures):
    input_array = np.array([[features.MedInc, features.HouseAge, features.AveRooms,
                             features.AveBedrms, features.Population, features.AveOccup,
                             features.Latitude, features.Longitude]])
    
    predictions = {}
    for name, model in models.items():
        price = model.predict(input_array)[0]
        predictions[name] = round(price, 2)

    return {"predicted_prices": predictions}
