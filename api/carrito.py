from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import get_db
from core.security import get_current_user
from models.usuario import RolEnum
from services.carrito_service import agregar_producto, ver_carrito, actualizar_cantidad, eliminar_item
from pydantic import BaseModel

router = APIRouter(prefix="/carrito", tags=["carrito"])


class AgregarItem(BaseModel):
    producto_id: int
    cantidad: int


class ActualizarCantidad(BaseModel):
    cantidad: int


def solo_cliente(current_user):
    if current_user.rol != RolEnum.CLIENTE:
        raise HTTPException(status_code=403, detail="Solo clientes pueden usar el carrito")


@router.post("/add")
def add_item(item: AgregarItem, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    solo_cliente(current_user)
    return agregar_producto(db, current_user.id, item.producto_id, item.cantidad)


@router.get("/")
def get_carrito(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    solo_cliente(current_user)
    return ver_carrito(db, current_user.id)


@router.put("/{item_id}")
def update_item(item_id: int, data: ActualizarCantidad, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    solo_cliente(current_user)
    return actualizar_cantidad(db, current_user.id, item_id, data.cantidad)


@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    solo_cliente(current_user)
    return eliminar_item(db, current_user.id, item_id)