# Ignore the following code

import requests
import json

url = "https://valorant-api.com/v1/weapons/63e6c2b6-4a8e-869c-3d4c-e38355226584"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

json = response.json()
data = json["data"]


print("Weapon Name: {}".format(data["displayName"]))
