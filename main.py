# main.py

from fastapi import FastAPI
from app.api import router as api_router, predict
from app.db.db import db_connection  # Import the function

app = FastAPI()

# Test DB connection on startup
db_connection()
app.include_router(predict.router)
app.include_router(api_router)
