from flask import Flask
import os

def app():
    app = Flask(__name__, static_folder='../static', template_folder='../templates')
    app.secret_key = os.urandom(24)

    return app