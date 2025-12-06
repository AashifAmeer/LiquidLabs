import sqlite3
import logging
from typing import Optional, List, Dict

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def get_posts_by_id(conn: sqlite3.Connection, post_id: int) -> Optional[Dict]:
    # Retrieve a post by its ID from the database'''
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts WHERE id = ?", (post_id,))
        row = cursor.fetchone()
        return dict(row) if row else None
    except Exception as e:
        logger.error(f"Error fetching post by id {post_id}: {e}")
        raise

def get_all_posts(conn: sqlite3.Connection) -> List[Dict]:
    # Retrieve all posts from the database, ordered by their ID
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts ORDER BY id ASC")
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    except Exception as e:
        logger.error(f"Error fetching all posts: {e}")
        raise

def create_post(conn: sqlite3.Connection, post: Dict) -> None:
    # Insert a new post record into the database
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO posts (id, userId, title, body) VALUES (?, ?, ?, ?)",
            (post['id'], post['userId'], post['title'], post['body'])
        )
        conn.commit()
    except Exception as e:
        logger.error(f"Error creating post {post['id']}: {e}")
        raise