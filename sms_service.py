from twilio.rest import Client
import os

class SmsService:
    def __init__(self):
        self.account_sid = os.environ['TWILIO_SID']
        self.auth_token = os.environ['TWILIO_KEY']
        self.client = Client(self.account_sid, self.auth_token)

    def appointment_confirmation(self, phone_number):
        message = self.client.messages.create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+17147331519',
                     to=phone_number
                 )

        return message.sid
