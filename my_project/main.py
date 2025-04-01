from pathlib import Path
from fastapi import FastAPI
from database.models import article
from database.database import engine
from routers import articles, users, auth, file
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(auth.router)
app.include_router(file.router)
app.include_router(users.router)
app.include_router(articles.router)

@app.get('/')
def index():
    return {"message": f"Hello"}

article.Base.metadata.create_all(engine)

app.mount("/storage/uploads", StaticFiles(directory=str(Path("storage") / "uploads")), name="uploads")
