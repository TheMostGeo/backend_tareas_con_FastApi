from sqlalchemy import select
from sqlalchemy.orm import Session


from Services.schemas.usuario_schema import CrearUsuario
from database.models import UsuarioModel

def obtener_usuario(db: Session, skip: int = 0, limit: int = 10) -> list[UsuarioModel]:
	consulta = select(UsuarioModel).offset(skip).limit(limit)
	return list(db.scalars(consulta).all())








