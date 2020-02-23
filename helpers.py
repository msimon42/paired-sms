import os
from flask import jsonify

def convert_to_international(number):
    return f"+1{number}"

def generate_response(type):
    return jsonify({'response': type})

def digits():
    return ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
