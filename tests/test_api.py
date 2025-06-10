import requests


def test_clasificacion_responde_correctamente():
    payload = {"texto": "La reunión es el viernes a las 10h."}
    response = requests.post("http://localhost:8000/clasificar", json=payload)

    assert response.status_code == 200
    assert response.json()["clasificacion"] in ["Urgente", "Moderado", "Normal"]
