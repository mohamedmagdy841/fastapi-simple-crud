from fastapi import Depends, APIRouter
from database import crud
from schemas import ArticleBase, ArticleResponse
from sqlalchemy.orm.session import Session
from database.database import get_db

router = APIRouter(prefix="/articles", tags=['articles'])

@router.get('/{user_id}', response_model=list[ArticleResponse])
def get_article(user_id: int, db: Session = Depends(get_db)):
    return crud.get_article(db, user_id)

@router.post('/', response_model=ArticleResponse)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return crud.create_article(db, request)