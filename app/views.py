# functions for handling user request
from app import app
from flask import render_template


@app.route('/')
def index():
    user = 'Amy'
    return render_template('index.html',user=user)

