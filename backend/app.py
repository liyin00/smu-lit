from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
from datetime import date
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import pathlib

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
    bdae = db.Column(db.Date)
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
                if getattr(self, column):
                    result[column] = getattr(self, column).strftime("%Y-%m-%d")
                    
                else:
                    result[column] = None
                
            else:
                result[column] = getattr(self, column)
            
        return result
            
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
                    result[column] = None
                
            else:
                result[column] = getattr(self, column)
            
        return result
    
    def update_columns(self, update_dict):
        """
        'update_columns' which updates the corresponding 
        key, value pair in the object instance
        """
        if 'case_id' in update_dict:
            self.case_id = update_dict['case_id']

        if 'client_name' in update_dict:
            self.client_name = update_dict['client_name']

        if 'client_id' in update_dict:
            self.client_id = update_dict['client_id']

        if 'gross_salary' in update_dict:
            self.gross_salary = update_dict['gross_salary']

        if 'case_title' in update_dict:
            self.case_title = update_dict['case_title']

        if 'case_category' in update_dict:
            self.case_category = update_dict['case_category']

        if 'court_hearing_date' in update_dict:
            self.court_hearing_date = update_dict['court_hearing_date']

        if 'client_case_description' in update_dict:
            self.client_case_description = update_dict['client_case_description']

        if 's3_url' in update_dict:
            self.s3_url = update_dict['s3_url']

        if 'sa_id' in update_dict:
            self.sa_id = update_dict['sa_id']

        if 'lawyer_id' in update_dict:
            self.lawyer_id = update_dict['lawyer_id']

        if 'current_case_status' in update_dict:
            self.current_case_status = update_dict['current_case_status']

        if 'student_assigned_date' in update_dict:
            self.student_assigned_date = update_dict['student_assigned_date']

        if 'case_summary_date' in update_dict:
            self.case_summary_date = update_dict['case_summary_date']

        if 'finalised_case_summary_date' in update_dict:
            self.finalised_case_summary_date = update_dict['finalised_case_summary_date']

        if 'confirmed_appointment_date' in update_dict:
            self.confirmed_appointment_date = update_dict['confirmed_appointment_date']

        if 'consultation_date' in update_dict:
            self.consultation_date = update_dict['consultation_date']

        if 'consultation_questions' in update_dict:
            self.consultation_questions = update_dict['consultation_questions']

        if 'consultation_advices' in update_dict:
            self.consultation_advices = update_dict['consultation_advices']

        if 'client_summary_approval' in update_dict:
            self.client_summary_approval = update_dict['client_summary_approval']

        if 'pre_consult_req' in update_dict:
            self.pre_consult_req = update_dict['pre_consult_req']

        if 'pre_consult_google_docs_link' in update_dict:
            self.pre_consult_google_docs_link = update_dict['pre_consult_google_docs_link']

            
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
        if 'case_id' in update_dict:
            self.case_id = update_dict['case_id']
            
        if 'case_summary_id' in update_dict:
            self.case_summary_id = update_dict['case_summary_id']
            
        if 'summary_of_facts' in update_dict:
            self.summary_of_facts = update_dict['summary_of_facts']
            
        if 'issues_questions' in update_dict:
            self.issues_questions = update_dict['issues_questions']
            
        if 'applicable_law' in update_dict:
            self.applicable_law = update_dict['applicable_law']
            
        if 'court_hearing_matter' in update_dict:
            self.court_hearing_matter = update_dict['court_hearing_matter']
            
        if 'specific_questions' in update_dict:
            self.specific_questions = update_dict['specific_questions']
            
        if 'client_summary_feedback' in update_dict:
            self.client_summary_feedback = update_dict['client_summary_feedback']
            
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

# Retrieve all case summary
@app.route('/get_all_case_summary', methods=['GET'])
def get_all_case_summary():
    try: 
        output = []
        case_summary_info = case_summary.query.all()

        for case_summary_element in case_summary_info:
            output.append(case_summary_element.get_dict())

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
                "message": "Error occured while retrieving all case summaries."
            }
        ), 404
        
# Login APIs
# 1 ) a) Check if email is used b) create OTP
# 2 ) Create new user (client)
# 3 ) a) check if name/password correct b) create OTP
# 4 ) Create new user (sa)
# 5 ) Create new user (lawyer)
# 6 ) Retrieve user profile

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
        MY_ADDRESS = 'marcus.goh.2019@scis.smu.edu.sg' # input your address
        MY_PW = 'Pkl12345:)' # input your password
        
        s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        s.starttls()
        s.login(MY_ADDRESS, MY_PW)

        # create message
        message = """
        Dear Sir/Mdm,

        Your verification code is {}.
        Please enter this code to verify your email and complete the registration process.

        Kind regards,
        Penteract""".format(otp)
        
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
                    "otp": otp
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
    
