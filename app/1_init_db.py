from app import db 
from models import *

db.create_all()


#Populate patient db

entry1 = Patient(name="Alasdair", surname="Bowen", sex="M", age="25",  ethnicity = "white", stage="Post-op", location ="Rehab Ward", ACS="87", mortality="8",
                    complication="-", procedure="external fixation of fracture right angle", condition="-") 
entry2 = Patient(name="Heather", surname="Loftus", sex="F", age="18",  ethnicity = "white" , stage="Post-op", location ="Rehab Ward", ACS="83", mortality="9",
                    complication="Unstable blood sugars", procedure="screw and plate to left radius and ulna", condition="Type 1 Diabetes")               
entry3 = Patient(name="Ewan", surname="Duncan", sex="M", age="17", ethnicity = "white" , stage="Post-op", location ="Rehab Ward", ACS="80", mortality="12",
                    complication="-", procedure="screw and plate to fractured right tibia", condition="Asthma")


 
 

db.session.add( entry1)
db.session.add( entry2)
db.session.add( entry3)
 
db.session.commit()

print(entry1)