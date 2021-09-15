from wtforms import Form, StringField, TextAreaField

class PatientForm(Form):
    treatment = StringField('Treatment')
    complication = TextAreaField('Complication')