# 2 ) Create new user (client)
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
                    "message": "Invalid password."
                }
            ), 404
            
        # retrieve user_obj json
        user_obj_json = user_obj.get_dict()
            
        # create OTP
        otp = random.randrange(100000, 1000000)
        
        # send to email
        
        # 1) login
        MY_ADDRESS = 'marcus.goh.2019@scis.smu.edu.sg' # input your address
        MY_PW = 'Pkl12345:)' # input your password
        
        s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        s.starttls()
        s.login(MY_ADDRESS, MY_PW)
        
        # create message
        message = """
        Dear Sir/Mdm,

        Your verification code is {}.
        Please enter this code to continue the login process.

        Kind regards,
        Penteract""".format(otp)
        
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
                "message": "Valid email and password."
            }
        ), 200
        
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 404,
                "message": "Incorrect email or password."
            }
        ), 404

# 4 ) Create new user (sa)
@app.route('/create_new_user_sa', methods=['POST'])
def create_new_user_sa():
    try:
        # retrieve data (email, name, educational_instituition, study_year, password)
        data = request.get_json()
        
        # fill in missing data
        data['last4_nric'] = None
        data['bdae'] = None
        data['user_id'] = 0
        data['role'] = "sa"
        data['company'] = None
        data['position'] = None
        
        user_obj = users(**data)
        
        db.session.add(user_obj)
        db.session.commit()

        return jsonify(
            {
                "code": 200,
                "message": "Successfully created new user for sa."
            }
        ), 200
    
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while creating new user for sa."
            }
        ), 404
        
# 5 ) Create new user (lawyer)
@app.route('/create_new_user_lawyer', methods=['POST'])
def create_new_user_lawyer():
    try:
        # retrieve data (email, name, company, position, password)
        data = request.get_json()
        
        # fill in missing data
        data['last4_nric'] = None
        data['bdae'] = None
        data['user_id'] = 0
        data['role'] = "lawyer"
        data['educational_instituition'] = None
        data['study_year'] = None
        
        user_obj = users(**data)
        
        db.session.add(user_obj)
        db.session.commit()

        return jsonify(
            {
                "code": 200,
                "message": "Successfully created new user for lawyer."
            }
        ), 200
    
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while creating new user for lawyer."
            }
        ), 404

# 6 ) Retrieve user profile
@app.route('/user_profile', methods=['POST'])
def user_profile():
    try:
        # retrieve data ()
        data = request.get_json()
        user_id = data['user_id']
        
        user_info = users.query.filter_by(user_id=user_id).first()
        
        return jsonify(
            {
                "code": 200,
                "data": user_info.get_dict()
            }
        ), 200

    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while retrieving user profile."
            }
        ), 404

# Case
# 1 ) Check if client created new case
# 2 ) Create new case
# 3 ) assign case to SA
# 4 ) SA does case summary
# 5 ) SA retrieve case summary
# 6 ) Retrieve a specific case
# 7 ) Retrieve cases by SA by case_status
# 8 ) Retrieve cases by lawyer by case_status
# 9 ) Retrieve case by client by case_status
# 10 ) Retrieve all cases by case_status
# 11 ) update client feedback

# 1 ) Check if client created new case
@app.route('/client_existing_case', methods=['POST'])
def client_existing_case():
    try:
        # retrieve data (client_id)
        data = request.get_json()
        client_id = data['client_id']

        # check if client_id exists in cases
        case_info = cases.query.filter_by(client_id=client_id).first()

        existing_case = False
        
        if case_info:
            existing_case = True
            
        return jsonify(
            {
                "code": 200,
                "existing_case": existing_case
            }
        ), 200
        
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while checking if client has an existing case."
            }
        ), 404
        
