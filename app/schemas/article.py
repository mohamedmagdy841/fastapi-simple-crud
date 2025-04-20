from typing import Optional
from pydantic import BaseModel, ConfigDict
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.schemas.user import User


class Article(BaseModel):
    title: str
    content: str
    is_published: Optional[bool] = True
    model_config = ConfigDict(from_attributes=True)

class ArticleBase(BaseModel):
    title: str
    content: str
    is_published: bool

class ArticleCreate(ArticleBase):
    pass

class ArticleUpdate(ArticleBase):
    pass

class ArticleResponse(ArticleBase):
    user: Optional["User"]
    model_config = ConfigDict(from_attributes=True)


from app.schemas.user import User
ArticleResponse.model_rebuild(_types_namespace={"User": User})