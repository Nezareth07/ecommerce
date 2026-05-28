import stripe
from fastapi import HTTPException

from core.stripe_config import stripe
from models.pedido import Pedido

def crear_checkout_session(pedido):

    try:

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],

            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": f"Pedido #{pedido.id}" 
                        },
                        "unit_amount": int(
                            float(pedido.total) * 100
                        )
                    },
                    "quantity": 1
                }
            ],

            mode="payment",

            success_url="http://localhost:3000/success",

            cancel_url= "http://localhost:3000/cancel",

            metadata={
                "pedido_id": pedido.id
            }

        )
        
        return {
            "checkout_url": session.url
        }
    
    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
