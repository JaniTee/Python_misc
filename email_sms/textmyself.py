#! python3
# textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string.

 # Preset values:
 
accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
authToken  = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
myNumber = '+358xxxxxx'
twilioNumber = '+195xxxxxxx'
from twilio.rest import Client

def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)
