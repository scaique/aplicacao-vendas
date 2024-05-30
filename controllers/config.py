from flask import Flask

def app():
    app = Flask(__name__, static_folder='../static', template_folder='../templates')
    app.secret_key = 'supersecretkey'

    return app