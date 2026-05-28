from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.db import get_db
from models.pedido import Pedido
from services.payment_service import crear_checkout_session

router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)

@router.post("/{pedido_id}")
def pagar_pedido(
    pedido_id: int,
    db: Session = Depends(get_db)
):
    
    pedido = db.query(Pedido).filter(
        Pedido.id == pedido_id
    ).first()

    if not pedido:
        return {"error": "Pedido no encontrado"}
    
    return crear_checkout_session(pedido)