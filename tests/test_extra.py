import requests

def test_clasificacion_urgente():
    payload = {"texto": "¡Hay un incendio en el laboratorio!"}
    response = requests.post("http://localhost:8000/clasificar", json=payload)

    assert response.status_code == 200
    assert response.json()["clasificacion"] == "Urgente"

def test_clasificacion_moderado():
    payload = {"texto": "Revisar por qué no llegan los correos."}
    response = requests.post("http://localhost:8000/clasificar", json=payload)

    assert response.status_code == 200
    assert response.json()["clasificacion"] == "Moderado"

def test_clasificacion_normal():
    payload = {"texto": "La reunión se mantiene el viernes."}
    response = requests.post("http://localhost:8000/clasificar", json=payload)

    assert response.status_code == 200
    assert response.json()["clasificacion"] == "Normal"

def test_mensaje_vacio():
    payload = {"texto": ""}
    response = requests.post("http://localhost:8000/clasificar", json=payload)

    assert response.status_code == 200
    assert response.json()["clasificacion"] in ["Urgente", "Moderado", "Normal"]
