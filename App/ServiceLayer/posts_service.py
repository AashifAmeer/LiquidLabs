import httpx
import logging
from App.DbLayer.db_connection import get_db_connection
from App.DbLayer.Repositories.posts_repository import (
    get_posts_by_id,
    get_all_posts,
    create_post
)

API_URL = "https://jsonplaceholder.typicode.com/posts"

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def fetch_post_by_id_from_api(post_id: int):
    # Fetch a specific post by ID from the public API
    try:
        with httpx.Client() as client:
            response = client.get(f"{API_URL}/{post_id}", timeout=30)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        logger.error(f"Error fetching post {post_id} from API: {e}")
        return None

def fetch_all_posts_from_api():
    # Fetch all posts from the public API
    try:
        with httpx.Client() as client:
            response = client.get(API_URL, timeout=30)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        logger.error(f"Error fetching all posts from API: {e}")
        return []

def create_post_in_db(post: dict, conn):
    # Helper function to insert a post into the database
    try:
        create_post(conn, post)
    except Exception as e:
        logger.error(f"Error creating post {post['id']} in DB: {e}")
        raise

def get_post_by_id_service(post_id: int):
    '''
    Retrieve a post by its ID using caching strategy.
    1. Check local database for cached post.
    2. If not found, fetch from public API and store in database.
    '''
    with get_db_connection() as conn:
        cached = get_posts_by_id(conn, post_id)
        if cached: 
            return cached

        api_post = fetch_post_by_id_from_api(post_id)
        if api_post: 
            create_post_in_db(api_post, conn)

        return api_post

def get_all_posts_service():
    '''
    Retrive all posts using caching:
    1. Return DB cached posts if available.
    2. If not, fetch from public API, store in DB, and return.
    '''
    with get_db_connection() as conn:
        cached_posts = get_all_posts(conn)
        if cached_posts: 
            return cached_posts

        api_posts = fetch_all_posts_from_api()
        for post in api_posts:
            create_post_in_db(post, conn)
        
        return api_posts