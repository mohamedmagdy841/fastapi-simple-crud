from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from app.crud import user as user_crud
from app.db.database import get_db
from app.schemas.user import UserBase, UserResponse
from app.utils.ApiResponse import ApiResponse
from app.routers.auth import get_current_user

router = APIRouter(prefix='/users', tags=['users'])


@router.get('/', response_model=ApiResponse[list[UserResponse]])
def get_all_users(db: Session = Depends(get_db)):
    return ApiResponse(data=user_crud.get_all_users(db))

@router.get('/{id}', response_model=ApiResponse[UserResponse])
def get_user(id: int, db: Session = Depends(get_db)):
    return ApiResponse(data=user_crud.get_user(db, id))

@router.put('/{id}/update', response_model=ApiResponse[UserResponse])
def update_user(id: int, request: UserBase, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return ApiResponse(data=user_crud.update_user(db, request, id, user.id))

@router.delete('/delete/{id}')
def update_user(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return user_crud.delete_user(db, id, user.id)