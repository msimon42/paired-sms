import os
from flask import jsonify

def convert_to_international(number):
    return f"+1{number}"

def generate_response(type):
    return jsonify('response': type)

def check_valid_request(data):
    return all([valid_keys(keys(data),
     valid_phone_number(data['phone_number']),
     valid_token(data['sms_token']),
     valid_message(data['message'])])

def valid_keys(keys):
    valid = {'phone_number', 'message', 'sms_token'}
    return valid == set(keys)

def valid_phone_number(number):
    valid_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    li_number = list(number)

    for number in li_number:
        if number not in valid_chars:
            li_number.remove(number)

    return len(li_number) == 10

def valid_token(token):
    return token == os.environ['SMS_TOKEN']

def valid_message(message):
    return len(message) >= 1
