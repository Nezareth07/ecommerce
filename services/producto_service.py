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