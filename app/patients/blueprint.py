from flask import Blueprint
from flask import render_template

from models import Patient

patients = Blueprint('patients', __name__, template_folder='templates')



@patients.route('/')
def patients_list():
    return render_template('patients.html')