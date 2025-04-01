from fastapi import FastAPI
from database.models import article
from database.database import engine
from routers import articles, users, auth

app = FastAPI()
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(articles.router)

@app.get('/')
def index():
    return {"message": f"Hello"}

article.Base.metadata.create_all(engine)