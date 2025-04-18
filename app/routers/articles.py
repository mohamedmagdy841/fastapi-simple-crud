from fastapi import Depends, APIRouter
from crud import article
from schemas import ArticleBase, ArticleResponse
from sqlalchemy.orm.session import Session
from db.database import get_db
from routers.auth import get_current_user
from utils.ApiResponse import ApiResponse

router = APIRouter(prefix="/articles", tags=['articles'])

@router.get('/{id}', response_model=ApiResponse[ArticleResponse])
def get_article(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return ApiResponse(data=article.get_article(db, id))

@router.post('/', response_model=ApiResponse[ArticleResponse])
def create_article(request: ArticleBase, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return ApiResponse(data=article.create_article(db, request))