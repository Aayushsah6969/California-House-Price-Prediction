# 🏡 California House Price Prediction

A fullstack machine learning web application to predict median house values in California based on multiple input features. Built with **FastAPI** for the backend, **React** for the frontend, and trained using **scikit-learn** models.

---


## 🚀 Features

- 🧠 Trains multiple ML models (Linear Regression, Random Forest, Gradient Boosting, etc.)
- 📦 Saves and serves trained models via FastAPI
- 🧪 Predicts house prices using input features like income, location, rooms, etc.
- 🌐 React frontend with user input form and result display
- 🔗 Connected to PostgreSQL for DB operations
- 🧾 CORS-enabled for smooth frontend-backend integration
- 🗃️ Optional: stores predictions + feedback for future retraining

---

## 🛠️ Tech Stack

- **Backend**: FastAPI, SQLAlchemy, PostgreSQL, scikit-learn, pandas, joblib
- **Frontend**: React, Vite
- **ML Models**: RandomForest, GradientBoosting, SVR, etc.

---

## 🧪 Sample Input & Output

### ✅ Sample Input (features):
```json
{
  "longitude": -122.23,
  "latitude": 37.88,
  "housing_median_age": 41.0,
  "total_rooms": 880.0,
  "total_bedrooms": 129.0,
  "population": 322.0,
  "households": 126.0,
  "median_income": 8.3252
}
