import requests

headers = {"x-api-key": "reqres-free-v1"}

url = "https://reqres.in/api/users/page=2"

data = {
    "name": "ezequiel",
    "job": "administrador"
}

response = requests.put(url,headers=headers,json=data)

print(response.status_code)
print(response.json())