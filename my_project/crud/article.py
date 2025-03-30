from database.models import Article
from schemas import ArticleBase
from sqlalchemy.orm.session import Session

# Create New Article
def create_article(db: Session, request: ArticleBase):
   new_article = Article(
      title = request.title,
      content = request.content,
      is_published =  request.is_published,
      user_id = request.user_id
   )
   db.add(new_article)
   db.commit()
   db.refresh(new_article)
   return new_article

# Get Articles of User
def get_article(db: Session, user_id: int):
   article = db.query(Article).filter(Article.user_id == user_id).all()
   return article