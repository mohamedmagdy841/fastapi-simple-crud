from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    class Config():
        from_attributes = True


class ArticleBase(BaseModel):
    title: str
    content: str
    is_published: bool
    user_id: int

class ArticleResponse(BaseModel):
    title: str
    content: str
    is_published: bool
    user: User
    class Config():
        from_attributes = True