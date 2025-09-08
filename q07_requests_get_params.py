"""Q07 — requests: GET with params"""
import requests
import json

def main():
    url = "https://jsonplaceholder.typicode.com/comments"
    params = {"postId": 1}
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    print(f"Total comments for postId=1: {len(data)}")
    print('\nFirst two items:')
    print(json.dumps(data[:2], indent=2))

if __name__ == "__main__":
    main()
