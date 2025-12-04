import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / 'Instance' / 'liquidlabs.db'

DB_PATH.parent.mkdir(parents=True, exist_ok=True)

CREATE_POSTS_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY,
    userId INTEGER,
    title TEXT,
    body TEXT
);
"""

def initialize_db():
    # Create the database and posts table if they don't exist
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(CREATE_POSTS_TABLE_QUERY)
        conn.commit()
        print("Database initialized successfully.")
    except Exception as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

def get_db_connection():
    # Establish a connection to the database
    try:
        conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        raise