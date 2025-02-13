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

@app.route('/resta/<int:n1>/<int:n2>')
def resta(n1=0, n2=0):
  resultado = n1 - n2
  return f"<h1>El resultado de la resta es {resultado}!</h2>"

@app.route('/<ope>/<int:n1>/<int:n2>')
def operaciones(ope="nn", n1=0, n2=0):
  if ope == "suma":
    resultado = n1 + n2
  elif ope == "resta":
    resultado = n1 - n2
  elif ope == "multiplicacion":
    resultado = n1 * n2
  elif ope == "division":
    resultado = n1 / n2
  else:
    resultado = "nn"

  if resultado == "nn":
    return f"<h1>No se encontro la operacion: {ope}</h2>"   
  return f"<h1>El resultado de la {ope} es {resultado}!</h2>"

app.run(debug=True)