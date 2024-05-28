from flask import Flask
from controllers.routes import register_routes, error
import webview

app = Flask(__name__, static_folder='./static', template_folder='./templates')

try:
    register_routes(app)
except Exception as e:
    error(app, e)

webview.create_window('Registro de Vendas', app)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    # webview.start()
