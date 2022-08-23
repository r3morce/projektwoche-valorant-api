# Now we get data from a valorant API and have a look into it

# Ignore the following code. Start at line 18

import requests
import json
import pprint

pp = pprint.PrettyPrinter(sort_dicts=False)

url = "https://valorant-api.com/v1/competitivetiers"

response = requests.request("GET", url)

response = json.loads(response.text)
data = response["data"]

# TODO: Let's have look into the dictionary 'data', pretty print it
# Hint: We did pretty printing in lesson 4


# It seems like the tier lists are nested into episodes

for episode in data:
    # TODO: Print the value  of key 'assetObjectName' from each 'episode'
    print("")

# The command 'pop' extracts the last episode of the list. Let's store it in a variable
current_episode = data.pop()

# TODO: Pretty print 'current_episode' and find out how tier information is structured
pp.pprint(current_episode)


# TODO Print the name of each tier with a for-loop
# Hint: Use a for-loop like above
# Hint: We printed values from dictionaries in 3. dictionary
