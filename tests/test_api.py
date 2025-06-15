import requests

def test_clasificacion_urgente():
    payload = {"texto": "¡Emergencia médica urgente!"}
    response = requests.post("http://localhost:8000/clasificar", json=payload)
    print("Probando texto URGENTE:", payload["texto"])
    print("Respuesta:", response.json())
    assert response.status_code == 200
    assert response.json()["clasificacion"] == "Urgente"

def test_clasificacion_normal():
    payload = {"texto": "Saludos cordiales, feliz semana."}
    response = requests.post("http://localhost:8000/clasificar", json=payload)
    print("Probando texto NORMAL:", payload["texto"])
    print("Respuesta:", response.json())
    assert response.status_code == 200
    assert response.json()["clasificacion"] == "Normal"
