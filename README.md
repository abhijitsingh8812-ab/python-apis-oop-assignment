# python-apis-oop-assignment
# python-apis-oop-assignment

Small Python assignment covering OOP and `requests` usage. Python 3.10+ required.

## Repo layout

python-apis-oop-assignment/
├─ src/
│  ├─ q01_oop_book_basics.py
│  ├─ q02_oop_encapsulation.py
│  ├─ q03_oop_inheritance.py
│  ├─ q04_oop_polymorphism.py
│  ├─ q05_oop_all_in_one.py
│  ├─ q06_requests_get.py
│  ├─ q07_requests_get_params.py
│  ├─ q08_requests_post.py
│  ├─ q09_requests_put_delete.py
│  ├─ q10_http_status_classifier.py
│  ├─ q11_fetch_with_status_handling.py
│  └─ q12_cli_http_client.py
├─ tests/
│  └─ smoke_tests.py
└─ requirements.txt

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run individual files

Each `src/qNN_*.py` file can be run directly. Example:

```bash
python src/q01_oop_book_basics.py
python src/q06_requests_get.py
```

## Run CLI client

```bash
python src/q12_cli_http_client.py GET https://jsonplaceholder.typicode.com/posts/1
python src/q12_cli_http_client.py POST https://jsonplaceholder.typicode.com/posts '{"title":"x","body":"y","userId":1}'
```

## Smoke tests

```bash
python tests/smoke_tests.py
```
