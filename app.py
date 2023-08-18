from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')

@app.route('/sumar')
def sumar():
    param1 = 10
    param2 = 20
    return param1 + param2

@app.route('/multiplicacion')
def multiplicacion():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return str(a*b)



  
def hello():
  return '<h1>Hello, feature1 and feature2!</h1>'
