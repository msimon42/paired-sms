from flask import Flask
from flask_cors import CORS


app = FLASK(__name__)
CORS(app)


if __name__ == '__main__':
   app.run(debug = True)
