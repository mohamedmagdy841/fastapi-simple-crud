from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

class Article(BaseModel):
    title: str
    content: str
    is_published: Optional[bool] = True
    model_config = ConfigDict(from_attributes=True)


class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str
    is_active: Optional[bool] = True

class UserResponse(BaseModel):
    username: str
    email: str
    is_active: Optional[bool] = True
    items: list[Article] = []
    model_config = ConfigDict(from_attributes=True)
