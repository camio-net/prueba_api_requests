import requests
import pytest

@pytest.mark.api
def test_get_users(url_base,header_request):
    url = f"{url_base}/2"
    
    headers = header_request

    response = requests.get(url, headers=headers)        

    #Validadcion status code
    assert response.status_code == 200

    data = response.json()
    #Validar data presente
    assert "data" in data

    

    #Validar al menos 1 usuario
    assert len(data["data"]) > 0


    