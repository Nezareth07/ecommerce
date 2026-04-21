from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import relationship
from db.db import Base

class Categoria(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(256), nullable=False)

    productos = relationship("Producto", back_populates="categoria")