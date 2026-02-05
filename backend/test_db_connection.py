import sys
import os
from sqlalchemy import create_engine, text

# Use the same logic as database.py
DATABASE_URL = "postgresql://postgres:root@localhost/phonebook"

print(f"Testing connection to: {DATABASE_URL}")

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        print(f"SUCCESS! Connected to PostgreSQL: {result.fetchone()[0]}")
except Exception as e:
    print(f"FAILED to connect: {e}")
    sys.exit(1)
