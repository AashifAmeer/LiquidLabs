from fastapi import APIRouter, HTTPException
from App.Schemas.post_model import PostModel
from App.ServiceLayer.posts_service import (
    get_post_by_id_service,
    get_all_posts_service
)

router = APIRouter(prefix="/api/posts", tags=["Posts"])

@router.get("/", response_model=list[PostModel])
def get_all_posts():
    '''
    This function is to retrieve all posts.
    first checks the local SQLite database for cached posts. If none are found,
    it fetches the posts from the public API, stores them in the database,
    and then returns the list of posts.
    '''
    try:
        posts = get_all_posts_service()
        return posts
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{post_id}", response_model=PostModel)
def get_post_by_id(post_id: int):
    '''
    This function is to retrieve a specific post by its ID.
    Checks the local SQLite database for a cached version of the post first. If not found,
    fetches the post from the public API, stores it in the database
    '''
    try:
        post = get_post_by_id_service(post_id)
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")
        return post
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))