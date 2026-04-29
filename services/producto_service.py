from fastapi import HTTPException
from models.usuario import RolEnum
from models.producto import Producto
from sqlalchemy.orm import Session

def crear_producto(db, producto_data, current_user):

    print(f"ROL DEL USUARIO: {current_user.rol}")
    print(f"TIPO: {type(current_user.rol)}")
    print(f"COMPARACION: {current_user.rol == RolEnum.PROVEEDOR}")

    if current_user.rol != RolEnum.PROVEEDOR:
        raise HTTPException(
            status_code=403,
            detail="Solo proveedores pueden crear productos"
        )

    nuevo = Producto(
        nombre=producto_data.nombre,
        descripcion=producto_data.descripcion,
        precio=producto_data.precio,
        imagen=producto_data.imagen,
        stock=producto_data.stock,
        categoria_id=producto_data.categoria_id,
        proveedor_id=current_user.id
    )

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    return nuevo


def obtener_productos(db: Session):
    return db.query(Producto).all()


def obtener_producto_por_id(db: Session, producto_id: int):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    return producto


def actualizar_producto(db, producto_id, producto_data, current_user):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    if current_user.rol != RolEnum.ADMIN and producto.proveedor_id != current_user.id:
        raise HTTPException(status_code=403, detail="No tienes permiso")
    
    for key, value in producto_data.dict(exclude_unset=True).items():
        setattr(producto, key, value)

    db.commit()
    db.refresh(producto)

    return producto

def eliminar_producto(db, producto_id, current_user):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    if current_user.rol != RolEnum.ADMIN and producto.proveedor_id != current_user.id:
        raise HTTPException(status_code=403, detail="No tienes permiso")
    
    db.delete(producto)
    db.commit()

    return{"message": "Producto eliminado correctamente"}