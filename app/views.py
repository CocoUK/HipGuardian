# functions for handling user request
from app import app
from flask import render_template
import pandas as pd 
from models import Patient


@app.route('/')
def index():
    user = 'Amy'
    return render_template('index.html',user=user)




@app.route("/dashboard")
def dashboard():
    user = 'Amy'
    
    entries = Patient.query.order_by(Patient.admission_date.desc()).all()
    #location_sex
    ##subset location and sex
    location = [] 
    sex = []
    for entry in entries:
        location.append(entry.location)
        sex.append(entry.sex)

    ##Create dataframe 
    location_sex = pd.DataFrame()
    location_sex['location'] = location
    location_sex['sex'] = sex

    location_sex = location_sex.groupby('location').sex.count()

    return render_template("dashboard.html", user= user, entries=entries)