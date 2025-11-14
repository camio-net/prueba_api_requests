import requests

def test_get_users():
    url = "https://reqres.in/api/users"
    headers = {"x-api-key": "reqres-free-v1"}   

    response = requests.get(url, headers=headers)        

    #Validadcion status code
    assert response.status_code == 200

    data = response.json()
    #Validar data presente
    assert "data" in data

    #Verificar ques es una listda "data"
    assert isinstance(data["data"], list)

    #Validar al menos 1 usuario
    assert len(data["data"]) > 0


    