from fastapi import APIRouter, Depends, Query, status, HTTPException
from sqlalchemy.orm import Session

from Services.schemas.tarea_schema import CrearTarea, Tarea
from Services.tarea_service import crear_nueva_tarea, obtener_lista_tareas
from database.connection import get_db


router = APIRouter(prefix="/tareas", tags=["Tareas"])


@router.get("", response_model=list[Tarea])
def obtener_tareas(
	skip: int = Query(0, ge=0),
	limit: int = Query(10, ge=1, le=100),
	db: Session = Depends(get_db),
):
	return obtener_lista_tareas(db, skip, limit)


@router.post("", response_model=Tarea, status_code=status.HTTP_201_CREATED)
def crear_tarea(tarea: CrearTarea, db: Session = Depends(get_db)):
	return crear_nueva_tarea(db, tarea)
