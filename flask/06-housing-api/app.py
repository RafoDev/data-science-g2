from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:1234@localhost/db_codigo"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Housing(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  rooms = db.Column(db.Integer, primary_key=True)
  price = db.Column(db.Double, primary_key=True)

  def __init__(self, rooms):
    self.rooms = rooms

db.create_all()

@app.route("/")
def index():
  context = {
    "message": "api v1.0"
  }
  return jsonify(context)