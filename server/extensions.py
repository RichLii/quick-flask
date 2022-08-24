from flask_socketio import SocketIO
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

cors = CORS()
socketio = SocketIO()
db = SQLAlchemy()
migrate = Migrate()
