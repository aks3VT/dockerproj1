from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/greetings', methods=['GET'])
def get_greetings():
 return jsonify('Greetings')
