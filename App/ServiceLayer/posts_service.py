import httpx
from App.DbLayer.db_connection import get_db_connection
from App.DbLayer.Repositories.posts_repository import (
    get_posts_by_id,
    get_all_posts,
    create_post
)

API_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_post_by_id_from_api(post_id: int):
    try:
        with httpx.Client() as client:
            response = client.get(f"{API_URL}/{post_id}", timeout=30)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        print(f"Error fetching post from API: {e}")
        raise

def fetch_all_posts_from_api():
    try:
        with httpx.Client() as client:
            response = client.get(API_URL, timeout=30)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        print(f"Error fetching posts from API: {e}")
        raise

def create_post_in_db(post: dict):
    conn = get_db_connection()
    try:
        create_post(conn, post)
    except Exception as e:
        print(f"Error creating post in DB: {e}")
        raise
    finally:
        conn.close()

def get_post_by_id_service(post_id: int):
    conn = get_db_connection()
    try:
        cached = get_posts_by_id(conn, post_id)
        if cached: return cached

        api_post = fetch_post_by_id_from_api(post_id)
        if not api_post: return None

        create_post_in_db(api_post)
        return api_post
    
    except Exception as e:
        print(f"Error getting post by ID from DB: {e}")
        raise
    finally:
        conn.close()

def get_all_posts_service():
    conn = get_db_connection()
    try:
        cached_posts = get_all_posts(conn)
        if cached_posts: return cached_posts

        api_posts = fetch_all_posts_from_api()
        for post in api_posts:
            create_post_in_db(post)
        
        return api_posts
    
    except Exception as e:
        print(f"Error getting all posts from DB: {e}")
        raise
    finally:
        conn.close()