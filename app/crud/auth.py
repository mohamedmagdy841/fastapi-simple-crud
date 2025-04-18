from schemas import UserBase
from sqlalchemy.orm.session import Session
from utils.hash import Hash
from models import User
from fastapi.security import OAuth2PasswordRequestForm
from utils.token import create_access_token, verify_token
from fastapi import HTTPException, status

def register(db: Session, request: UserBase):
    new_user = User(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
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