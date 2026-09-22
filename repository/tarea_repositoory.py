from sqlalchemy import select
from sqlalchemy.orm import Session

from Services.schemas.tarea_schema import CrearTarea
from database.models import TareaModel


def obtener_tareas(db: Session, skip: int = 0, limit: int = 10) -> list[TareaModel]:
	consulta = select(TareaModel).offset(skip).limit(limit)
	return list(db.scalars(consulta).all())


def crear_tarea(db: Session, tarea: CrearTarea) -> TareaModel:
	nueva_tarea = TareaModel(**tarea.model_dump())
	db.add(nueva_tarea)
	db.commit()
	db.refresh(nueva_tarea)
	return nueva_tarea
