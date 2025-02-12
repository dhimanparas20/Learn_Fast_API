from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError
from database import get_db
from models import User
from schemas import UserCreate, TokenData
from config import settings

router = APIRouter(prefix="/auth", tags=["Authentication"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

@router.post("/register", response_model=TokenData)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    user.password = hash_password(user.password)
    new_user = User(username=user.username, email=user.email, hashed_password=user.password)
    db.add(new_user)
    await db.commit()
    return {"access_token": create_access_token({"sub": new_user.username}), "token_type": "bearer"}

@router.post("/login", response_model=TokenData)
async def login(user: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await db.execute("SELECT * FROM users WHERE username=:username", {"username": user.username})
    db_user = db_user.fetchone()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"access_token": create_access_token({"sub": db_user.username}), "token_type": "bearer"}
