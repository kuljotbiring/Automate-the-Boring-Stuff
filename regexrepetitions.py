# import the regex module
import re

"""**************************** USING A ? SYMBOL  - ZERO OR ONE MATCHES ******************************************"""
# using ? means match preceeding group zero or one times
batRegex = re.compile(r'Bat(wo)?man')  # this will search for batwoman or batman
mo = batRegex.search('The Adventures of Batman')

print(mo.group())  # will display Batman

mo = batRegex.search('The Adventures of Batwoman')

print(mo.group())  # will display Batwoman

mo = batRegex.search('The Adventures of Batwowowoman')

try:
    print(mo.group())  # will display None as wo was either zero or one times to match
except:
    print('This returns nothing')

# find phone numbers where area code is optional
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phonenumber is 555-1234. Call me tomorrow')
print(mo.group())

"""*********************************** USING A * SYMBOL - ZERO OR MORE TIME **************************************"""
# the * star character means match zero or more times
batRegex = re.compile(r'Bat(wo)*man')

mo = batRegex.search('The Adventures of Batman')
print(mo.group())  # will display Batman

mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())  # will display Batwoman

mo = batRegex.search('The Adventures of Batwowowoman')
print(mo.group())  # will display Batwowowoman

"""*********************************** USING A + SYMBOL - ONE OR MORE TIMES *************************************"""
# the + mean match one or more times
batRegex = re.compile(r'Bat(wo)+man')

# mo = batRegex.search('The Adventures of Batman')
# print(mo.group())  # will display NONE

mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())  # will display Batwoman

mo = batRegex.search('The Adventures of Batwowowoman')
print(mo.group())  # will display Batwowowoman


"""******************************* USING A {num} SYMBOL - EXACT NUMBER OF TIMES ********************************"""
haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('He said HaHaHa')
print(mo.group())

"""****************************** USING A {num} SYMBOL - EXACT RANGE NUMBER OF TIMES *******************************"""
# 5 is inclusive. Leaving out the first number implies 0 to other number. leaving out second means first num or more
haRegex = re.compile(r'(Ha){3,5}')
mo = haRegex.search('He said HaHaHaHaHa')
print(mo.group())

# regex does GREEDY matches. meaning it will return the most it can at the earliest it can
digitRegex = re.compile(r'(\d){3,5}')
mo = digitRegex.search('1234567890')
print(mo.group())  # matches 123453

# if you want to make it NON-GREET use a ? with it. will match smallest possible string
digitRegex = re.compile(r'(\d){3,5}?')
mo = digitRegex.search('1234567890')
print(mo.group())  # matches 123
