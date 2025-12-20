import requests
import json

url = "http://localhost:11434/api/chat"
data = {
    "model": "llama3:latest",
    "messages": [
        {"role": "user", "content": "Hello"}
    ],
    "stream": False
}

try:
    print("Sending raw request to Ollama...")
    response = requests.post(url, json=data, timeout=30)
    print(f"Status: {response.status_code}")
    print(f"Body: {response.text}")
except Exception as e:
    print(f"Error: {e}")
