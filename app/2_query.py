from app import db 
from models import *

patients = Patient.query.all()

print(patients)

p1 = Patient.query.filter(Patient.name.contains('Ewan')).all()
print(p1)

p2 = Patient.query.filter(Patient.name.contains('Ewan')).first()
print(p2)

p3 = Patient.query.filter(Patient.name=='Ewan').first()
print(p3)

