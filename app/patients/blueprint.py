from flask import Blueprint
from flask import render_template
from flask import request

from models import Patient
from .forms import PatientForm

patients = Blueprint('patients', __name__, template_folder='templates')

@patients.route('/treatment')
def treatment_create():
    form = PatientForm()
    return render_template('patients/treatment_create.html', form = form)



@patients.route('/')
def patients_list():
    q = request.args.get('q')

    if q:
        patients = Patient.query.filter(Patient.name.contains(q) | Patient.surname.contains(q) | Patient.condition.contains(q) | Patient.complication.contains(q) | Patient.procedure.contains(q))
    else:    
        patients = Patient.query.all()
    return render_template('patients/patients.html', patients = patients)

@patients.route('/<slug>')
def patient_detail(slug):
    patient = Patient.query.filter(Patient.slug==slug).first()
    return render_template('patients/patient_detail.html', patient = patient)

@patients.route('/location/<slug>')
def location_detail(slug):
    location = Patient.query.filter(Patient.slug--slug).first()
    return render_template('patients/location_detail.html', location = location)