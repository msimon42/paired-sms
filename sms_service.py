from twilio.rest import Client

class SmsService:
    def __init__(self):
        self.account_sid = 'AC2941d98ae9b3e95cbdd26ab748b51bed'
        self.auth_token = 'b9425062024348ef6467d815848ee4f8'
        self.client = Client(self.account_sid, self.auth_token)

    def appointment_confirmation(self, phone_number):
        message = self.client.messages.create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+17147331519',
                     to=phone_number
                 )

        return message.sid
