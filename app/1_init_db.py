from app import db 
from models import *

db.create_all()


#Populate patient db

entry1 = Patient(name="Alasdair", surname="Bowen", sex="M", age="25",  ethnicity = "white" )
entry2 = Patient(name="Heather", surname="Loftus", sex="F", age="18",  ethnicity = "white" )                 
entry3 = Patient(name="Ewan", surname="Duncan", sex="M", age="17", ethnicity = "white" )
 

db.session.add( entry1)
db.session.add( entry2)
db.session.add( entry3)
 
db.session.commit()

print(entry1)