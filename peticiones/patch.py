import requests

headers = {"x-api-key": "reqres-free-v1"}

url = "https://reqres.in/api/users/page=2"

data = {
    "name": "marcelo",
    
}

response = requests.patch(url,headers=headers,json=data)

print(response.status_code)
print(response.json())