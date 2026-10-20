
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_inicio():
    respuesta = client.get("/")
    assert respuesta.status_code == 200
    assert respuesta.json()["version"] == "1.0.0"


def test_crear_estudiante():
    respuesta = client.post(
        "/students",
        json={
            "nombre": "Ana",
            "apellido": "Perez",
            "correo": "ana@example.com",
            "programa": "Ingenieria de Sistemas"
        }
    )
    assert respuesta.status_code == 201
    assert respuesta.json()["nombre"] == "Ana"


def test_listar_estudiantes():
    respuesta = client.get("/students")
    assert respuesta.status_code == 200
    assert isinstance(respuesta.json(), list)


def test_estudiante_inexistente():
    respuesta = client.get("/students/999999")
    assert respuesta.status_code == 404
