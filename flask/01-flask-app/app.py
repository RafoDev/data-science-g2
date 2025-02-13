from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
  return "<h1>Hola mundo desde Flask! 👽</h2>"

@app.route('/saludo')
def saludo():
  nombre = request.args.get("nombre", "")
  return f"<h1>Hola {nombre}!</h2>"

@app.route('/suma')
def suma():
  n1 = request.args.get("n1", "0")
  n2 = request.args.get("n2", "0")
  resultado = int(n1) + int(n2)
  return f"<h1>El resultado de la suma es {resultado}!</h2>"

app.run(debug=True)