import os

from flask import Flask, jsonify
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    return app

    @app.route("/", methods=['GET'])
    def hello_world():
        return "Hello World"

app = create_app()

if __name__ == "__main__":
    app.run()
