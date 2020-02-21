import os

class ValidateRequest:

    def __init__(self):
        pass

    def run(self, data):
        keys = self.valid_keys(data.keys())
        phone_number = self.valid_phone_number(data['phone_number'])
        token = self.valid_token(data['sms_token'])
        message = self.valid_message(data['message'])
        return all([keys, phone_number, token, message])

    def valid_keys(self, keys):
        valid = {'phone_number', 'message', 'sms_token'}
        return valid == set(keys)

    def valid_phone_number(self, number):
        valid_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        li_number = list(number)

        for number in li_number:
            if number not in valid_chars:
                li_number.remove(number)

        return len(li_number) == 10

    def valid_token(self, token):
        return token == os.environ['SMS_TOKEN']

    def valid_message(self, message):
        return len(message) >= 1
