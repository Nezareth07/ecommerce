from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.db import get_db
from core.security import get_current_user
from services.carrito_service import *

router = APIRouter(prefix="/carrito", tags=["carrito"])


@router.get("/")
def get_carrito(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return ver_carrito(db, user.id)


@router.post("/add")
def add_producto(producto_id: int, cantidad: int,
                 db: Session = Depends(get_db),
                 user=Depends(get_current_user)):
    return agregar_producto(db, user.id, producto_id, cantidad)


@router.put("/item/{item_id}")
def update_item(item_id: int, cantidad: int,
                db: Session = Depends(get_db),
                user=Depends(get_current_user)):
    return actualizar_cantidad(db, user.id, item_id, cantidad)


@router.delete("/item/{item_id}")
def delete_item(item_id: int,
                db: Session = Depends(get_db),
                user=Depends(get_current_user)):
    return eliminar_item(db, user.id, item_id)