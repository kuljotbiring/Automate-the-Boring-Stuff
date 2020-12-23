# import pretty print to make nicer output
import pprint

# We want to count the number of characters in a string

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

# make a dictionary
count = {}

# We loop over the characters in the string
for character in message.upper():

    # initialize each char in the dictionary with 0 using setdefault method
    count.setdefault(character, 0)
    # increment the occurence found
    count[character] += 1

pprint.pprint(count)
