# Contains code of application

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config



# Create an instance of class Flask
app = Flask(__name__)
app.config.from_object(Config)



db = SQLAlchemy(app)