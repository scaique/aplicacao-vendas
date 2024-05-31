import webview
from controllers.routes import register_routes
from controllers.config import app

app = app()
register_routes(app)
webview.create_window(title='Registro de Vendas', url=app, maximized=True, confirm_close=True)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    # webview.start()
