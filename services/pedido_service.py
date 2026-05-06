from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.usuario import RolEnum
from models.carrito import Carrito
from models.carrito_item import CarritoItem
from models.producto import Producto
from models.pedido import Pedido, EstadoPedido
from models.pedido_item import PedidoItem
from models.pedido import EstadoPedido
from models.usuario import RolEnum

def crear_pedido(db: Session, user_id: int, direccion_envio: str):

    carrito = db.query(Carrito).filter(Carrito.usuario_id == user_id).first()

    if not carrito or not carrito.items:
        raise HTTPException(status_code=400, detail="El carrito está vacío")
    

    for item in carrito.items:
        producto = db.query(Producto).filter(Producto.id == item.producto_id).first()

        if not producto:
            raise HTTPException(status_code=404, detail=f"Producto {item.producto_id} no existe")
        
        if item.cantidad > producto.stock:
            raise HTTPException(
                status_code=400,
                detail=f"Stock insuficiente para producto {producto.nombre}"
            )
    
        total = 0
    for item in carrito.items:
        total += item.cantidad * float(item.precio_unitario)

    pedido = Pedido(
        usuario_id=user_id,
        estado=EstadoPedido.PENDIENTE,
        total=total,
        direccion_envio=direccion_envio
    )

    db.add(pedido)
    db.commit()
    db.refresh(pedido)

    for item in carrito.items:
        pedido_item = PedidoItem(
            pedido_id=pedido.id,
            producto_id=item.producto_id,
            cantidad=item.cantidad,
            precio=item.precio_unitario  # precio congelado
        )
        db.add(pedido_item)

    for item in carrito.items:
        producto = db.query(Producto).filter(Producto.id == item.producto_id).first()
        producto.stock -= item.cantidad

    db.query(CarritoItem).filter(CarritoItem.carrito_id == carrito.id).delete()

    db.commit()

    return pedido

def obtener_pedidos_usuario(db: Session, user_id: int):
    pedidos = (
        db.query(Pedido)
        .filter(Pedido.usuario_id == user_id)
        .order_by(Pedido.id.desc())
        .all()
    )

    return pedidos

def obtener_pedido(db: Session, pedido_id: int, user):
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()

    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

    if pedido.usuario_id != user.id and user.rol != RolEnum.ADMIN:
        raise HTTPException(status_code=403, detail="No tienes permiso")

    return pedido

from models.pedido import EstadoPedido
from models.usuario import RolEnum


def cancelar_pedido(db: Session, pedido_id: int, user):
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()

    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

    if pedido.usuario_id != user.id and user.rol != RolEnum.ADMIN:
        raise HTTPException(status_code=403, detail="No tienes permiso")

    if pedido.estado != EstadoPedido.PENDIENTE:
        raise HTTPException(
            status_code=400,
            detail="Solo se pueden cancelar pedidos pendientes"
        )

    pedido.estado = EstadoPedido.CANCELADO

    db.commit()
    db.refresh(pedido)

    return pedido


