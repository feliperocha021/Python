"""
API (Application Programming Interface) é uma interface que permite que diferentes sistemas conversem entre si.

Muitas APIs modernas usam o padrão REST e se comunicam via HTTP.

Para consumir dados de uma API em Python, a biblioteca mais usada é o requests.

Com ela, você pode enviar requisições HTTP (GET, POST, PUT, DELETE) e receber respostas em formatos como JSON ou XML.
"""

import requests

params = {"userId": 1}
response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)

if response.ok:
    posts = response.json()
    for post in posts:
        print(post["title"])

new_post = {
    "title": "My new post",
    "body": "This is the content",
    "userId": 1
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)

if response.ok:
    print("Created:", response.json())

try:
    response = requests.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()  # raises HTTPError if status != 200
except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
