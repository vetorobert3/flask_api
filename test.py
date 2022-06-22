import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"author": "Thomas Carlyle", "quote": "No pressure, no diamonds."},
    {"author": "Helen Keller", "quote": "We can do anything we want if we stick to it long enough."},
    {"author": "Samuel Beckett", "quote": "Try again. Fail again. Fail better"},
    {"author": "Seneca", "quote": "He who is brave is free"}
]

for i in range(len(data)):
    response = requests.put(BASE + "quote/" + str(i), data[i])
    print(response.json())

input()

response = requests.get(BASE + "quote/8")
print(response.json())