
# 📘 ML Web App — Phase 1 Plan

---

## 🧠 Project Overview

End-to-end ML system:
- Users input features via React frontend
- 5 ML models (Logistic, KNN, DT, SVM, RF) predict and return results
- Users provide feedback: ✅ Correct, ❌ Incorrect, 😐 Neutral
- All predictions & feedback saved in PostgreSQL
- Admin features:
  - View feedback stats
  - Trigger model retraining
  - Upload new training data

---

## ⚙️ Tech Stack

| Layer           | Technology                                      |
|-----------------|-------------------------------------------------|
| ML Models       | Scikit-learn (Logistic, KNN, DT, SVM, RF)        |
| Backend API     | FastAPI                                         |
| Database        | PostgreSQL                                      |
| Frontend        | React.js                                        |
| Admin Panel     | React + role-based routing                      |
| Visualization   | Chart.js / Recharts (React)                     |

---


## 📂 Planned Folder Structure

```
ml-web-app/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models/      # Saved ML models (.pkl)
│   │   ├── routes/      # FastAPI route handlers
│   │   ├── schemas/     # Pydantic models
│   │   ├── services/    # Model logic, prediction, training
│   │   ├── database/    # DB connection + models (SQLAlchemy)
│   │   └── utils/
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── services/    # API communication
│   └── package.json
└── README.md
```

---


## 🪜 Phase 1 Development Plan

### 1. 📊 Dataset & Model Training
- Select dataset (e.g., Wine Quality, Heart Disease)
- Train 5 ML models
- Save models as `.pkl` (joblib)
- Create `train.py` for reproducibility
- Save sample predictions

---

### 2. ⚙️ Backend (FastAPI)
- Initialize FastAPI project (`main.py`, `uvicorn`)
- Set up PostgreSQL (SQLAlchemy or Tortoise)
- API routes:
  - `POST /predict`: Input → predictions from 5 models
  - `POST /feedback`: Save user feedback
  - `GET /feedback-stats`: Model success/neutral/failure rates
  - `POST /admin/train`: Retrain models
  - `POST /admin/upload`: Upload new CSV data
- Pydantic schemas: `PredictionInput`, `PredictionOutput`, `Feedback`, `TrainingDataUpload`
- Log API requests

---

### 3. 🗄️ Database (PostgreSQL)
- Tables:
  - `predictions`: user input, model name, output, timestamp
  - `feedback`: prediction_id, feedback_type
  - `training_data`: raw CSV rows (optional)
- Alembic migrations (optional)

---

### 4. 🌐 Frontend (React.js)
- Dashboard UI:
  - Form for input features
  - Show predictions from 5 models
  - Feedback buttons: ✅ / ❌ / 😐
- Admin Panel:
  - Feedback breakdown (charts)
  - Upload CSV for training
  - Retrain button

---

### 5. 🔁 Admin-Triggered Training
- Admin clicks “Retrain”
- Frontend requests `/admin/train`
- Backend retrains models with all data
- New `.pkl` files replace old
- Log training history

---


## 🧪 Sample User Flow

1. User inputs features → clicks “Predict”
2. FastAPI returns predictions from 5 models
3. User gives feedback (correct, wrong, neutral)
4. Feedback saved in DB
5. Admin views stats in panel
6. Admin uploads new data or retrains models

---

## 📈 Admin Stats To Track
- Model accuracy (user feedback)
- Count of correct / incorrect / neutral per model
- Last training time
- Data volume collected

---

## 🔐 Phase 2 Ideas (Future)
- User login / feedback tied to profile
- Email alerts for low-accuracy models
- Auto-retraining (weekly or volume-based)
- Docker + CI/CD deployment

---

## ✅ Summary

| Component      | Status                  |
|---------------|-------------------------|
| ✅ Planning    | Done                    |
| ✅ Tech Stack  | FastAPI + React + PostgreSQL |
| 🚧 Backend API | To Start                |
| 🚧 ML Models   | 5 already trained       |
| 🚧 Feedback    | In Plan                 |
| 🚧 Admin Panel | In Plan                 |

---


