# Now we get data from a valorant API and have a look into it

# Ignore the following code. Start at line 18

import requests
import json
import pprint

pp = pprint.PrettyPrinter(sort_dicts=False)

url = "https://valorant-api.com/v1/agents/dade69b4-4f5a-8528-247b-219e5a1facd6"

response = requests.request("GET", url)

response = json.loads(response.text)
data = response["data"]

# We have data from a valorant API stored in a variable called 'data'
# TODO: Let's have a look into it, print 'data'
# TODO: Can you find display name?


# TODO: Use the pretty print command 'pp.pprint()' to see a better readable output.
# TODO: Can you find display name?


# TODO: Print the value of the key 'displayName' from the dictionary 'data'
# Hint: You did this with your name the lesson before
