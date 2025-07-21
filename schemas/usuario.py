from pydantic import BaseModel
from typing import Optional


class UsuarioBase(BaseModel):
    nombre: str
    clave: str

class UsuarioResponse(BaseModel):
    id_usuario: int
    nombre: str
    edad: int

    class Config:
        from_attributes = True

class UsuarioRegister(BaseModel):
    nombre: str
    clave: str
    edad: int
    apellido: Optional[str] = "Paucar"  # solo si decides manejarlo