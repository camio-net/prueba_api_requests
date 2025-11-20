import requests


headers = {"x-api-key": "reqres-free-v1"}

url = "https://reqres.in/api/users/page/2"

response = requests.delete(url,headers=headers)

print(response.status_code)
print(response.text)