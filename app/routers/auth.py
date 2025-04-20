from fastapi import APIRouter, Depends, BackgroundTasks
from pydantic import EmailStr
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.db.database import get_db
from app.crud import auth
from app.schemas.user import UserBase, UserResponse
from app.services.send_email import send_email

router = APIRouter(tags=["auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@router.post("/register", response_model=UserResponse)
def register(request: UserBase, back_task: BackgroundTasks, db: Session = Depends(get_db)):
    return auth.register(db, back_task, request)

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    return auth.login(form_data, db)

@router.get("/current-user", response_model=UserResponse)
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    return auth.get_current_user(token, db)

@router.post("/forgot-password")
def forgot_password(email: EmailStr, back_task: BackgroundTasks, db: Session = Depends(get_db)):
    return auth.forgot_password(email, back_task, db)

@router.post("/reset-password")
def reset_password(token: str, new_password: str, db: Session = Depends(get_db)):
    return auth.reset_password(token, new_password, db)