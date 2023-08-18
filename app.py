from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')

@app.route('/suma')
def suma():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return str(a+b)

@app.route('/multiplicacion')
def multiplicacion():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return str(a*b)
def hello():
    return '<h1>Hello, feature2!</h1>'
