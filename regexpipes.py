# import the regex module
import re

# save the search for the patters in varaible
# use parenthesis to group searches
phoneNumRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# call the search function to search in a string into a match object variable
mo = phoneNumRegex.search("Batmobile lost a wheel")

# if you cant find the search the variable will store None


print(mo.group())  # displays Batmobile