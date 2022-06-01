import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "helloworld/veto/39")
print(response.json())