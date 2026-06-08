import requests
from dags.opendota.config import entities
for entity in entities:
    resp = requests.get(f"https://api.opendota.com/api/{entity["endpoint"]}")
    resp = resp.json()
    print(resp)