# 2 ) Create new case
@app.route('/create_case', methods=['POST'])
def create_case():
    try:
        # retrieve data (client_name, client_id, gross_salary, case_title, case_category, court_hearing_date, client_case_description, s3_url)
        data = request.get_json()
        
        data['court_hearing_date'] = datetime.strptime(data['court_hearing_date'], '%Y-%m-%d')
        data['current_case_status'] = "New Case"
        data['case_id'] = 0
        data['sa_id'] = None 
        data['lawyer_id'] = None 
        data['student_assigned_date'] = None 
        data['case_summary_date'] = None 
        data['finalised_case_summary_date'] = None 
        data['confirmed_appointment_date'] = None 
        data['consultation_date'] = None 
        data['consultation_questions'] = None 
        data['consultation_advices'] = None 
        data['client_summary_approval'] = None 
        data['pre_consult_req'] = None 
        data['pre_consult_google_docs_link'] = None
        
        case_obj = cases(**data)
        
        # add to database
        db.session.add(case_obj)
        db.session.commit()
        
        return jsonify(
            {
                "code": 200,
                "message": "Case successfully created."
            }
        ), 200
        
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while creating case."
            }
        ), 404

# 3 ) assign case to SA
@app.route('/assigning_case_to_SA', methods=['POST'])
def assigning_case_to_SA():
    try:
        # retrieve data (case_id, sa_id)
        data = request.get_json()
        
        # retrieve case_info
        case_id = data['case_id']
        case_info = cases.query.filter_by(case_id=case_id).first()

        case_info.update_columns({
            'student_assigned_date': date.today(),
            'current_case_status': 'Assigned cases',
            'sa_id': data['sa_id']
        })
        
        db.session.commit()
        
        return jsonify(
            {
                "code": 200,
                "message": "Successfully assigned case to SA."
            }
        ), 200
        
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while assigning case to SA."
            }
        ), 404

# 4 ) SA does case summary
@app.route('/create_case_summary', methods=['POST'])
def create_case_summary():
    try:
        # retrieve data (case_id, summary_of_facts, issues_questions, applicable_law, court_hearing_matter, specific_questions)
        data = request.get_json()
        case_id = data['case_id']
        case_obj = cases.query.filter_by(case_id=case_id).first()
        
        # create case summary instance
        data['case_summary_id'] = 0
        data['client_summary_feedback'] = None
        case_summary_obj = case_summary(**data)
        
        db.session.add(case_summary_obj)
        db.session.commit()
        
        # update case summary date
        case_obj.update_columns({
            "case_summary_date": date.today()
        })
        
        db.session.commit()
        
        return jsonify(
            {
                "code": 200,
                "message": "Successfully created case summary."
            }
        ), 200
        
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while creating case summary."
            }
        ), 404

# 5 ) SA retrieve case summary
@app.route('/get_case_summary', methods=['POST'])
def get_case_summary():
    try:
        # retrieve data (case_id)
        data = request.get_json()
        case_id = data['case_id']
        
        # retrieve info from cases
        cases_info = cases.query.filter_by(case_id=case_id).first()
        cases_info_json = cases_info.get_dict()
        
        # retrieve info from case summary
        case_summary_info = case_summary.query.filter_by(case_id=case_id)
        
        output = []
        
        for case_summary_element in case_summary_info:
            output.append(case_summary_element.get_dict())
        
        return jsonify(
            {
                "code": 200,
                "data": {
                    "case_summary": output[-1],
                    "case_summary_date": cases_info_json['case_summary_date'],
                    "finalised_case_summary_date": cases_info_json['finalised_case_summary_date']
                }
            }
        ), 200
        
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 404,
                "message": "Error occurred while retrieving case summary."
            }
        ), 404

# 6 ) Retrieve a specific case
@app.route('/get_specific_case', methods=['POST'])
def get_specific_case():
    try:
        # retrieve data (case_id)
        data = request.get_json()
        case_id = data['case_id']
        
        case_info = cases.query.filter_by(case_id=case_id).first()
        
        return jsonify(
            {
                "code": 200,
                "data": case_info.get_dict()
            }
        ), 200
        
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 404,
                "message": "Error occurred while retrieving specific case."
            }
        ), 404

# 7 ) Retrieve cases by SA by case_status
@app.route('/get_cases_by_sa', methods=['POST'])
def get_cases_by_sa():
    try:
        # retrieve data (sa_id)
        data = request.get_json()
        
        sa_id = data['sa_id']
        cases_info = cases.query.filter_by(sa_id=sa_id)
        
        output = {}
        
        for case in cases_info:
            case_data = case.get_dict()
            current_case_status = case_data['current_case_status']
            
            if current_case_status not in output:
                output[current_case_status] = []
                
            output[current_case_status].append(case_data)
            
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
                "message": "Error occured while retrieving cases by SA."
            }
        ), 404

