import imapclient, pyzmail

connection = imapclient.IMAPClient('imap.gmail.com', ssl=True)

# enter the loggin information with email address and password
connection.login('kuljotiscool@gmail.com', 'abc123')

# select a folder
connection.select_folder('INBOX', readonly=True)

# return unique IDs for emails received since August 20
UIDs = connection.search(['SINCE 20-Aug-2020'])

# use fetch first arg is UID and second is what part of the email we want
connection.fetch([47474], ['BODY[]', 'FLAGS'])

message = pyzmail.PyzMessage.factory(rawMessage[47474] [b'BODY[]'])

# get the subject
message.get_subject()

# get the address
message.get_addresses('from')

# get the address
message.get_addresses('to')

# get the address
message.get_addresses('bcc')

# see if there is a text part
message.text_part

# see if tehre is an html part
message.html_part

message.text_part.get_payload().decode('UTF-8')