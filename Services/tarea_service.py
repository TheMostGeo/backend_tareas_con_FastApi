from sqlalchemy.orm import Session

from Services.schemas.tarea_schema import CrearTarea
from database.models import TareaModel
from repository.tarea_repositoory import crear_tarea as guardar_tarea
from repository.tarea_repositoory import obtener_tareas as buscar_tareas


def obtener_lista_tareas(
	db: Session, skip: int = 0, limit: int = 10
) -> list[TareaModel]:
	return buscar_tareas(db, skip, limit)


def crear_nueva_tarea(db: Session, tarea: CrearTarea) -> TareaModel:
	return guardar_tarea(db, tarea)
