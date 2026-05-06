from sqlalchemy import Column, Integer, ForeignKey, DateTime, Numeric, String, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from db.db import Base
import enum


class EstadoPedido(str, enum.Enum):
    PENDIENTE = "pendiente"
    PAGADO = "pagado"
    ENVIADO = "enviado"
    CANCELADO = "cancelado"


class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)

    usuario_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    estado = Column(Enum(EstadoPedido), default=EstadoPedido.PENDIENTE, nullable=False)

    total = Column(Numeric(10, 2), nullable=False)

    direccion_envio = Column(String(255), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    usuario = relationship("Usuario", back_populates="pedidos")
    items = relationship("PedidoItem", back_populates="pedido", cascade="all, delete-orphan")