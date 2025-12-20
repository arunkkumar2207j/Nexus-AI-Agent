import requests

try:
    r = requests.get("http://localhost:11434/api/tags")
    print(r.json())
except Exception as e:
    print(e)
