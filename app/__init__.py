from flask import Flask, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
from .routes import (
    add_book_bp,
    list_books_bp,
    search_books_bp,
    delete_book_bp,
    update_book_bp
)

def create_app():

    app = Flask(__name__)

    @app.route('/swagger.yaml')
    def swagger_spec():
        return send_from_directory('.', 'swagger.yaml')

    # swagger UI setup
    SWAGGER_URL = '/api-docs'
    API_URL = 'swagger.yaml'  
    swagger_ui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    # API blueprints
    app.register_blueprint(add_book_bp, url_prefix='/api')
    app.register_blueprint(list_books_bp, url_prefix='/api')
    app.register_blueprint(search_books_bp, url_prefix='/api')
    app.register_blueprint(delete_book_bp, url_prefix='/api')
    app.register_blueprint(update_book_bp, url_prefix='/api')

    return app