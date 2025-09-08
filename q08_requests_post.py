"""Q08 — requests: POST JSON"""
import requests
import json

def main():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {"title": "OOPs Assignment", "body": "Learning Python requests", "userId": 101}
    resp = requests.post(url, json=payload, timeout=10)
    print("Status code:", resp.status_code)
    try:
        print("Response JSON:", resp.json())
    except Exception:
        print("No JSON returned")

if __name__ == "__main__":
    main()
