from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello, feature 1 and feature 2!</h1>'

@app.route('/sumar')
def sumar():
    param1 = 10
    param2 = 20
    return param1 + param2

@app.route('/multiplicar')
def multiplicar():
    param1 = 10
    param2 = 20
    return param1 * param2
