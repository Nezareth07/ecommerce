from sqlalchemy.orm import Session
from models.usuario import Usuario
from schemas.usuario_schema import UserCreate
from passlib.context import CryptContext
import os
from dotenv import load_dotenv
from jose import jwt
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

def crear_usuario(db: Session, user_data: UserCreate):
    hashed_password = pwd_context.hash(user_data.password)

    nuevo_usuario = Usuario(
        nombre=user_data.nombre,
        email=user_data.email,
        password=hashed_password,
        telefono=user_data.telefono,
        rol=user_data.rol
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return nuevo_usuario


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=30)

    to_encode.update({"exp": expire})
    
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_user_by_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()
