from fastapi import HTTPException, status
from app.schemas.article import ArticleCreate, ArticleUpdate
from app.models.article import Article
from sqlalchemy.orm.session import Session

def get_all_articles(db: Session):
   return db.query(Article).all()

# Create New Article
def create_article(db: Session, request: ArticleCreate, user_id: int):
   new_article = Article(
      title = request.title,
      content = request.content,
      is_published =  request.is_published,
      user_id = user_id
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

# Update Article
def update_article(db: Session, request: ArticleUpdate, id: int, user_id: int):
   article = db.query(Article).filter(Article.id == id).first()

   if not article:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")
   
   if article.user_id != user_id:
      raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You aren't allowed")
   
   article.title = request.title
   article.content = request.content
   article.is_published = request.is_published

   db.commit()
   db.refresh(article)
   return article

# Delete Article
def delete_article(id: int, db: Session, user_id: int):
   article = db.query(Article).filter(Article.id == id).first()

   if not article:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")
   
   if article.user_id != user_id:
      raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You aren't allowed")
   
   db.delete(article)
   db.commit()
   return {"message": "Article Deleted Successfully!"}
   
   