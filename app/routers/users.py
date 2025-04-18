from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from crud import user
from db.database import get_db
from schemas import UserBase, UserResponse
from utils.ApiResponse import ApiResponse

router = APIRouter(prefix='/users', tags=['users'])


@router.get('/', response_model=ApiResponse[list[UserResponse]])
def get_all_users(db: Session = Depends(get_db)):
    return ApiResponse(data=user.get_all_users(db))

@router.get('/{id}', response_model=ApiResponse[UserResponse])
def get_user(id: int, db: Session = Depends(get_db)):
    return ApiResponse(data=user.get_user(db, id))

@router.put('/{id}/update')
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    return user.update_user(db, request, id)

@router.delete('/delete/{id}')
def update_user(id: int, db: Session = Depends(get_db)):
    return user.delete_user(db, id)