# import SMTP library
import smtplib

# make connection object and connect it to the SMTP server along with the port number
connection = smtplib.SMTP('smtp.gmail.com', 587)

# connect to the server - starts the connection. returns a tuple with response code and bytes object
connection.ehlo()

# start the TLS encryption
connection.starttls()

# enter the loggin information with email address and password
connection.login('kuljotiscool@gmail.com', 'abc123')

# send emails using from and to address, followed by body of the email
connection.sendmail('kuljotiscool@gmail.com', 'tim.cook@apple.com', 'Subject: Software Engineer...\n\n'
                                                                    'Hi Tim, I accept your job offer\n\n-KJ')

# the return object will be all the emails it failed to send. if you get an empty dictionary - all emails sent

# disconnect from SMTP server
connection.quit()