import os
import sms_service
from flask import Flask, jsonify, request
from flask_cors import CORS
from sms_service import SmsService
from helpers import convert_to_international, generate_response, check_valid_request

app = Flask(__name__)
CORS(app)

@app.route("/request", methods=['POST'])
def request_notif():
    data = request.get_json(force=True)
    if check_valid_request(data):
        message = SmsService()
        return message.message_request(convert_to_international(data['phone_number']), data['message'])
    else:
        return generate_response('Invalid request')



if __name__ == "__main__":
    app.run()
