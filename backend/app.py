from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql'\
    '+mysqlconnector://root@localhost:3306/penteract_db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)
CORS(app)

class users(db.Model):
    __tablename__ = 'users'
    
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    bdae = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    last4_nric = db.Column(db.String(4))
    role = db.Column(db.String(10), nullable=False)
    educational_instituition = db.Column(db.String(50))
    study_year = db.Column(db.Integer)
    company = db.Column(db.String(50))
    position = db.Column(db.String(50))

    def __init__(
        self,
        user_id,
        name,
        password,
        bdae,
        email,
        last4_nric,
        role,
        educational_instituition,
        study_year,
        company,
        position
    ):
        self.user_id = user_id
        self.name = name
        self.password = password
        self.bdae = bdae
        self.email = email
        self.last4_nric = last4_nric
        self.role = role
        self.educational_instituition = educational_instituition
        self.study_year = study_year
        self.company = company
        self.position = position
        
    def get_dict(self):
        """
        'get_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        
        datetime_column = ['bdae']
        
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            if column in datetime_column:
                result[column] = getattr(self, column).strftime("%Y-%m-%d")
                
            else:
                result[column] = getattr(self, column)
            
        return result
    
    def update_columns(self, update_dict):
        """
        'update_columns' which updates the corresponding 
        key, value pair in the object instance
        """
        for column in update_dict:
            self[column] = update_dict[column]
            
    def validate_password(self, password):
        return self.password == password

class cases(db.Model):
    __tablename__ = 'cases'
    
    case_id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(30), nullable=False)
    client_id = db.Column(db.Integer, nullable=False)
    gross_salary = db.Column(db.Integer, nullable=False)
    case_title = db.Column(db.String(100), nullable=False)
    case_category = db.Column(db.String(30), nullable=False)
    court_hearing_date = db.Column(db.Date, nullable=False)
    client_case_description = db.Column(db.String(1500))
    s3_url = db.Column(db.String(200))
    sa_id = db.Column(db.Integer)
    lawyer_id = db.Column(db.Integer)
    current_case_status = db.Column(db.String(30), nullable=False)
    student_assigned_date = db.Column(db.Date)
    case_summary_date = db.Column(db.Date)
    finalised_case_summary_date = db.Column(db.Date)
    confirmed_appointment_date = db.Column(db.Date)
    consultation_date = db.Column(db.Date)
    consultation_questions = db.Column(db.String(5000))
    consultation_advices = db.Column(db.String(5000))
    client_summary_approval = db.Column(db.String(30))
    pre_consult_req = db.Column(db.Integer)
    pre_consult_google_docs_link = db.Column(db.String(300))

    def __init__(
        self,
        case_id,
        client_name,
        client_id,
        gross_salary,
        case_title,
        case_category,
        court_hearing_date,
        client_case_description,
        s3_url,
        sa_id,
        lawyer_id,
        current_case_status,
        student_assigned_date,
        case_summary_date,
        finalised_case_summary_date,
        confirmed_appointment_date,
        consultation_date,
        consultation_questions,
        consultation_advices,
        client_summary_approval,
        pre_consult_req,
        pre_consult_google_docs_link
    ):
        self.case_id = case_id
        self.client_name = client_name
        self.client_id = client_id
        self.gross_salary = gross_salary
        self.case_title = case_title
        self.case_category = case_category
        self.court_hearing_date = court_hearing_date
        self.client_case_description = client_case_description
        self.s3_url = s3_url
        self.sa_id = sa_id
        self.lawyer_id = lawyer_id
        self.current_case_status = current_case_status
        self.student_assigned_date = student_assigned_date
        self.case_summary_date = case_summary_date
        self.finalised_case_summary_date = finalised_case_summary_date
        self.confirmed_appointment_date = confirmed_appointment_date
        self.consultation_date = consultation_date
        self.consultation_questions = consultation_questions
        self.consultation_advices = consultation_advices
        self.client_summary_approval = client_summary_approval
        self.pre_consult_req = pre_consult_req
        self.pre_consult_google_docs_link = pre_consult_google_docs_link

    def get_dict(self):
        """
        'get_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        
        datetime_column = [
            'court_hearing_date',
            'student_assigned_date',
            'case_summary_date',
            'finalised_case_summary_date',
            'confirmed_appointment_date',
            'consultation_date'
        ]
        
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            if column in datetime_column:
                if getattr(self, column):
                    result[column] = getattr(self, column).strftime("%Y-%m-%d")
                
            else:
                result[column] = getattr(self, column)
            
        return result
    
    def update_columns(self, update_dict):
        """
        'update_columns' which updates the corresponding 
        key, value pair in the object instance
        """
        for column in update_dict:
            self[column] = update_dict[column]
            
