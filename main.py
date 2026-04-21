from fastapi import FastAPI
from db.db import engine, Base
from sqlalchemy import text
from api.auth import router as auth_router


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)

@app.get("/")
def root():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 5"))

    data = result.scalar()
    return {"result": data}