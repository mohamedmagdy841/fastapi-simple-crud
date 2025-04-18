from fastapi import HTTPException, status
from models import User
from schemas import UserBase
from sqlalchemy.orm.session import Session
from utils.hash import Hash

# Get All Users
def get_all_users(db: Session):
  return db.query(User).all()

# Get User
def get_user(db: Session, id: int):
   user = db.query(User).filter(User.id == id).first()
   if not user:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
   return user

# Update User
def update_user(db: Session, request: UserBase, id: int):
   user = db.query(User).filter(User.id == id)
   if not user.first():
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
   user.update({
      User.username: request.username,
      User.email: request.email,
      User.is_active: request.is_active,
      User.password: Hash.bcrypt(request.password)
      
   })
   db.commit()
   return {"message": "User Updated Successfully!"}

# Delete User
def delete_user(db: Session, id: int):
   user = db.query(User).filter(User.id == id).first()
   if not user:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
   db.delete(user)
   db.commit()
   return {"message": "User Deleted Successfully!"}
