from pydantic import BaseModel, Field

class CrearUsuario(BaseModel): 
    User_name: str = Field(..., min_length=3, max_length=20)
    id_tarea: int = Field(..., gt=0)

class Usuario(CrearUsuario):
    id_user: int




