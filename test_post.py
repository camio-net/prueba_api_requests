import requests

def test_post_users():
    url = "https://reqres.in/api/users"
    headers = {"x-api-key": "reqres-free-v1"}   

    payload =  {
    "name": "damian",
    "job": "vendor"
    }

    response = requests.post(url, headers=headers, json=payload)

    #verificaion json creado
    assert response.status_code == 201

    #Verificacion del contenido del json
    data = response.json()
    #Validacion que el nombre y trabajo son correctos
    assert data["name"] == payload["name"]
    assert data["job"] == payload["job"]

    #Validacion que el id y createdAt estan presentes
    assert "id" in data