import re

"""*********************************** USING A ^ SYMBOL - START WITH PATTERN **************************************"""
# use carrot here to find something that starts with desired string
beginsWithHelloRegex = re.compile(r'^Hello')
mo = beginsWithHelloRegex.search('Hello there!')
print(mo.group())

"""*********************************** USING A $ SYMBOL - END WITH PATTERN **************************************"""
# use dollar to say what string should end with
endsWithWorldRegex = re.compile(r'world!$')
mo = endsWithWorldRegex.search('Hello world!')
print(mo.group())

"""*************************** USING A ^ and $ SYMBOL - START STOP EXACT PATTERN ******************************"""
# use carrot and dollar to specify entire text must start and end with JUST that pattern
allDigitsRegex = re.compile(r'^\d+$')
mo = allDigitsRegex.search('2316544646446877787864')
print(mo.group())

# mo = allDigitsRegex.search('23165446464x46877787864')
# print(mo.group()) this wont work since the x breaks up the pattern

"""****************************** USING A . SYMBOL - WILDCARD (except new line) *******************************"""
# anything and then .at the DOT character matches a single char
atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)  # returns ['cat', 'hat', 'sat', 'lat', 'mat']

"""****************************** USING A .* SYMBOLS - ANY PATTERN *******************************"""
# .* uses greedy mode
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.findall('First Name: Kuljot Last Name: Biring')
print(mo)

# non greedy version example
serve = '<To serve humans> for dinner.>'
nonGreedy = re.compile(r'<(.*?)>')
mo = nonGreedy.findall(serve)
print(mo)

# greedy version example
serve = '<To serve humans> for dinner.>'
nonGreedy = re.compile(r'<(.*)>')
mo = nonGreedy.findall(serve)
print(mo)

# every character is every character EXCEPT new line
prime = 'Serve the public trust, \nProtect the innocent. \nUphold the law.'

dotStar = re.compile(r'.*')
mo = dotStar.search(prime)
print(mo.group())  # result: Serve the public trust, since newline stops it

# how to get EVERY CHARACTER!!
dotStar = re.compile(r'.*', re.DOTALL)
mo = dotStar.search(prime)
print(mo.group())  # returns full string

# make search case insensitive
ignoreRegex = re.compile(r'[aeiou]', re.IGNORECASE)
mo = ignoreRegex.findall('All Your Base Are Belong To Us')
print(mo)  # result ['A', 'o', 'u', 'a', 'e', 'A', 'e', 'e', 'o', 'o', 'U']
