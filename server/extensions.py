from flask_socketio import SocketIO
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

cors = CORS()
socketio = SocketIO()
db = SQLAlchemy()
