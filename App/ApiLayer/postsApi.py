from fastapi import APIRouter, HTTPException
from App.Scehmas.post_model import PostModel
from App.ServiceLayer.posts_service import (
    get_post_by_id_service,
    get_all_posts_service
)

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.get("/", response_model=list[PostModel])
def get_all_posts():
    try:
        posts = get_all_posts_service()
        return posts
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{post_id}", response_model=PostModel)
def get_post_by_id(post_id: int):
    try:
        post = get_post_by_id_service(post_id)
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")
        return post
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))