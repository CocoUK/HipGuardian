from app import db 
from models import Patient 

patient = Patient.query.first()

print (patient)

print(patient.treatments.all())
