# Ignore the follwoing code

import requests
import json
from pprint import pprint

url = "https://valorant-api.com/v1/agents/dade69b4-4f5a-8528-247b-219e5a1facd6"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

data = json.loads(response.text)

#

print("Status:", data["status"])
