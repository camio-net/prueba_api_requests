import requests

def test_patch_users(url_base,header_request):
    headers = header_request

    url = f"{url_base}/page=2"

    data = {
        "name": "marcelo"       
    }

    response = requests.patch(url,headers=headers,json=data)

    #Validacion status code
    assert response.status_code == 200

    #Validacion de datos 
    body = response.json()

    assert body["name"] == data ["name"]
    
