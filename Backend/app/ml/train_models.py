import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
import joblib
import os

# Load California Housing dataset from sklearn
california = fetch_california_housing()
X = california.data
y = california.target
feature_names = california.feature_names

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define models
models = {
    "LinearRegression": LinearRegression(),
    "DecisionTree": DecisionTreeRegressor(),
    "RandomForest": RandomForestRegressor(n_estimators=100),
    "GradientBoosting": GradientBoostingRegressor(),
    "SVR": SVR()
}

# Output directory
model_dir = "app/ml/models"
os.makedirs(model_dir, exist_ok=True)

# Train, evaluate, and save models
for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    print(f"{name}: RMSE = {rmse:.2f}")
    
    # Save model
    joblib.dump(model, f"{model_dir}/{name}.pkl")
