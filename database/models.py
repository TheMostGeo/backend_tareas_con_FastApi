from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from database.base import Base


class TareaModel(Base):
	__tablename__ = "tareas"

	id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
	nombre: Mapped[str] = mapped_column(String(20), nullable=False)
	dias: Mapped[int] = mapped_column(Integer, nullable=False)
	fecha_ini: Mapped[str] = mapped_column(String(20), nullable=False)
	fecha_fin: Mapped[str | None] = mapped_column(String(20), nullable=True)


class UsuarioModel(Base):
	__tablename__ = "Usuarios"
	
	id_user: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
	User_name: Mapped[str] = mapped_column(String(20), nullable=False)
	id_tarea: Mapped[int] = mapped_column(Integer, ForeignKey("tareas.id"))
