import requests
from pprint import pprint

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + '')
pprint(response.json())
