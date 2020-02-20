import os
import sms_service
from flask import Flask, jsonify, request
from flask_cors import CORS
from sms_service import SmsService
from helpers import convert_to_international

app = Flask(__name__)
CORS(app)

@app.route("/request", methods=['POST'])
def request_notif():
    data = request.get_json(force=True)
    if data['sms_token'] == os.environ['SMS_TOKEN']:
        message = SmsService()
        return message.message_request(convert_to_international(data['phone_number']), data['message'])
    else:
        return 'Invalid token. Message not sent.'



if __name__ == "__main__":
    app.run()
