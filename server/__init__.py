import os
from flask import Flask
from server.extensions import socketio, cors, db
from server.api.init_api import init_api

MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@db/flask'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(init_api)

    socketio.init_app(app, cors_allowed_origins='*')
    cors.init_app(app)
    db.init_app(app)

    return app
