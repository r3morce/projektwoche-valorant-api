# A for loop is used for iterating over a sequence

# First we need a list
ranks = ["Radiant", "Immortal", "Diamond",
         "Platinum", "Gold", "Silver", "Bronze", "Iron"]


# The loop is used like this:
for rank in ranks:
    # You can access each item whitin a loop
    print("rank in loop", rank)

# With the for loop you can execute a set of statements, once for each item in a list
for rank in ranks:
    print("lower rank in loop", rank.lower())

# TODO: Loop through the list and print each rank upper case
