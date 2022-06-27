from http import client
from pydoc import cli
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
    email = db.Column(db.String(50), nullable=False)
    last4_nric = db.Column(db.String(4), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    role = db.Column(db.String(10), nullable=False)
    study_year = db.Column(db.Integer, nullable=False)

    def __init__(
        self,
        name,
        bdae,
        email,
        last4_nric,
        user_id,
        role,
        study_year
    ):
        self.name = name
        self.bdae = bdae
        self.email = email
        self.last4_nric = last4_nric
        self.user_id = user_id
        self.role = role
        self.study_year = study_year

    def get_dict(self):
        """
        'get_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result


class appointment(db.Model):
    __tablename__ = 'appointment'

    date = db.Column(db.String(10))
    timeslot = db.Column(db.Integer(), nullable=False)
    client_id = db.Column(db.Integer(), db.ForeignKey(users.user_id), nullable=False)
    lawyer_id = db.Column(db.Integer(), db.ForeignKey(users.user_id), nullable=False)
    appointment_id = db.Column(db.Integer(), primary_key=True, nullable=False)

    def __init__(
        self,
        date,
        timeslot,
        client_id,
        lawyer_id,
        appointment_id
    ):
        self.date = date
        self.timeslot = timeslot
        self.client_id = client_id
        self.lawyer_id = lawyer_id
        self.appointment_id = appointment_id
    
    def get_dict(self):
        """
        'get_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

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
    lawyer_case_comments = db.Column(db.String(5000), nullable=False)
    sa_id = db.Column(db.Integer, db.ForeignKey(users.user_id), nullable=False)
    lawyer_id = db.Column(db.Integer, db.ForeignKey(users.user_id), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey(users.user_id), nullable=False)
    appointment_id = db.Column(db.Integer, db.ForeignKey(appointment.appointment_id), nullable=False)
    client_feedback = db.Column(db.String(1500), nullable=False)
    client_approval_status = db.Column(db.String(30), nullable=False)

    def __init__(
        self, 
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
        client_approval_status
    ):
        self.s3_url = s3_url
        self.case_id = case_id
        self.case_status = case_status
        self.case_category = case_category
        self.hearing_date = hearing_date
        self.case_title = case_title
        self.client_case_summary = client_case_summary
        self.sa_case_summary = sa_case_summary
        self.lawyer_case_comments = lawyer_case_comments
        self.sa_id = sa_id
        self.lawyer_id = lawyer_id
        self.client_id = client_id
        self.appointment_id = appointment_id
        self.client_feedback = client_feedback
        self.client_approval_status = client_approval_status
        
    def get_dict(self):
        """
        'get_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

    def assigncase(self, sa_id):
        self.case_status = 'In Progress'
        self.sa_id = sa_id
        
    def update_sa_case_summary(self, sa_case_summary):
        self.sa_case_summary = sa_case_summary
        
    def approve_case(self, client_approval_status):
        self.client_approval_status = client_approval_status
        
    def update_appointment(self, appointment_id):
        self.appointment_id = appointment_id
        
    def update_lawyer_case_comments(self, lawyer_case_comments):
        self.lawyer_case_comments = lawyer_case_comments
        
        
# Retrieve all cases
@app.route('/view_all_cases', methods=['GET'])
def view_all_cases():
    try: 
        output = []
        cases_info = cases.query.all()
        for case in cases_info:
            output.append(case.get_dict())

        return jsonify(
            {
                "code": 200,
                "data": output
            }
        ), 200

    except Exception:
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while retrieving all cases"
            }
        ), 404

# Retrieve all users
@app.route('/view_all_users', methods=['GET'])
def view_all_users():
    try: 
        output = []
        users_info = users.query.all()
        for user in users_info:
            output.append(user.get_dict())

        return jsonify(
            {
                "code": 200,
                "data": output
            }
        ), 200

    except Exception:
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while retrieving all users"
            }
        ), 404

# Retrieve all appointments
@app.route('/view_all_appts', methods=['GET'])
def view_all_appts():
    try: 
        output = []
        appts_info = appointment.query.all()
        for appt in appts_info:
            output.append(appt.get_dict())

        return jsonify(
            {
                "code": 200,
                "data": output
            }
        ), 200

    except Exception:
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while retrieving all appointments"
            }
        ), 404

# create new user for client
@app.route('/new_client', methods=['POST'])
def create_new_client():
    try:
        # retrieve post request data
        data = request.get_json()
        
        data['user_id'] = 0
        data['role'] = "client"

        user_obj = users(**data)

        db.session.add(user_obj)
        db.session.commit()

        return jsonify(
            {
                "code": 200,
                "message": "Client successfully created" 
            }
        ), 200

    except Exception:
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while creating new user"
            }
        ), 404

# Retrieve cases by status
@app.route('/cases_by_status/<string:case_status>', methods=['GET'])
def get_all_cases_by_status(case_status):
    try:
        output = []
        cases_info = cases.query.filter_by(case_status=case_status)
        
        for case in cases_info:
            output.append(case.get_dict())
            
        return jsonify(
            {
                "code": 200,
                "data": output
            }
        ), 200

    except Exception:
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while retrieving opened cases"
            }
        ), 404

@app.route('/create_case', methods=['POST'])
def create_case():
    try:
        # retrieve post request data
        data = request.get_json()
        
        data['case_id'] = 0
        data['case_status'] = 'Pending'
        data['case_category'] = None
        data['sa_case_summary'] = ''
        data['lawyer_case_comments'] = ""
        data['sa_id'] = None
        data['lawyer_id'] = None
        data['appointment_id'] = None
        data['client_feedback'] = ""
        data['client_approval_status'] = None
        data['client_id'] = data['client_id']

        case_obj = cases(**data)
        print(case_obj.get_dict())
        
        db.session.add(case_obj)
        db.session.commit()
        
        return jsonify(
            {
                "code": 200,
                "message": "Case successfully created"
            }
        ), 200

    except Exception:
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while creating case"
            }
        ), 404
        
@app.route('/retrieve_user_info/<string:email>', methods=['GET'])
def get_user_info(email):
    try:
        users_info = users.query.filter_by(email=email).first()
        return jsonify(
            {
                "code": 200,
                "data": users_info.get_dict()
            }
        ), 200

    except Exception:
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while retrieving user info"
            }
        ), 404
        
@app.route('/retrieve_client_case/<string:client_id>', methods=['GET'])
def get_client_case(client_id):
    try:
        client_id = int(client_id)
        case_info = cases.query.filter_by(client_id=client_id).first()
        
        if case_info:
            return jsonify(
                {
                    "code": 200,
                    "data": case_info.get_dict()
                }
            ), 200
            
        else:
            return jsonify(
                {
                    "code": 404,
                    "Message": "Client does not have any case"
                }
            ), 404

    except Exception:
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while retrieving client case"
            }
        ), 404

@app.route('/retrieve_SA_cases/<string:sa_id>', methods=['GET'])
def get_sa_cases(sa_id):
    try:
        output = []
        sa_id = int(sa_id)
        cases_info = cases.query.filter_by(sa_id=sa_id)
        
        for case in cases_info:
            output.append(case.get_dict())
        
        return jsonify(
            {
                "code": 200,
                "data": output
            }
        ), 200

    except Exception:
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while retrieving SA cases"
            }
        ), 404
        
@app.route('/retrieve_lawyer_cases/<string:lawyer_id>', methods=['GET'])
def get_lawyer_cases(lawyer_id):
    try:
        output = []
        lawyer_id = int(lawyer_id)
        cases_info = cases.query.filter_by(lawyer_id=lawyer_id)
        
        for case in cases_info:
            output.append(case.get_dict())
        
        return jsonify(
            {
                "code": 200,
                "data": output
            }
        ), 200

    except Exception:
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while retrieving lawyer cases"
            }
        ), 404
    
@app.route('/assign_case_to_sa', methods=['POST'])
def assign_case_to_sa():
    try:
        data = request.get_json()
        case_id = data['case_id']
        sa_id = data['sa_id']
        
        case = cases.query.filter_by(case_id=case_id).first()
        case.assigncase(sa_id)
        db.session.commit()

        return jsonify(
            {
                "code": 200,
                "message": "Case successfully assigned"
            }
        ), 200

    except Exception:
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while assigning case to SA"
            }
        ), 404

@app.route('/sa_case_summarisation', methods=['POST'])
def sa_case_summarisation():
    try:
        data = request.get_json()
        case_id = data['case_id']
        sa_case_summary = data['sa_case_summary']
        
        case = cases.query.filter_by(case_id=case_id).first()
        case.update_sa_case_summary(sa_case_summary)
        db.session.commit()

        return jsonify(
            {
                "code": 200,
                "message": "SA Case summarisation successfully updated"
            }
        ), 200

    except Exception:
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while updating SA case summarisation"
            }
        ), 404

# client approval
@app.route('/client_approve_case', methods=['POST'])
def client_approve_case():
    try:
        data = request.get_json()
        
        case_id = data['case_id']
        client_approval_status = data['client_approval_status']
        
        case = cases.query.filter_by(case_id=case_id).first()
        case.approve_case(client_approval_status)
        
        db.session.commit()
    
        return jsonify(
            {
                "code": 200,
                "message": "Successfully updated"
            }
        ), 200

    except Exception:
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while updating case approval"
            }
        ), 404
    
# create appointment
@app.route('/create_appointment', methods=['POST'])
def create_appointment():
    try:
        # retrieve data
        data = request.get_json()
        data['appointment_id'] = 0
             
        # add new row in appointment
        appointment_obj = appointment(** data)
        db.session.add(appointment_obj)
        db.session.commit()

        # retrieve appointment_id
        appointment_id = appointment.query.filter_by(client_id=data['client_id']).first().get_dict()['appointment_id']
        print(appointment_id)
        
        # update case
        case_info = cases.query.filter_by(client_id=data['client_id']).first()
        case_info.update_appointment(appointment_id)
        
        db.session.commit()
    
        return jsonify(
            {
                "code": 200,
                "message": "Successfully created appointment"
            }
        ), 200

    except Exception:
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while creating appointment"
            }
        ), 404

# lawyer case comments
@app.route('/lawyer_case_comments', methods=['POST'])
def lawyer_case_comments():
    try:
        data = request.get_json()
        case_id = data['case_id']
        lawyer_case_comments = data['lawyer_case_comments']
        
        case = cases.query.filter_by(case_id=case_id).first()
        case.update_lawyer_case_comments(lawyer_case_comments)
        db.session.commit()

        return jsonify(
            {
                "code": 200,
                "message": "Lawyer case comments successfully updated"
            }
        ), 200

    except Exception:
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while updating lawyer case comments"
            }
        ), 404

# Check case creation status
@app.route('/check_case_creation_status', methods=['POST'])
def case_creation_status():
    try:
        data = request.get_json()
        client_id = data['client_id']
        case_info = cases.query.filter_by(client_id=client_id).first()
        
        output = False
        
        if case_info:
            output = True

        return jsonify(
            {
                "code": 200,
                "creation_status": output
            }
        ), 200

    except Exception:
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while checking case creation status"
            }
        ), 404
        


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5888, debug=True)
