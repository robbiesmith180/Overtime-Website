from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy


# Create the application object
app = Flask(__name__)

# Configurations for creating the database using SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False
app.config['SECRET_KEY'] = 'secretkey'

# Create the SQLAlchemy object
db = SQLAlchemy(app)

from app import routes