from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from db.db import get_db
from core.security import get_current_user
from services.pedido_service import crear_pedido, obtener_pedidos_usuario, obtener_pedido, cancelar_pedido
from schemas.pedido_schema import PedidoCreate, PedidoOut

router = APIRouter(prefix="/pedidos", tags=["pedidos"])


@router.post("/", response_model=PedidoOut)
def crear_pedido_endpoint(
    data: PedidoCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return crear_pedido(db, user.id, data.direccion_envio)

@router.get("/", response_model=List[PedidoOut])
def listar_pedidos(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return obtener_pedidos_usuario(db, user.id)

@router.get("/{pedido_id}", response_model=PedidoOut)
def obtener_pedido_endpoint(
    pedido_id: int,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return obtener_pedido(db, pedido_id, user)

@router.put("/{pedido_id}/cancel", response_model=PedidoOut)
def cancelar_pedido_endpoint(
    pedido_id: int,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return cancelar_pedido(db, pedido_id, user)