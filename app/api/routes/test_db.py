# app/api/routes/test_db.py

from fastapi import APIRouter
from sqlalchemy import text
from app.db.db import engine

router = APIRouter()

@router.get("/db-time", tags=["DB Test"])
def get_db_time():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT NOW()")).fetchone()
            return {"db_time": result[0]}
    except Exception as e:
        return {"error": str(e)}
