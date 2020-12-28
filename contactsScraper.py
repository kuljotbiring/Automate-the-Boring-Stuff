import re, pyperclip

# use https://automatetheboringstuff.com/files/examplePhoneEmailDirectory.pdf to test code
# select all text and press copy. then run program. paste grabbed output into a text file

# create a regex for phone numbers
phoneRegex = re.compile(r"""
# 415-555-0000, 555 -000, (415) 555-0000. 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?            # area code (optional)
(\s|-)                              # first separator - either a space or a dash
\d\d\d                              # first 3 digits
-                                   # separator
\d\d\d\d                            # last 4 digits
(((ext(\.)?\s)|x)                   # extension word-part (optional)
 (\d{2,5}))?                        # extension number-part (optional)
 )
""", re.VERBOSE)

emailRegex = re.compile(r"""
[a-zA-Z0-9_.+]+         # name part
@ # @ symbol            # @ symbol
[a-zA-Z0-9_.+]+         # domain name part     

""", re.VERBOSE)

# get text off clipboard
text = pyperclip.paste()

# extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNUmbers = []
for phoneNumber in extractedPhone:
    allPhoneNUmbers.append(phoneNumber[0])

# copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNUmbers) + '\n'.join(extractedEmail)

pyperclip.copy(results)