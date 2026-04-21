from sqlalchemy.orm import Session
from models.usuario import Usuario
from schemas.usuario_schema import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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