# app/db/db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/california_db"  # update this

# Create engine
engine = create_engine(DATABASE_URL)

# Create session
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def db_connection():
    try:
        with engine.connect() as connection:
            logging.info("✅ Database connection successful!")
    except Exception as e:
        logging.error(f"❌ Database connection failed: {e}")
