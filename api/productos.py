from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from db.db import get_db
from core.security import get_current_user
from schemas.product_schema import ProductoCreate, ProductoOut, ProductoUpdate
from typing import List, Optional
from services.producto_service import crear_producto, obtener_producto_por_id, actualizar_producto, eliminar_producto, listar_productos_por_filtro

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=ProductoOut)
def crear_producto_endpoint(
    producto: ProductoCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return crear_producto(db, producto, current_user)


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

@router.delete("/{producto_id}")
def delete_producto(
    producto_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return eliminar_producto(db, producto_id, current_user)

@router.get("/", response_model=List[ProductoOut])
def get_productos(
    categoria_id: Optional[int] = Query(None),
    min_precio: Optional[float] = Query(None),
    max_precio: Optional[float] = Query(None),
    search: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    limit: int = Query(10, le=100),
    db: Session = Depends(get_db)
):
    return listar_productos_por_filtro(
        db,
        categoria_id,
        min_precio,
        max_precio,
        search,
        page,
        limit
    )