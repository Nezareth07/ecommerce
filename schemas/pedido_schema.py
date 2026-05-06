from pydantic import BaseModel, ConfigDict
from typing import List

class PedidoCreate(BaseModel):
    direccion_envio: str

class PedidoItemOut(BaseModel):
    producto_id: int
    cantidad: int
    precio: float
    model_config = ConfigDict(from_attributes=True)

class PedidoOut(BaseModel):
    id: int
    usuario_id: int
    total: float
    estado: str
    direccion_envio: str
    items: List[PedidoItemOut]

    model_config = ConfigDict(from_attributes=True)