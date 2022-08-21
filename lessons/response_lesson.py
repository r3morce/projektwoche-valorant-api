# Ignore the follwoing code

import requests
import json
import pprint

url = "https://valorant-api.com/v1/agents/dade69b4-4f5a-8528-247b-219e5a1facd6"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

response = json.loads(response.text)
data = response["data"]

# We have data from a valorant API stored in a variable called 'data'
# TODO: Let's have a look into it


# TODO: Use the pretty print 'pprint' command to have a human readable output
pp = pprint.PrettyPrinter(compact=True)
pp.pprint(data)
