"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)

#Add any logging levels and handlers with app.logger

# 1. Set the logging level for app.logger
app.logger.setLevel(logging.DEBUG)

# 2. Create a StreamHandler and set its level
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

# 3. Add the StreamHandler to app.logger
app.logger.addHandler(stream_handler)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
