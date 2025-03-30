from pydantic import BaseModel, EmailStr

class Article(BaseModel):
    title: str
    content: str
    is_published: bool
    class Config():
        from_attributes = True

class User(BaseModel):
    id: int
    username: str
    class Config():
        from_attributes = True


class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    username: str
    email: str
    items: list[Article] = []
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