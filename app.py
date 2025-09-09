from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from database import init_db, insert_leave, insert_onboarding, insert_exit

app = Flask(__name__)
CORS(app)

init_db()  # Initialize DB on startup

@app.route('/')
def home():
    return "HR Chatbot Backend Running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    intent = req.get('queryResult').get('intent').get('displayName')

    params = req.get('queryResult').get('parameters')
    
    if intent == 'apply.leave':
        data = {
            'name': params.get('name'),
            'email': params.get('email'),
            'start_date': params.get('start_date'),
            'end_date': params.get('end_date'),
            'leave_type': params.get('leave_type')
        }
        insert_leave(data)
        return jsonify({'fulfillmentText': f"Leave request submitted for {data['name']} from {data['start_date']} to {data['end_date']}."})

    elif intent == 'start.onboarding':
        data = {
            'name': params.get('name'),
            'email': params.get('email'),
            'position': params.get('position'),
            'start_date': params.get('start_date')
        }
        insert_onboarding(data)
        return jsonify({'fulfillmentText': f"Onboarding started for {data['name']} joining as {data['position']} on {data['start_date']}."})

    elif intent == 'request.exit':
        data = {
            'name': params.get('name'),
            'email': params.get('email'),
            'exit_date': params.get('exit_date'),
            'reason': params.get('reason')
        }
        insert_exit(data)
        return jsonify({'fulfillmentText': f"Exit process started for {data['name']} effective {data['exit_date']}."})

    else:
        return jsonify({'fulfillmentText': "Sorry, I didn’t understand that."})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
