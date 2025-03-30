from fastapi import FastAPI
from database import models
from database.database import engine
from routers import articles, users

app = FastAPI()
app.include_router(users.router)
app.include_router(articles.router)

@app.get('/')
def index():
    return {"message": f"Hello"}

models.Base.metadata.create_all(engine)