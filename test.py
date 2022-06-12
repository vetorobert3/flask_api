import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "quote/1", {"author": "Buddha", "quote": "live and let die"})
print(response.json())

input()

response = requests.get(BASE + "quote/1")
print(response.json())