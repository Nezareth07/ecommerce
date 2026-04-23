from pydantic import BaseModel, ConfigDict, EmailStr, Field
from models.usuario import RolEnum


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserCreate(BaseModel):
    nombre: str
    email: EmailStr 
    password: str = Field(min_length=6, max_length=72)
    telefono: str
    rol: RolEnum


class UserOut(BaseModel):
    id: int
    nombre: str
    email: EmailStr
    telefono: str
    rol: RolEnum

    model_config = ConfigDict(from_attributes=True)
    

class Token(BaseModel):
    access_token: str
    token_type: str