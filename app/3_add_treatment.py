from app import db 
from models import *

fluids = Treatment(name = "IV fluids", slug='fluids', medication = "Fluids", status="green")
blood_tests = Treatment(name = "Blood tests", slug='blood test', status = "ambar")
ch_xray = Treatment(name = "Chest and hip Xray", slug='xray', status = "green")
pain = Treatment(name = "Pain relief", slug='pain', medication = "Painkiller")
urin = Treatment(name = "Urin analysis", slug='urin', status = "red")


print(blood_tests.id)

db.session.add(fluids)
db.session.add(blood_tests)
db.session.add(ch_xray)
db.session.add(pain)
db.session.add(urin)
db.session.commit()

print(blood_tests.id)