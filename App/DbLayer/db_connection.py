import sqlite3
import logging
from pathlib import Path
from contextlib import contextmanager

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Define database path
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / 'Instance' / 'liquidlabs.db'

# Ensuring the Instance directory exists
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

# SQL query to create posts table
CREATE_POSTS_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY,
    userId INTEGER,
    title TEXT,
    body TEXT
);
"""

def initialize_db():
    # Create the SQLite database and posts table if they don't exist
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(CREATE_POSTS_TABLE_QUERY)
        logger.info("Database initialized successfully.")
    except Exception as e:
        logger.error(f"Error initializing database: {e}")
        

@contextmanager
def get_db_connection():
    # Establish a connection to the database, used as a context manager to make sure safe opening and closing  
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()