from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from database import crud
from database.database import get_db
from schemas import UserBase, UserResponse

router = APIRouter(prefix='/users', tags=['users'])

@router.post('/', response_model=UserResponse)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return crud.create_user(db, request)

@router.get('/', response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return crud.get_all_users(db)

@router.get('/{id}', response_model=UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, id)

@router.put('/{id}/update')
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    return crud.update_user(db, request, id)

@router.delete('/delete/{id}')
def update_user(id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, id)