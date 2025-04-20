from datetime import timedelta
import os
from pydantic import EmailStr
from app.schemas.user import UserBase
from sqlalchemy.orm.session import Session
from app.utils.hash import Hash
from app.models.user import User
from fastapi.security import OAuth2PasswordRequestForm
from app.utils.token import create_access_token, verify_token
from fastapi import BackgroundTasks, HTTPException, status
from app.services.send_email import send_email

def register(db: Session, back_task: BackgroundTasks, request: UserBase):
    new_user = User(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()

    back_task.add_task(
        send_email,
        to_email = request.email,
        subject = "Welcome To Our Blog!",
        template_name = "welcome_email.html",
        context={
            "name": request.username
        }
    )

    db.refresh(new_user)
    return new_user

def login(
    form_data: OAuth2PasswordRequestForm,
    db: Session
):
    user = db.query(User).filter(User.username == form_data.username).first()

    if not user or not Hash.verify(user.password, form_data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    
    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

def get_current_user(token: str, db: Session):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
    user = db.query(User).filter(User.username == payload["sub"]).first()
    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="User not found")
    
    return user

def forgot_password(email: EmailStr, back_task: BackgroundTasks, db: Session):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    token = create_access_token({"sub": user.email}, timedelta(minutes=30))
    RESET_PASSWORD_BASE_URL = os.getenv("RESET_PASSWORD_BASE_URL", "http://localhost:3000/reset-password")
    reset_link = f"{RESET_PASSWORD_BASE_URL}?token={token}"

    back_task.add_task(
        send_email,
        to_email=user.email,
        subject="Reset Your Password",
        template_name="reset_email.html",
        context={
            "name": user.username,
            "reset_link": reset_link
        }
    )
    return {"message": "Reset link sent"}

def reset_password(token: str, new_password: str, db: Session):
    payload = verify_token(token)
    
    if not payload:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or expired token")
    
    email = payload.get("sub")
    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.password = Hash.bcrypt(new_password)
    db.commit()
    return {"message": "Password updated successfully"}