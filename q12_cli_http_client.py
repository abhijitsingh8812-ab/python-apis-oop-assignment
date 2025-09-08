"""Q12 — Mini CLI HTTP Client
Usage examples:
  python q12_cli_http_client.py GET https://jsonplaceholder.typicode.com/posts/1
  python q12_cli_http_client.py POST https://jsonplaceholder.typicode.com/posts '{"title":"x","body":"y","userId":1}'
"""
import sys
import json
import requests

def main(argv):
    if len(argv) < 2:
        print("Usage: python q12_cli_http_client.py METHOD URL [JSON_BODY]")
        return
    method = argv[0].upper()
    url = argv[1]
    body = None
    if method in ("POST", "PUT"):
        if len(argv) < 3:
            print("POST/PUT require a JSON body string as the 3rd argument")
            return
        raw = argv[2]
        try:
            body = json.loads(raw)
        except json.JSONDecodeError:
            print("Invalid JSON body")
            return

    try:
        if method == "GET":
            resp = requests.get(url, timeout=10)
        elif method == "POST":
            resp = requests.post(url, json=body, timeout=10)
        elif method == "PUT":
            resp = requests.put(url, json=body, timeout=10)
        elif method == "DELETE":
            resp = requests.delete(url, timeout=10)
        else:
            print("Invalid method. Use GET, POST, PUT, DELETE")
            return
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return

    print("Status:", resp.status_code)
    try:
        print(resp.json())
    except Exception:
        print(resp.text)

if __name__ == "__main__":
    main(sys.argv[1:])
