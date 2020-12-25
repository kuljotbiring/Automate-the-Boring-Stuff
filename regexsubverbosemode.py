import re

caseDocument = 'Agent Alice gave the secret documents to Agent Bob'
namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.findall(caseDocument)
print(mo)

# call .sub method with first argument to replace the re.compile search
redactedMsg = namesRegex.sub('REDACTED', caseDocument)

print(redactedMsg)  # result: REDACTED gave the secret documents to REDACTED

# how to redact only part of the find result for regex
namesRegex = re.compile(r'Agent (\w)\w*')
mo = namesRegex.findall(caseDocument)
# use group 1 only which is just the A and the B
redactedMsg = namesRegex.sub(r'Agent \1 ****', caseDocument)
print(redactedMsg)  # result: Agent A **** gave the secret documents to Agent B ****

# use verbose allows the adding of comments
re.compile(r"""
(\d\d\d-) |    # area code (without parens, with dash
(\(\d\d\d\) )  # -or- are code with parens and no dash
\d\d\d         # first 3 digits
-              # second dash
\d\d\d\d       # last 4 digits
\sx\d{2,4}     # extension, like x12345""", re.VERBOSE)

# for multiple arguments use bitwise operator eg ( , re.IGNORECASE | re.DOTALL | re.verbose)
