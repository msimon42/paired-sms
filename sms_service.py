from twilio.rest import Client
import os

class SmsService:
    def __init__(self):
        self.account_sid = os.environ['TWILIO_SID']
        self.auth_token = os.environ['TWILIO_KEY']
        self.client = Client(self.account_sid, self.auth_token)

    def appointment_request(self, phone_number, name, time):
        message = self.client.messages.create(
                     body=f"Hello! {name} has requested a pairing at {time}. Visit https://paired-turing.firebaseapp.com/schedule to confirm",
                     from_='+17147331519',
                     to=phone_number
                 )

        return message.sid

    def appointment_confirmation(self, phone_number, name, time):
        message = self.client.messages.create(
                     body=f"Hello! {name} has confirmed your request to pair at {time}. You're all set!",
                     from_='+17147331519',
                     to=phone_number
                 )

        return message.sid
