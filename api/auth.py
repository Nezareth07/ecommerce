from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import get_db
from schemas.usuario_schema import UserCreate, UserOut, UserLogin, Token
from services.auth_service import crear_usuario, get_user_by_email, create_access_token
from passlib.context import CryptContext

router = APIRouter(prefix="/auth", tags=["auth"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return crear_usuario(db, user)

@router.post("/login", response_model=Token)
def login(user:UserLogin, db: Session = Depends(get_db)):

    db_user = get_user_by_email(db, user.email)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    if not pwd_context.verify(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token({"sub": db_user.email})

    return{
        "access_token": token,
        "token_type": "bearer"
    }