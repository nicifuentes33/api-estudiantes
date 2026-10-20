
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="API de Estudiantes",
    description="API REST para gestionar estudiantes",
    version="1.0.0"
)

estudiantes = []
ultimo_id = 0


class Estudiante(BaseModel):
    nombre: str
    apellido: str
    correo: str
    programa: str


@app.get("/")
def inicio():
    return {
        "mensaje": "API de Estudiantes funcionando correctamente",
        "version": "1.0.0"
    }


@app.post("/students", status_code=201)
def crear_estudiante(estudiante: Estudiante):
    global ultimo_id

    ultimo_id += 1

    nuevo_estudiante = {
        "id": ultimo_id,
        "nombre": estudiante.nombre,
        "apellido": estudiante.apellido,
        "correo": estudiante.correo,
        "programa": estudiante.programa
    }

    estudiantes.append(nuevo_estudiante)

    return nuevo_estudiante


@app.get("/students")
def listar_estudiantes():
    return estudiantes


@app.get("/students/{id}")
def obtener_estudiante(id: int):
    for estudiante in estudiantes:
        if estudiante["id"] == id:
            return estudiante

    raise HTTPException(
        status_code=404,
        detail="Estudiante no encontrado"
    )
