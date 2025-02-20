from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.app_context().push()

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:1234@localhost/db_codigo"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Housing(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  rooms = db.Column(db.Integer, nullable=False)
  price = db.Column(db.Double, nullable=True)

  def __init__(self, rooms):
    self.rooms = rooms

db.create_all()

ma = Marshmallow(app)
class HousingSchema(ma.Schema):
  class Meta:
    fields = ("id", "rooms", "price")


@app.route("/")
def index():
  context = {
    "message": "api v1.0"
  }
  return jsonify(context)

@app.route("/housing", methods=["POST"])
def set_data():
  rooms = request.json["rooms"]
  new_housing = Housing(rooms)
  db.session.add(new_housing)
  db.session.commit()

  data_schema = HousingSchema()

  context = {
    "status": True,
    "message": "New housing created!",
    "content": data_schema.dump(new_housing)
  }
  return jsonify(context)

@app.route('/housing', methods=["GET"])
def get_data():
  data = Housing.query.all()
  data_schema = HousingSchema(many=True)

  context = {
    "status": True,
    "message": "All the housing data",
    "content": data_schema.dump(data)
  }

  return context

@app.route('/housing/<id>')
def get_data_by_id(id):
  data = Housing.query.get(id)
  data_schema = HousingSchema()

  context = {
    "status": True,
    "message": "Requested register",
    "content": data_schema.dump(data)
  }

  return context


@app.route("/housing/<id>", methods=["PUT"])
def update_data(id):
  rooms = request.json["rooms"]
  price = request.json["price"]

  updated_housing = Housing.query.get(id)
  updated_housing.rooms = rooms
  updated_housing.price = price
  db.session.commit()

  data_schema = HousingSchema()

  context = {
    "status": True,
    "message": "Housing updated!",
    "content": data_schema.dump(updated_housing)
  }
  return jsonify(context)