# 8 ) Retrieve cases by lawyer by case_status
@app.route('/get_cases_by_lawyer', methods=['POST'])
def get_cases_by_lawyer():
    try:
        # retrieve data (lawyer_id)
        data = request.get_json()
        
        lawyer_id = data['lawyer_id']
        cases_info = cases.query.filter_by(lawyer_id=lawyer_id)
        
        output = {}
        
        for case in cases_info:
            case_data = case.get_dict()
            current_case_status = case_data['current_case_status']
            
            if current_case_status not in output:
                output[current_case_status] = []
                
            output[current_case_status].append(case_data)
            
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
                "message": "Error occured while retrieving cases by lawyer."
            }
        ), 404

# 9 ) Retrieve case by client by case_status
@app.route('/get_cases_by_client', methods=['POST'])
def get_cases_by_client():
    try:
        # retrieve data (client_id)
        data = request.get_json()
        
        client_id = data['client_id']
        cases_info = cases.query.filter_by(client_id=client_id)
        
        output = {}
        
        for case in cases_info:
            case_data = case.get_dict()
            current_case_status = case_data['current_case_status']
            
            if current_case_status not in output:
                output[current_case_status] = []
                
            output[current_case_status].append(case_data)
            
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
                "message": "Error occured while retrieving cases by client."
            }
        ), 404

# 10 ) Retrieve all cases by case_status
@app.route('/get_all_cases_admin', methods=['GET'])
def get_all_cases_admin():
    try:
        cases_info = cases.query.all()
        
        output = {}
        
        for case in cases_info:
            case_data = case.get_dict()
            current_case_status = case_data['current_case_status']
            
            if current_case_status not in output:
                output[current_case_status] = []
                
            output[current_case_status].append(case_data)
            
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
                "message": "Error occured while retrieving all cases by case status."
            }
        ), 404

# 11 ) update client feedback (last seen)
@app.route('/client_feedback', methods=['POST'])
def client_feedback():
    try:
        # retrieve data (case_id, client_summary_approval, client_summary_feedback)
        data = request.get_json()
        
        case_id = data['case_id']
        client_summary_approval = data['client_summary_approval']
        client_summary_feedback = data['client_summary_feedback']
        
        # update case_summary
        case_summary_info = case_summary.query.filter_by(case_id=case_id)[-1]
        case_summary_info.update_columns({
            "client_summary_feedback": client_summary_feedback
        })
        print(case_summary_info.get_dict())
        db.session.commit()
        
        # update case
        case_info = cases.query.filter_by(case_id=case_id).first()
        case_info.update_columns({
            "current_case_status": "Active",
            "finalised_case_summary_date": date.today(),
            "client_summary_approval": client_summary_approval
        })
        
        db.session.commit()
        
        return jsonify(
            {
                "code": 200,
                "message": "Successfully updated client feedback."
            }
        ), 200
        
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 404,
                "message": "Error occurred while updating client feedback."
            }
        ), 404

# Chat
# 1 ) retrieve chat message by case_id and category
# 2 ) create chat message

# 1 ) retrieve chat message by case_id and category
@app.route('/retrieve_chat', methods=['POST'])
def retrieve_chat():
    try:
        # retrieve data (case_id, category)
        data = request.get_json()
        
        case_id = data['case_id']
        category = data['category']
        
        chats_info = chats.query.filter_by(case_id=case_id, category=category)
        
        output = []
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
                "message": "Error occured while retrieving chats information."
            }
        ), 404

# 2 ) create chat message
@app.route('/create_chat_message', methods=['POST'])
def create_chat_message():
    try:
        # retrieve data (case_id, category, sender_id, message)
        data = request.get_json()
        
        data['chat_id'] = 0
        data['msg_date_time'] = datetime.today()
        
        chats_obj = chats(**data)
        
        db.session.add(chats_obj)
        db.session.commit()
        
        return jsonify(
            {
                "code": 200,
                "message": "Successfully created message in chat."
            }
        ), 200
        
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while creating message."
            }
        ), 404

# User profile
# 1 ) Retrieve user information by user_id
@app.route('/get_user_profile', methods=['POST'])
def get_user_profile():
    try:
        # retrieve data (user_id)
        data = request.get_json()
        user_id = data['user_id']
        
        user_info = users.query.filter_by(user_id=user_id).first()

        return jsonify(
            {
                "code": 200,
                "data": user_info.get_dict()
            }
        ), 200
        
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 404,
                "message": "Error occurred while retrieving user profile."
            }
        ), 404
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8100, debug=True)

# template
@app.route('/template', methods=['POST'])
def template():
    try:
        # retrieve data ()
        data = request.get_json()
        
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 404,
                "message": ""
            }
        ), 404