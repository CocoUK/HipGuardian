from app import db 
from models import *

treatments = Treatment.query.all()
patient = Patient.query.first()

for treatment in treatments:
    patient.treatments.append(treatment)


print(patient.treatments.all())
db.session.add(patient)
db.session.commit()
 



 

