import requests

endpoint = "http://localhost:8000/api/"
# endpoint = "https://httpbin.org/anything"
r = requests.get(endpoint, params={"key": "value"}, json={"query": "python"})
print(r.json())
