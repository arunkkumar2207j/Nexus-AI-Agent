import requests
import sys

try:
    print("Sending request...")
    r = requests.post("http://localhost:8000/api/chat", json={"message": "What is in the document?"}, timeout=60)
    print(f"Status: {r.status_code}")
    print(f"Response: {r.text}")
except Exception as e:
    print(f"Error: {e}")
