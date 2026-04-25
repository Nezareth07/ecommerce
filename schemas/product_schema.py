from pydantic import BaseModel, ConfigDict
from decimal import Decimal
from typing import Optional


class ProductoCreate(BaseModel):
    nombre: str
    descripcion: str
    precio: Decimal
    imagen: str
    stock: int
    categoria_id: int

class ProductoOut(BaseModel):
    id: int
    nombre: str
    descripcion: str
    precio: Decimal
    imagen: str
    stock: int
    categoria_id: int
    proveedor_id: int

    model_config = ConfigDict(from_attributes=True)

class ProductoUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio: Optional[Decimal] = None
    imagen: Optional[str] = None
    stock: Optional[int] = None
    categoria_id: Optional[int] = None
