# Now we get data from a valorant api and have a look into it

# Ignore the following code. Start at line 18

import requests
import json
import pprint

pp = pprint.PrettyPrinter(sort_dicts=False)

url = "https://valorant-api.com/v1/competitivetiers"

response = requests.request("GET", url)

response = json.loads(response.text)
data = response["data"]

# TODO: Let's have look into the data, pretty print the dictionary 'data'


# Seems like the tier lists are nested into episodes
for episode in data:
    # TODO: Print the value  of key 'assetObjectName' from each 'episode'
    print("")

# The command 'pop' extracts the last element of the list. Let's store it in a variable
current_episode = data.pop()

# We want information about each tier, where are they located?
# Hint: You can use pretty print to have a look into 'current_episode'


# TODO Print the name of each tier
# Hint: You can look into the data with pp.pprint(tiers)
