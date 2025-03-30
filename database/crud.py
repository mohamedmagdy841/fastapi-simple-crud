from database.models import Article, User
from schemas import ArticleBase, UserBase
from sqlalchemy.orm.session import Session
from utils.hash import Hash

# Create New User
def create_user(db: Session, request: UserBase):
    new_user = User(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Get All Users
def get_all_users(db: Session):
  return db.query(User).all()

# Get User
def get_user(db: Session, id: int):
   return db.query(User).filter(User.id == id).first()

# Update User
def update_user(db: Session, request: UserBase, id: int):
   user = db.query(User).filter(User.id == id)
   user.update({
      User.username: request.username,
      User.email: request.email,
      User.password: Hash.bcrypt(request.password)
      
   })
   db.commit()
   return {"message": "User Updated Successfully!"}

# Delete User
def delete_user(db: Session, id: int):
   user = db.query(User).filter(User.id == id).first()
   db.delete(user)
   db.commit()
   return {"message": "User Deleted Successfully!"}


#---------------------------------------------------------------

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