from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import os

# Using your local PostgreSQL password "root"
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:root@localhost/phonebook")

# Ensure PostgreSQL compatibility (psycopg2) and SQLite check_same_thread
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    # Handles postgresql:// and other dialects
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
