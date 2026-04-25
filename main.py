from fastapi import FastAPI
from db.db import engine, Base
from sqlalchemy import text
from api.auth import router as auth_router
from api.productos import router as productos_router
from api.categorias import router as categorias_router



app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(productos_router)
app.include_router(categorias_router)

@app.get("/")
def root():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 5"))

    data = result.scalar()
    return {"result": data}