# Now we get data from a valorant API and have a look into it

# Ignore the following code. Start at line 19

import requests
import json
import pprint

pp = pprint.PrettyPrinter(sort_dicts=False, depth=4)

url = "https://valorant-api.com/v1/competitivetiers"

response = requests.request("GET", url)

response = json.loads(response.text)
data = response["data"]
data = data[4:]

# TODO: Let's have look into the dictionary 'data', pretty print it
# Hint: We did pretty printing in lesson 'json pretty print'



for episode in data:
    # TODO: Print the value  of key 'assetObjectName' from each 'episode'
    # Hint: We did this in lesson summary
    
    print("")

# The method 'pop' extracts the last episode of the list. Let's store it in a variable
current_episode = data.pop()

# TODO: Pretty print 'current_episode' and find out where tier information is located


# TODO: save tiers in a variable
# Hint: We did this is in lesson dicionary


# TODO Print the name of each tier with a for-loop
# Hint: We printed values in lesson dicionary

