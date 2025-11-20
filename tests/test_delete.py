import requests

def test_delete_users(url_base):
    headers = {"x-api-key": "reqres-free-v1"}

    url = f"{url_base}/page/2"

    response = requests.delete(url,headers=headers)

    assert response.status_code == 204