from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql'\
    '+mysqlconnector://root@localhost:3306/penteract_db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)
CORS(app)

class users(db.Model):
    __tablename__ = 'users'

    name = db.Column(db.String(30), primary_key=True)
    bdae = db.Column(db.String(10), nullable=False)
    last4_nric = db.Column(db.String(4), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    role = db.Column(db.String(10), nullable=False)
    study_year = db.Column(db.Integer, nullable=False)

    def __init__(self, name, bdae, last4_nric,
                 role, study_year):
        self.name = name
        self.bdae = bdae
        self.last4_nric = last4_nric
        self.role = role
        self.study_year = study_year

    def get_user(self):

        return {
            "name": self.name,
            "bdae": self.bdae,
            "last4_nric": self.last4_nric,
            "role": self.role,
            "study_year" : self.study_year
        }


class appointment(db.Model):
    __tablename__ = 'appointment'

    date = db.Column(db.String(10))
    timeslot = db.Column(db.Integer(), nullable=False)
    client_id = db.Column(db.Integer(), db.ForeignKey(users.user_id), nullable=False)
    lawyer_id = db.Column(db.Integer(), db.ForeignKey(users.user_id), nullable=False)
    appointment_id = db.Column(db.Integer(), primary_key=True, nullable=False)

    def __init__(self, date, timeslot,
                 client_id, lawyer_id, appointment_id):
        self.date = date
        self.timeslot = timeslot
        self.client_id = client_id
        self.lawyer_id = lawyer_id
        self.appointment_id = appointment_id
    
    def get_appointment(self):
        
        return {
            "date": self.date,
            "timeslot": self.timeslot,
            "client_id": self.client_id,
            "lawyer_id": self.lawyer_id,
            "appointment_id": self.appointment_id
        }

class cases(db.Model):
    __tablename__ = 'cases'
  
    s3_url = db.Column(db.String(200), nullable=False)
    case_id = db.Column(db.Integer, primary_key=True)
    case_status = db.Column(db.String(30), nullable=False)
    case_category = db.Column(db.String(30), nullable=False)
    hearing_date = db.Column(db.String(10), nullable=False)
    case_title = db.Column(db.String(100), nullable=False)
    client_case_summary = db.Column(db.String(1500), nullable=False)
    sa_case_summary = db.Column(db.String(5000), nullable=False)
    sa_id = db.Column(db.Integer, db.ForeignKey(users.user_id), nullable=False)
    lawyer_id = db.Column(db.Integer, db.ForeignKey(users.user_id), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey(users.user_id), nullable=False)
    appointment_id = db.Column(db.Integer, db.ForeignKey(appointment.appointment_id), nullable=False)
    client_feedback = db.Column(db.String(1500), nullable=False)
    client_approval_status = db.Column(db.String(30), nullable=False)

    def __init__(self, 
                s3_url,
                case_id,
                case_status,
                case_category,
                hearing_date,
                case_title,
                client_case_summary,
                sa_case_summary,
                lawyer_case_comments,
                sa_id,
                lawyer_id,
                client_id,
                appointment_id,
                client_feedback,
                client_approval_status):
        self.s3_url = s3_url,
        self.case_id = case_id,
        self.case_status = case_status,
        self.case_category = case_category,
        self.hearing_date = hearing_date,
        self.case_title = case_title,
        self.client_case_summary = client_case_summary,
        self.sa_case_summary = sa_case_summary,
        self.lawyer_case_comments = lawyer_case_comments,
        self.sa_id = sa_id,
        self.lawyer_id = lawyer_id,
        self.client_id = client_id,
        self.appointment_id = appointment_id,
        self.client_feedback = client_feedback,
        self.client_approval_status = client_approval_status
        

    def get_cases_info(self):
        return {
            's3_url' : self.s3_url,
            'case_id' : self.case_id,
            'case_status' : self.case_status,
            'case_category' : self.case_category,
            'hearing_date' : self.hearing_date,
            'case_title' : self.case_title,
            'client_case_summary' : self.client_case_summary,
            'sa_case_summary' : self.sa_case_summary,
            'lawyer_case_comments' : self.lawyer_case_comments,
            'sa_id' : self.sa_id,
            'lawyer_id' : self.lawyer_id,
            'client_id' : self.client_id,
            'appointment_id' : self.appointment_id,
            'client_feedback' : self.client_feedback,
            'client_approval_status' : self.client_approval_status
        }

# APIs:
# 1. Return all cases assigned (Case category, hearing date, Case Title)
# 2. Return specific case (Case category, hearing date, case title, document, ...)

@app.route('/view_all_cases', methods=['GET'])
def view_all_cases():
    try: 
        cases_info = cases.query.all()

        return jsonify(
            {
                "code": 200,
                "data": cases_info.json()
            }
        ), 200

    except Exception:
        return jsonify(
            {
                "code": 404,
                "message": "GG"
            }
        ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
