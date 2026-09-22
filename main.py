from fastapi import FastAPI

from Routers.tareas_router import router as tareas_router
from database import models  # noqa: F401: registra los modelos antes de crear tablas
from database.base import Base
from database.connection import engine


Base.metadata.create_all(bind=engine)

app = FastAPI(
	title="Mi API con FastAPI",
	description="API de tareas",
	version="1.0.0",
)

app.include_router(tareas_router)
