import os
from flask import jsonify

def convert_to_international(number):
    return f"+1{number}"

def generate_response(type):
    return jsonify({'response': type})
