"""Q11 — Practical Status Handling"""
import requests

def fetch_data(url: str) -> None:
    try:
        resp = requests.get(url, timeout=10)
    except requests.exceptions.ConnectionError:
        print(f"Connection error when trying to reach: {url}")
        return
    except requests.exceptions.Timeout:
        print(f"Request to {url} timed out")
        return
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return

    code = resp.status_code
    if code == 200:
        print("Success")
    elif 400 <= code <= 499:
        print("Client Error")
    elif 500 <= code <= 599:
        print("Server Error")
    else:
        print(f"Unexpected status code: {code}")

    try:
        print(resp.json())
    except Exception:
        print(resp.text[:200])

if __name__ == "__main__":
    tests = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/invalid",
        "http://does-not-exist.example",
    ]
    for t in tests:
        print('\nFetching:', t)
        fetch_data(t)
