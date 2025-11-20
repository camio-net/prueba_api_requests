import requests


headers = {"x-api-key": "reqres-free-v1"}

url = "https://reqres.in/api/users"


data = {
    "name": "damian",
    "job": "vendor"
}

response = requests.post(url, headers=headers, json=data)

print("Response Status Code:", response.status_code)
print("Response Body:", response.json())
