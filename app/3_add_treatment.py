from app import db 
from models import *

IV_Fluids = Treatment(treatment = 'IV Fluids', slug = "IV_fluids")
IV_Fluids.id

db.session.add(IV_Fluids)
db.session.commit()
print(IV_Fluids.id)