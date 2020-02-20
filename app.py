import os
import sms_service
from flask import Flask, jsonify, request
from flask_cors import CORS
from sms_service import SmsService

def create_app():
    app = Flask(__name__)


    @app.route("/request", methods=['POST'])
    def request_notif():
        data = request.get_json(force=True)
        message = SmsService()
        return message.appointment_request(data['phone_number'], data['name'], data['time'])



    return app


app = create_app()

if __name__ == "__main__":
    app.run()
