from flask import Blueprint
from flask import render_template

from models import Patient

patients = Blueprint('patients', __name__, template_folder='templates')



@patients.route('/')
def patients_list():
    patients = Patient.query.all()
    return render_template('patients/patients.html', patients = patients)

@patients.route('/<slug>')
def patient_detail(slug):
    patient = Patient.query.filter(Patient.slug==slug).first()
    return render_template('patient/patient_detail.html', patient = patient)