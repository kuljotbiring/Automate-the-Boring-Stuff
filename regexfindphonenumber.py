# import the regex module
import re

# save the search for the patters in varaible
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# call the search function to search in a string into a match object variable
mo = phoneNumRegex.search("Call me 415-555-10111 tomorrow, or at my office line  415-888-9999")
# display the results griy
print(mo.group())

# find all the phone numbers. returns a list
mo2 = phoneNumRegex.findall("Call me 415-555-10111 tomorrow, or at my office line  415-888-9999")
print(mo2)
