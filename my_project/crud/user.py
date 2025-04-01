from fastapi import HTTPException, status
from database.models import User
from schemas import UserBase
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
