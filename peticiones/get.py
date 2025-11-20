import requests


headers = {"x-api-key": "reqres-free-v1"}

url = "https://reqres.in/api/users?page=2"
response = requests.get(url,headers=headers)

print("Response Status Code:", response.status_code)
print("Response Body:", response.json())
