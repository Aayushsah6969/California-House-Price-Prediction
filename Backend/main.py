# main.py

from fastapi import FastAPI
from app.api import router as api_router, predict
#from app.db.db import db_connection  # Import the function
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Test DB connection on startup
# db_connection()
app.include_router(predict.router)
app.include_router(api_router)
