import requests
url = "http://127.0.0.1:5000/api/jokes/3"
response = requests.get(url)
print(response.json())
# Use requests package to call your api address http://127.0.0.1:5000/api/joke to display a funny joke

