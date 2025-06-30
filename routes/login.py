from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.usuario import Usuario
from schemas.usuario import UsuarioBase, UsuarioResponse
from database import get_db

router = APIRouter()

@router.post("/v1/login/usuario", response_model=dict)
def login_usuario(data: UsuarioBase, db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.nombre == data.nombre, Usuario.clave == data.clave).first()
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    return {
        "message": "Inicio de sesión exitoso",
        "status": 200,
        "data": {
            "id_usuario": user.id_usuario,
            "nombre": user.nombre,
            "edad": user.edad
        }
    }
