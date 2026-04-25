from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.db import get_db
from schemas.categoria_schema import CategoriaCreate, CategoriaOut
from services.categoria_service import crear_categoria, listar_categorias

router = APIRouter(prefix="/categories", tags=["categories"])


@router.post("/", response_model=CategoriaOut)
def crear_categoria_endpoint(
    categoria: CategoriaCreate,
    db: Session = Depends(get_db)
):
    return crear_categoria(db, categoria)


@router.get("/", response_model=list[CategoriaOut])
def listar_categorias_endpoint(
    db: Session = Depends(get_db)
):
    return listar_categorias(db)