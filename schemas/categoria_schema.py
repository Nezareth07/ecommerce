from pydantic import BaseModel, ConfigDict

class CategoriaCreate(BaseModel):
    nombre: str

class CategoriaOut(BaseModel):
    id: int
    nombre: str

    model_config = ConfigDict(from_attributes=True)