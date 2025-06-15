import requests

def test_clasificacion_urgente():
    payload = {"texto": "¡Emergencia médica urgente!"}
    response = requests.post("http://localhost:8000/clasificar", json=payload)
    assert response.status_code == 200
    assert response.json()["clasificacion"] == "Urgente"

def test_clasificacion_moderado():
    payload = {"texto": "Podríamos reunirnos esta semana para conversar."}
    response = requests.post("http://localhost:8000/clasificar", json=payload)
    assert response.status_code == 200
    assert response.json()["clasificacion"] == "Moderado"

def test_clasificacion_normal():
    payload = {"texto": "Saludos cordiales, feliz semana."}
    response = requests.post("http://localhost:8000/clasificar", json=payload)
    assert response.status_code == 200
    assert response.json()["clasificacion"] == "Normal"
