from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.db import get_db
from schemas.usuario_schema import UserCreate, UserOut
from services.auth_service import crear_usuario

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return crear_usuario(db, user)