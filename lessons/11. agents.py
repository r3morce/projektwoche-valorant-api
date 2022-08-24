# Now we get data from a valorant API and have a look into it

# Ignore the following code. Start at line 18

import requests
import json
import pprint

pp = pprint.PrettyPrinter(sort_dicts=False, depth=2)

url = "https://valorant-api.com/v1/agents"

response = requests.request("GET", url)

response = json.loads(response.text)
data = response["data"]

# TODO: Let's have look into the dictionary 'data', pretty print it
pp.pprint(data)


# TODO: Find out how the agents data is structured
# TODO: Find out where the agent name is stored

# TODO: Create a new variable 'agents' and store 'data' in it for better readability
agents = data

# TODO: Print all agents names
# Hint: We did a similar thing in lesson summary

for agent in agents:
    print("")
    
# TODO: Look at the list, what do you notice?