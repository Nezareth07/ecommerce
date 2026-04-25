from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.db import get_db
from core.security import get_current_user
from schemas.product_schema import ProductoCreate, ProductoOut
from services.producto_service import crear_producto

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=ProductoOut)
def crear_producto_endpoint(
    producto: ProductoCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return crear_producto(db, producto, current_user)

