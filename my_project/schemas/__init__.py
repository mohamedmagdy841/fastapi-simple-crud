from schemas.user import UserBase, UserResponse
from schemas.article import ArticleBase, ArticleResponse

# Fix forward references
UserResponse.model_rebuild()
ArticleResponse.model_rebuild()
