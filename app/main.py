# enter point of app
from app import app
from app import db
import views

from patients.blueprint import patients

app.register_blueprint(patients, url_prefix='/patient')

if __name__ =='__main__':
    app.run()