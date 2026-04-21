from sqlalchemy import Column, DateTime, Text, Numeric, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime
from db.db import Base

class Producto(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(Text, nullable=False)
    precio = Column(Numeric(10, 2), nullable=False)
    imagen = Column(String(500), nullable=False)
    stock = Column(Integer, nullable=False)
    activo = Column(Boolean, default=True, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    categoria_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    proveedor_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    categoria = relationship("Categoria", back_populates="productos")
    proveedor = relationship("Usuario", back_populates="productos")

    