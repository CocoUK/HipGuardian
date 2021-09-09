# Contains code of application

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config
from patients.blueprint import patients


# Create an instance of class Flask
app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(patients, url_prefix='/patient')

db = SQLAlchemy(app)