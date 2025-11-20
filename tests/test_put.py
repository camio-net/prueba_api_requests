import requests
import time
import pytest

@pytest.mark.api
def test_put_users(url_base,header_request):
    #Variable de tiempo inicio
    inicio = time.time()
    
    headers = header_request

    url = f"{url_base}/page=2"

    data = {
    "name": "ezequiel",
    "job": "administrador"
    }

    response = requests.put(url,headers=headers,json=data)

    #Tiempo de respuesta de la peticion
    final = time.time() - inicio


    #Validadcion de status
    assert response.status_code == 200
    
    #Validacion tiempo de respuesta
    assert final < 2 , "La api tardo demaciado {final}"
    

    #Validacion de datos
    body = response.json()

    assert "updatedAt" in body
    assert  isinstance(body["name"],str)

    assert body["name"] == data["name"]
