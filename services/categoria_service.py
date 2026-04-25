from models.categoria import Categoria

def crear_categoria(db, categoria_data):
    nueva = Categoria(nombre=categoria_data.nombre)

    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    return nueva


def listar_categorias(db):
    return db.query(Categoria).all()