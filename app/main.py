from pathlib import Path
from fastapi import FastAPI
from app.routers import articles, users, auth, file
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(auth.router)
app.include_router(file.router)
app.include_router(users.router)
app.include_router(articles.router)

@app.get("/", tags=["home"])
async def index():
    return {"message": "Welcome"}

app.mount("/storage/uploads", StaticFiles(directory=str(Path("storage") / "uploads")), name="uploads")


