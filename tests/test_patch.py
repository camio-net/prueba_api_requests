import requests

def test_patch_users():
    headers = {"x-api-key": "reqres-free-v1"}

    url = "https://reqres.in/api/users/page=2"

    data = {
        "name": "marcelo",
        
    }

    response = requests.patch(url,headers=headers,json=data)

    #Validacion status code
    assert response.status_code == 200

    #Validacion de datos 
    body = response.json()

    assert body["name"] == data ["name"]
    
