from fastapi import HTTPException, status
from app.models.user import User
from app.schemas.user import UserBase
from sqlalchemy.orm.session import Session
from app.utils.hash import Hash

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
def update_user(db: Session, request: UserBase, id: int, user_id: int):
    user_obj = db.query(User).filter(User.id == id).first()
    
    if not user_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    if id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You aren't allowed")

    user_obj.username = request.username
    user_obj.email = request.email
    user_obj.is_active = request.is_active
    user_obj.password = Hash.bcrypt(request.password)

    db.commit()
    db.refresh(user_obj)
    return user_obj

# Delete User
def delete_user(db: Session, id: int, user_id: int):
   user = db.query(User).filter(User.id == id).first()
   if not user:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
   
   if id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You aren't allowed")
   
   db.delete(user)
   db.commit()
   return {"message": "User Deleted Successfully!"}
