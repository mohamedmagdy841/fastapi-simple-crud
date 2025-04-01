from datetime import datetime, timedelta, timezone
import jwt
from jwt import PyJWTError
import os
from dotenv import load_dotenv

load_dotenv()  # Automatically finds .env in the project

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM      = "HS256"
EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except PyJWTError:
        return None