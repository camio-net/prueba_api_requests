import pytest
import requests

def test_get_users():
    url = "https://reqres.in/api/users?page=2"
    headers = {"x-api-key": "reqres-free-v1"}   

    response = requests.get(url, headers=headers)        

    #Validadcion status code
    assert response.status_code == 200


    