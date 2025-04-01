from fastapi import Depends, APIRouter
from crud import article
from schemas import ArticleBase, ArticleResponse
from sqlalchemy.orm.session import Session
from database.database import get_db
from routers.auth import get_current_user

router = APIRouter(prefix="/articles", tags=['articles'])

@router.get('/{id}', response_model=ArticleResponse)
def get_article(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return article.get_article(db, id)

@router.post('/', response_model=ArticleResponse)
def create_article(request: ArticleBase, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return article.create_article(db, request)