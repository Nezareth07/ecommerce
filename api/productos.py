from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.db import get_db
from core.security import get_current_user
from schemas.product_schema import ProductoCreate, ProductoOut, ProductoUpdate
from services.producto_service import crear_producto
from typing import List
from services.producto_service import obtener_productos, obtener_producto_por_id, actualizar_producto

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=ProductoOut)
def crear_producto_endpoint(
    producto: ProductoCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return crear_producto(db, producto, current_user)

@router.get("/", response_model=List[ProductoOut])
def listar_productos(db: Session = Depends(get_db)):
    return obtener_productos(db)

@router.get("/{producto_id}", response_model=ProductoOut)
def get_producto(
    producto_id: int,
    db: Session = Depends(get_db)
):
    return obtener_producto_por_id(db, producto_id)

@router.put("/{producto_id}", response_model=ProductoOut)
def update_producto(
    producto_id: int,
    producto: ProductoUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return actualizar_producto(db, producto_id, producto, current_user)
