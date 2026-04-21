from sqlalchemy import Column, DateTime, Enum
from sqlalchemy.sql.sqltypes import Integer, String
from datetime import datetime
from sqlalchemy.orm import relationship
from db.db import Base
from enum import Enum as PyEnum

class RolEnum(PyEnum):
    ADMIN = "admin"
    PROVEEDOR = "proveedor"
    CLIENTE = "cliente"


class Usuario(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True, index=True)
    password = Column(String(255), nullable=False)
    telefono = Column(String(255), nullable=False)

    rol = Column(Enum(RolEnum), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    productos = relationship("Producto", back_populates="proveedor")