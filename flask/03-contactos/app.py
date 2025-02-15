from flask import Flask, render_template, url_for
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route("/")
def index():
  url = "https://randomuser.me/api/?results=10"
  lista_contactos = requests.get(url).json()
  return render_template("index.html", contactos=lista_contactos["results"])

@app.route("/hombres")
def hombres():
  url = "https://randomuser.me/api/?results=10&gender=male"
  lista_contactos = requests.get(url).json()
  return render_template("hombres.html", contactos=lista_contactos["results"])

@app.route("/mujeres")
def mujeres():
  url = "https://randomuser.me/api/?results=10&gender=female"
  lista_contactos = requests.get(url).json()
  return render_template("mujeres.html", contactos=lista_contactos["results"])

@app.route("/stats")
def stats():
  url = "https://randomuser.me/api/?results=100"
  data = requests.get(url).json()
  results = data['results']
  
  genders = [user["gender"] for user in results]
  ages = [user["dob"]["age"] for user in results]
  countries = [user["location"]["country"] for user in results]

  df_users = pd.DataFrame({
    "gender": genders,
    "age": ages,
    "country": countries,
  })
  df_users

  plt.figure(figsize=(6,6))
  sns.countplot(data=df_users, y="country", hue="gender")

  pathname = os.path.join("static", "images", "stats.png")
  plt.savefig(pathname)
  plt.close()

  return render_template("stats.html", graph_url = url_for("static", filename="images/stats.png"))


app.run(debug=True)