class case_summary(db.Model):
    __tablename__ = 'case_summary'
    
    case_id = db.Column(db.Integer, nullable=False)
    case_summary_id = db.Column(db.Integer, primary_key=True)
    summary_of_facts = db.Column(db.String(3000))
    issues_questions = db.Column(db.String(3000))
    applicable_law = db.Column(db.String(2000))
    court_hearing_matter = db.Column(db.String(2000))
    specific_questions = db.Column(db.String(2000))
    client_summary_feedback = db.Column(db.String(1500))
    
    def __init__(
        self,
        case_id,
        case_summary_id,
        summary_of_facts,
        issues_questions,
        applicable_law,
        court_hearing_matter,
        specific_questions,
        client_summary_feedback
    ):
        self.case_id = case_id
        self.case_summary_id = case_summary_id
        self.summary_of_facts = summary_of_facts
        self.issues_questions = issues_questions
        self.applicable_law = applicable_law
        self.court_hearing_matter = court_hearing_matter
        self.specific_questions = specific_questions
        self.client_summary_feedback = client_summary_feedback
    
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
    
    def update_columns(self, update_dict):
        """
        'update_columns' which updates the corresponding 
        key, value pair in the object instance
        """
        for column in update_dict:
            self[column] = update_dict[column]
            
class chats(db.Model):
    __tablename__ = 'chats'
    
    case_id = db.Column(db.Integer, nullable=False)
    chat_id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), nullable=False)
    sender_id = db.Column(db.Integer)
    message = db.Column(db.String(1500), nullable=False)
    msg_date_time = db.Column(db.DateTime, nullable=False)
    
    def __init__(
        self,
        case_id,
        chat_id,
        category,
        sender_id,
        message,
        msg_date_time,
    ):
        self.case_id = case_id
        self.chat_id = chat_id
        self.category = category
        self.sender_id = sender_id
        self.message = message
        self.msg_date_time = msg_date_time

    def get_dict(self):
        """
        'get_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        
        datetime_column = ['msg_date_time']
        
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            if column in datetime_column:
                result['date'] = getattr(self, column).strftime("%Y-%m-%d")
                result['time'] = getattr(self, column).strftime("%H:%M:%S")
                
            else:
                result[column] = getattr(self, column)
            
        return result
    
    def update_columns(self, update_dict):
        """
        'update_columns' which updates the corresponding 
        key, value pair in the object instance
        """
        for column in update_dict:
            self[column] = update_dict[column]

# Retrieve all users
@app.route('/get_all_users', methods=['GET'])
def get_all_users():
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

    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while retrieving all users."
            }
        ), 404
        
# Retrieve all cases
@app.route('/get_all_cases', methods=['GET'])
def get_all_cases():
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

    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while retrieving all cases."
            }
        ), 404
        
# Retrieve all chats
@app.route('/get_all_chats', methods=['GET'])
def get_all_chats():
    try: 
        output = []
        chats_info = chats.query.all()

        for chat in chats_info:
            output.append(chat.get_dict())

        return jsonify(
            {
                "code": 200,
                "data": output
            }
        ), 200

    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while retrieving all chats."
            }
        ), 404

# Login APIs
# 1 ) a) Check if email is used b) create OTP
# 2 ) Create new user
# 3 ) a) check if name/password correct b) create OTP

# 1 ) a) Check if email is used b) create OTP
def read_template(filename):
    with open(filename) as f:
        template_content = f.read()

    return Template(template_content)

@app.route('/registration_scan', methods=['POST'])
def registration_scan():
    try:
        # retrieve data
        data = request.get_json()
        email = data['email']
        
        # check if email in users
        user_info = users.query.filter_by(email=email).first()
        
        if user_info:
            return jsonify(
                {
                    "code": 404,
                    "message": "There is an existing user with the same email."
                }
            ), 404
            
        # create OTP
        otp = random.randrange(100000, 1000000)
        
        # send to email
        
        # 1) login
        MY_ADDRESS = 'THE_Penteract@outlook.com' # input your address
        MY_PW = 'PenteractPassword' # input your password
        
        s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        s.starttls()
        s.login(MY_ADDRESS, MY_PW)
        
        # create message
        template_content = read_template('Email Templates/otp_registration.txt')        
        message = template_content.substitute(verification_code=otp)
        
        # send message
        msg = MIMEMultipart()
        
        msg['From'] = MY_ADDRESS
        msg['To'] = email
        msg['Subject'] = 'Penteract Verification Code'

        msg.attach(MIMEText(message, 'plain'))
        
        s.send_message(msg)
        del msg
        s.quit
        
        return jsonify(
            {
                "code": 200,
                "data": {
                    "otp": otp,
                    "user_id": user_obj_json['user_id'],
                    "name": user_obj_json['name']
                },
                "message": "Registration scan completed. Email is available."
            }
        ), 200
        
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while doing registration scan."
            }
        ), 404
    
# 2 ) Create new user
@app.route('/create_new_user_client', methods=['POST'])
def create_new_user_client():
    try:
        # retrieve data (email, name, bdae, last4_nric, password)
        data = request.get_json()
        
        # fill in missing data
        data['bdae'] = datetime.strptime(data['bdae'], '%Y-%m-%d')
        data['user_id'] = 0
        data['role'] = "client"
        data['educational_instituition'] = None
        data['study_year'] = None
        data['company'] = None
        data['position'] = None
        
        user_obj = users(**data)
        
        db.session.add(user_obj)
        db.session.commit()

        return jsonify(
            {
                "code": 200,
                "message": "Successfully created new user for client."
            }
        ), 200
    
        
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while creating new user for client."
            }
        ), 404
    
# 3 ) a) check if name/password correct b) create OTP
@app.route('/login', methods=['POST'])
def login():
    try:
        # retrieve data (email, password)
        data = request.get_json()
        
        email = data['email']
        password = data['password']
        
        # retrieve user_obj by email
        user_obj = users.query.filter_by(email=email).first()
        
        # check if email and password match
        validation_results = user_obj.validate_password(password)
        
        if not validation_results:
            return jsonify(
                {
                    "code": 404,
                    "message": "Invalid password"
                }
            ), 404
            
        # retrieve user_obj json
        user_obj_json = user_obj.get_dict()
            
        # create OTP
        otp = random.randrange(100000, 1000000)
        
        # send to email
        
        # 1) login
        MY_ADDRESS = 'THE_Penteract@outlook.com' # input your address
        MY_PW = 'PenteractPassword' # input your password
        
        s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        s.starttls()
        s.login(MY_ADDRESS, MY_PW)
        
        # create message
        template_content = read_template('Email Templates/otp_login.txt')        
        message = template_content.substitute(verification_code=otp)
        
        # send message
        msg = MIMEMultipart()
        
        msg['From'] = MY_ADDRESS
        msg['To'] = email
        msg['Subject'] = 'Penteract Verification Code'

        msg.attach(MIMEText(message, 'plain'))
        
        s.send_message(msg)
        del msg
        s.quit

        return jsonify(
            {
                "code": 200,
                "data": {
                    "otp": otp,
                    "user_id": user_obj_json['user_id'],
                    "name": user_obj_json['name']
                },
                "message": "Valid email and password"
            }
        ), 200
        
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 404,
                "message": "Incorrect email or password"
            }
        ), 404
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8100, debug=True)
