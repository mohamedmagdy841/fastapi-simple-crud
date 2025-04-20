from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.schemas.article import Article

class User(BaseModel):
    id: int
    username: str
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
    articles: Optional[List["Article"]] = None
    model_config = ConfigDict(from_attributes=True)

from app.schemas.article import Article
UserResponse.model_rebuild(_types_namespace={"Article": Article})