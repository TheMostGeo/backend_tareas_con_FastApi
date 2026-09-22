from pydantic import BaseModel, Field


class CrearTarea(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=20)
    dias: int = Field(..., gt=0)
    fecha_ini: str = Field(..., min_length=1, max_length=20)
    fecha_fin: str | None = None


class Tarea(CrearTarea):
    id: int




