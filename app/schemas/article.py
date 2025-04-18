from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    id: int
    username: str
    model_config = ConfigDict(from_attributes=True)


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
    model_config = ConfigDict(from_attributes=True)