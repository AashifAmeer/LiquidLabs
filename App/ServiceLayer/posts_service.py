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
        print(f"Error fetching post {post_id} from API: {e}")
        return None

def fetch_all_posts_from_api():
    try:
        with httpx.Client() as client:
            response = client.get(API_URL, timeout=30)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        print(f"Error fetching posts from API: {e}")
        return []

def create_post_in_db(post: dict, conn):
    try:
        create_post(conn, post)
    except Exception as e:
        print(f"Error creating post in DB: {e}")
        raise

def get_post_by_id_service(post_id: int):
    with get_db_connection() as conn:
        cached = get_posts_by_id(conn, post_id)
        if cached: 
            return cached

        api_post = fetch_post_by_id_from_api(post_id)
        if api_post: 
            create_post_in_db(api_post)

        return api_post

def get_all_posts_service():
    with get_db_connection() as conn:
        cached_posts = get_all_posts(conn)
        if cached_posts: 
            return cached_posts

        api_posts = fetch_all_posts_from_api()
        for post in api_posts:
            create_post_in_db(post, conn)
        
        return api_posts