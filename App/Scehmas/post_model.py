from pydantic import BaseModel

class PostModel(BaseModel):
    id: int
    userId: int
    title: str
    body: str