from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql'\
    '+mysqlconnector://root@localhost:3306/penteract_db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)
CORS(app)

class chat(db.Model):
    __tablename__ = 'chat'

    chat_id = db.Column(db.Integer, nullable=False, primary_key=True)
    sender_id = db.Column(db.Integer, nullable=False)
    receiver_id = db.Column(db.Integer, nullable=False)
    message = db.Column(db.String(1500), nullable=False)
    msgDateTime = db.Column(db.String(100), nullable=False)
    case_id = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(100), nullable=False)

    def __init__(
        self,
        chat_id,
        sender_id,
        receiver_id,
        message,
        msgDateTime,
        case_id,
        category
    ):
        self.chat_id = chat_id
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.message = message
        self.msgDateTime = msgDateTime 
        self.case_id = case_id
        self.category = category

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

@app.route("/")
def hello():
    return "liveness probe!"

@app.route('/send_message', methods=['POST'])
def create_new_message():
    try:
        # retrieve post request data
        data = request.get_json()
        data['chat_id'] = 0
        data['msgDateTime'] = datetime.datetime.now()

        chat_details = chat(**data)

        db.session.add(chat_details)
        db.session.commit()

        return jsonify(
            {
                "code": 200,
                "message": "Message successfully sent!" 
            }
        ), 200

    except Exception:
        return jsonify(
            {
                "code": 404,
                "message": "Error occured while sending message."
            }
        ), 404
        
@app.route('/receive_message/<string:case_id>/<string:category>',methods=['GET'])
def get_message(case_id, category):
    try:
        output = []
        messages = chat.query.filter_by(case_id=case_id, category=category)
        
        for message in messages:
            output.append(message.get_dict())
            
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
                "message": "Error occured while retrieving messages"
            }
        ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
