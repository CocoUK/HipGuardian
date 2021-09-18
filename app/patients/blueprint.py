from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect, url_for

from models import Patient
from .forms import TreatmentForm
from app import db 

patients = Blueprint('patients', __name__, template_folder='templates')

@patients.route('/treatment/', methods=['POST', 'GET'])
def treatment_create():
    
    form = TreatmentForm()

    if request.method == 'POST':
        treatment = request.form.get('treatment')
        date = request.form.get('Date')
        complication = request.form.get('Complications')
        medication = request.form.get('Medications')
        action = request.form.get('Actions')
        status = request.form.get('Status')
        notes = request.form.get('Notes')

        try:
             treatment  = Patient(treatment= treatment)
             db.session.add(treatment)
             db.session.acommit()
        except:
            print('Very long traceback')
        return redirect(url_for('patients.patient_detail', slug = "#"))
  
    return render_template('patients/treatment_create.html', form = form)


@patients.route('/')
def patients_list():
    q = request.args.get('q')

    if q:
        patients = Patient.query.filter(Patient.name.contains(q) | Patient.surname.contains(q) | Patient.condition.contains(q) 
            | Patient.complication.contains(q) | Patient.procedure.contains(q) | Patient.location.contains(q) | Patient.stage.contains(q))
    else:    
        patients = Patient.query.order_by(Patient.admission_date.desc())

    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    
    pages = patients.paginate(page=page, per_page=10)

    return render_template('patients/patients.html', patients = patients, pages=pages)

@patients.route('/<slug>')
def patient_detail(slug):
    patient = Patient.query.filter(Patient.slug==slug).first()
    return render_template('patients/patient_detail.html', patient = patient)

@patients.route('/location/<slug>')
def location_detail(slug):
    location = Patient.query.filter(Patient.slug--slug).first()
    return render_template('patients/location_detail.html', location = location)


@patients.route('<slug>/treatment', methods=['POST', 'GET'])
def treatment_add(slug):
    patient = Patient.query.filter(Patient.slug==slug).first()

    if request.method =="POST":
        form = TreatmentForm(fromdata=request.form, obj=patient)
        form.populate_obj(patient)
        db.session.commit()
        return redirect(url_for('patients.patient_detail', slug=patient.slug))
    form = TreatmentForm(obj=patient)
    return render_template('patients/treatment_create.html', patient = patient, form = form)


    
    