from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.carrito import Carrito
from models.carrito_item import CarritoItem
from models.producto import Producto

def obtener_carrito(db: Session, user_id: int):
    carrito = db.query(Carrito).filter(Carrito.usuario_id == user_id).first()

    if not carrito:
        carrito = Carrito(usuario_id=user_id)
        db.add(carrito)
        db.commit()
        db.refresh(carrito)

    return carrito

def agregar_producto(db: Session, user_id: int, producto_id: int, cantidad: int):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    carrito = obtener_carrito(db, user_id)

    item = db.query(CarritoItem).filter(
        CarritoItem.carrito_id == carrito.id,
        CarritoItem.producto_id == producto_id
    ).first()

    if item:
        item.cantidad += cantidad
    else: item = CarritoItem(
        carrito_id=carrito.id,
        producto_id=producto_id,
        cantidad=cantidad,
        precio_unitario=producto.precio
    )
    db.add(item)

    db.commit()
    db.refresh(item)

def actualizar_cantidad(db: Session, user_id: int, item_id: int, cantidad: int):
    carrito = obtener_carrito(db, user_id)

    item = db.query(CarritoItem).filter(
        CarritoItem.id == item_id,
        CarritoItem.carrito_id == carrito.id
    ).first()

    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")

    if cantidad <= 0:
        db.delete(item)
    else:
        item.cantidad = cantidad

    db.commit()

    return {"msg": "Cantidad actualizada"}

def eliminar_item(db: Session, user_id: int, item_id: int):
    carrito = obtener_carrito(db, user_id)

    item = db.query(CarritoItem).filter(
        CarritoItem.id == item_id,
        CarritoItem.carrito_id == carrito.id
    ).first()

    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")

    db.delete(item)
    db.commit()

    return {"msg": "Producto eliminado del carrito"}

def ver_carrito(db: Session, user_id: int):
    carrito = obtener_carrito(db, user_id)

    items = []
    total = 0

    for item in carrito.items:
        subtotal = item.cantidad * float(item.precio_unitario)
        total += subtotal

        items.append({
            "item_id": item.id,
            "producto_id": item.producto_id,
            "cantidad": item.cantidad,
            "precio_unitario": float(item.precio_unitario),
            "subtotal": subtotal
        })

    return {
        "carrito_id": carrito.id,
        "items": items,
        "total": total
    }
