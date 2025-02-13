from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
  url = "https://randomuser.me/api/?results=10"
  lista_contactos = requests.get(url).json()
  return render_template("index.html", contactos=lista_contactos["results"])

@app.route("/hombres")
def hombres():
  return render_template("hombres.html")

app.run(debug=True)