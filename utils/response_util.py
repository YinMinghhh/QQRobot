import requests

def post(op: str, json) -> requests.models.Response:
    return requests.post("http://localhost:3000/" + op, json=json)
