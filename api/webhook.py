from fastapi import APIRouter, Request, HTTPException
import stripe
import os

from db.db import SessionLocal
from models.pedido import Pedido, EstadoPedido

router = APIRouter(
    prefix="/webhook",
    tags=["Webhook"]
)

@router.post("/stripe")
async def stripe_webhook(request: Request):

    payload = await request.body()

    try:

        event = stripe.Event.construct_from(
            await request.json(),
            stripe.api_key
        )

    except Exception as e:

        raise HTTPException(

            status_code=400,
            detail=str(e)
        )
    
    if event["type"] == "checkout.session.completed":

        session = event["data"]["object"]

        pedido_id = session["metadata"]["pedido_id"]

        db = SessionLocal()

        pedido = db.query(Pedido).filter(
            Pedido.id == int(pedido_id)
        ).first()

        if pedido:

            pedido.estado = EstadoPedido.PAGADO

            db.commit()
        
        db.close()

    return {"status":"succes"}