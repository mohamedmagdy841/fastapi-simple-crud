from fastapi import HTTPException, status
from models import Article
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

# Get Article
def get_article(db: Session, id: int):
   article = db.query(Article).filter(Article.id == id).first()
   if not article:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")
   return article