from fastapi import APIRouter, File, UploadFile, Request, HTTPException, status
from fastapi.responses import FileResponse
import shutil
import hashlib
import time
from pathlib import Path

router = APIRouter(prefix='/files', tags=["files"])

UPLOAD_DIR = Path("storage/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def generate_unique_image(filename: str) -> str:
    ext = filename.split(".")[-1]
    timestamp = str(int(time.time()))
    hash_part = hashlib.sha256(filename.encode()).hexdigest()[:10]
    return f"{hash_part}_{timestamp}.{ext}"

@router.post("/upload")
def upload_file(request: Request, file: UploadFile = File(...)):
    new_filename = generate_unique_image(file.filename)
    path = UPLOAD_DIR / new_filename

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    base_url = str(request.base_url)

    return {"filename": new_filename, "url": f"{base_url}files/{new_filename}"}

@router.get("/download/{filename}", response_class=FileResponse)
def get_file(filename: str):
    path = UPLOAD_DIR / filename
    if not path.exists():
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="File not found")
    return path

