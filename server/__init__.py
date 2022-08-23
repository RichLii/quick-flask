from flask import Flask
from server.extensions import socketio, cors
from server.api.init_api import init_api


def create_app():
    app = Flask(__name__)

    app.register_blueprint(init_api)

    socketio.init_app(app, cors_allowed_origins='*')
    cors.init_app(app)

    return app
