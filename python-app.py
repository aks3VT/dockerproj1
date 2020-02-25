from flask import Flask
import json

app = Flask(__name__)
@app.route('/')
def home():
    return "Hello, World!"

@app.route('/greetings')
def hello():
    x = '{ "greetings":["Hello", "Greetings" ]}'
    greetings = json.loads(x)
    return greetings


