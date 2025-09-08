"""Q06 — requests: Basic GET"""
import requests

def main():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    print("Full JSON response:")
    print(data)
    print('\nTitle field:')
    print(data.get("title"))

if __name__ == "__main__":
    main()
