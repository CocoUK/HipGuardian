from wtforms import Form, StringField, TextAreaField, DateField

class PatientForm(Form):
    treatment = StringField('Treatment')
    date = DateField('Date')
    complication = TextAreaField('Complications')
    medication = StringField('Medications')
    action = TextAreaField('Actions')
    status = StringField('Status')
    notes = TextAreaField('Notes')


class TreatmentForm(Form):
    treatment = StringField('Treatment')
    date = DateField('Date')
    complication = TextAreaField('Complications')
    medication = StringField('Medications')
    action = TextAreaField('Actions')
    status = StringField('Status')
    notes = TextAreaField('Notes')