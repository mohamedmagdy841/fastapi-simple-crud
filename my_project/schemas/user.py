from pydantic import BaseModel, EmailStr


class Article(BaseModel):
    title: str
    content: str
    is_published: bool
    class Config():
        from_attributes = True


class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str
    is_active: bool

class UserResponse(BaseModel):
    username: str
    email: str
    is_active: bool
    items: list[Article] = []
    class Config():
        from_attributes = True
