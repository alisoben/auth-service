from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.usuario import Usuario
from schemas.usuario import UsuarioRegister  # Usamos este esquema
from database import get_db

router = APIRouter()

@router.post("/v1/register/usuario", response_model=dict)
def register_usuario(data: UsuarioRegister, db: Session = Depends(get_db)):
    # Verificar si ya existe un usuario con ese nombre
    existing_user = db.query(Usuario).filter(Usuario.nombre == data.nombre).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    nuevo_usuario = Usuario(nombre=data.nombre, clave=data.clave, edad=data.edad, apellido=data.apellido)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return {
        "message": "Usuario registrado exitosamente",
        "status": 201,
        "data": {
            "id_usuario": nuevo_usuario.id_usuario,
            "nombre": nuevo_usuario.nombre,
            "edad": nuevo_usuario.edad
        }
    }
