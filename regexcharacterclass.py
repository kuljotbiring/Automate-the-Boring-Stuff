# import the regex module
import re

# \d does any digit 0 to 9
# \D any character that is NOT a numeric digit 0 to 9
# \w any letter, numeric digit, or underscore char
# \W any character that is not a letter, digit, or underscore
# \s any space, tab, or newline char
# \S any character that is NOT space, tab, or newline char

lyrics = '12 drummers drumming, 11 pipers piping, 10 lords-a-leaping, 9 ladies dancing, 8 maids-a-milking, ' \
         '7 swans-a-swimming, 6 geese-a-laying, 5 golden rings, 4 calling birds, 3 French hens, 2 turtle doves' \
         'and 1 partridge in a pear tree'

# find some number with words
# we use the expression. 1 or more digit, a space, and then one or more word
xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall(lyrics)
print(mo)

# results of print are
""""['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 golden', 
'4 calling', '3 French', '2 turtle', '1 partridge']"""

# use square brackets to make own character class using square brackets
vowelRegex = re.compile(r'[aeiou]')  # is equivalent to saying r'(a|e|i|o|u)'
mo = vowelRegex.findall('robocop eats baby food.')
print(mo)  # result is ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o']

doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
mo = doubleVowelRegex.findall('Robocop eats baby food.')
print(mo)  # result is ['ea', 'oo'] since it looks for double vowels (two in a row)

# us a carrot symbol ^ which means NOT
# here find everything any character not in here ( will get ANY char not in there)
vowelRegex = re.compile(r'[^aeiouAEIOU]')  # is equivalent to saying r'(a|e|i|o|u)'
mo = vowelRegex.findall('robocop eats baby food.')
print(mo)  # result is ['r', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.']