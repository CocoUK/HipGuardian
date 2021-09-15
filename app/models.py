from datetime import datetime
from enum import unique
from time import time 
import re
from app import db


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    surname = db.Column(db.String(25))
    sex = db.Column(db.String(1))
    age = db.Column(db.Integer)
    admission_date = db.Column(db.DateTime, default = datetime.utcnow)
    ethnicity = db.Column(db.String(25))
    slug = db.Column(db.String(140), unique=True)
    stage = db.Column(db.String(25))
    location = db.Column(db.String(25))
    ACS = db.Column(db.String(1))
    mortality = db.Column(db.String(1))
    procedure = db.Column(db.String(25))
    complication = db.Column(db.String(25))
    condition = db.Column(db.String(25))
   


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.name:
            self.slug = slugify(self.name)
        else:
            self.slug = str(int(time()))

    def __repr__(self):
        return f'<Patient id: {self.id}, name:{self.name}, surname:{self.surname}, age:{self.age}, sex:{self.sex}, admission_date: {self.admission_date}, ethnicity:{self.ethnicity}, slug:{self.slug}, stage:{self.stage}, location:{self.location}, ACS:{self.ACS}, mortality:{self.mortality}, procedure:{self.procedure}, complication:{self.complication}, condition:{self.condition} >'


class Treatment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    treatment = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.slug = slugify(self.treatment)

    def __rep__(self):
        return f'<Treatment id: {self.id}, treatment: {self.treatment}>'



    