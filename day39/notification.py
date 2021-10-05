# from twilio.rest import Client
# from decouple import config



from twilio.rest import Client
import os
from decouple import config

TWILIO_ACCOUNT_SID = config('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = config('TWILIO_AUTH_TOKEN')

class SMSNotification():
    """
    Send SMS notification via Twilio if price of flight is less than or equal to the wishlist price
    """
    def __init__(self):
        self.account_sid = TWILIO_ACCOUNT_SID
        self.auth_token = TWILIO_AUTH_TOKEN
        self.client = Client(self.account_sid,self.auth_token)

    def send_message(self, flight_notification):
        message = self.client.messages \
            .create(
            body=f"{flight_notification}",
            from_='+13126265243',
            to='+254700116007'
        )
        print(message.sid)
        print(message.status)


# alert = SMSNotification()
# alert.send_message()

