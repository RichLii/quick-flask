from flask import Flask
from server.extensions import socketio, cors, db
from server.api.init_api import init_api


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<username>:<password>@<ip>/flask'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(init_api)

    socketio.init_app(app, cors_allowed_origins='*')
    cors.init_app(app)
    db.init_app(app)

    return app
