from twilio.rest import Client
import os
# these credentials are available on your twilio dashboard

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Bacon",
                     from_='+13126265243',
                     to='+254700116007'
                 )

print(message.sid)
print(message.status)


# Project 1 Use twilio to send a message incase it will rain
