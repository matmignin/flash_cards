#!/usr/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from werkzeug.utils import secure_filename
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from quiz_app import routes
