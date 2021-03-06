from twilio.rest import Client
from flask import jsonify
from helpers import generate_response
import os

class SmsService:
    def __init__(self):
        self.account_sid = os.environ['TWILIO_SID']
        self.auth_token = os.environ['TWILIO_KEY']
        self.client = Client(self.account_sid, self.auth_token)

    def message_request(self, phone_number, message):
        message = self.client.messages.create(
                     body=message,
                     from_='+17147331519',
                     to=phone_number
                 )
        if message.sid:
            return generate_response('success')
        else:
            return generate_response('Twilio error')
