from http import client
import json
from pydoc import cli
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import datetime

app = Flask(__name__)
cors = CORS(app)

@app.route('/chat', methods=['GET'])
def chat():
    return jsonify({
  "code": 200, 
  "data": [
    {
      "sender": "liyin", 
      "receiver": "amanda",
      "sender_role": "client",
      "sender_id": 5, 
      "receiver_id": 8, 
      "message": "Hi! I am liyin, your troublesome client for the day", 
      "timestamp": "Tue, 28 Jun 2022 20:32:38 GMT",
      "category": "sa-client"
    }, 
    {
        "sender": "amanda", 
        "receiver": "liyin",
        "sender_role": "amanda",
        "sender_id": 8, 
        "receiver_id": 5, 
        "message": "Hi Li Yin! Pls go away", 
        "timestamp": "Tue, 28 Jun 2022 20:35:38 GMT",
        "category": "sa-client"
    }, 
    {
        "sender": "liyin", 
        "receiver": "amanda",
        "sender_role": "client",
        "sender_id": 5, 
        "receiver_id": 8, 
        "message": "No.", 
        "timestamp": "Tue, 28 Jun 2022 20:40:38 GMT",
        "category": "sa-client"
    }
  ]
})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
