from fastapi import APIRouter
from app.api.routes import test_db

router = APIRouter()

router.include_router(test_db.router)

@router.get("/")
def root():
    return {"message": "California House Price Prediction API is live with data"}
