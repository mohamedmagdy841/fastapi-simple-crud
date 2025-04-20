from fastapi import Depends, APIRouter
from app.crud import article
from app.schemas.article import ArticleResponse, ArticleCreate, ArticleUpdate
from sqlalchemy.orm.session import Session
from app.db.database import get_db
from app.routers.auth import get_current_user
from app.utils.ApiResponse import ApiResponse

router = APIRouter(prefix="/articles", tags=['articles'])

@router.get('/', response_model=ApiResponse[list[ArticleResponse]])
def get_all_articles(db: Session = Depends(get_db)):
    return ApiResponse(data=article.get_all_articles(db))

@router.get('/{id}', response_model=ApiResponse[ArticleResponse])
def get_article(id: int, db: Session = Depends(get_db)):
    return ApiResponse(data=article.get_article(db, id))

@router.post('/', response_model=ApiResponse[ArticleResponse])
def create_article(request: ArticleCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return ApiResponse(data=article.create_article(db, request, user.id))

@router.put('/{id}/update', response_model=ApiResponse[ArticleResponse])
def update_article(id: int, request: ArticleUpdate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return ApiResponse(data=article.update_article(db, request, id, user.id))

@router.delete('/{id}')
def delete_article(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return article.delete_article(id, db, user.id)