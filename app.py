from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')

def hello():
    return '<h1>Hello, feature 1 and feature 2!</h1>'

