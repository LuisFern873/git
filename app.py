from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')

def hello():
    return '<h1>Hello, feature 1!</h1>'

def sumar():
    param1 = 10
    param2 = 20
    return param1 + param2

def multiplicar():
    param1 = 10
    param2 = 20
    return param1 * param2