from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from ml_model import InsuranceModel

app = Flask(__name__)
app.app_context().push()

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:1234@localhost/db_codigo"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Insurance(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  age = db.Column(db.Integer, nullable=False)
  charges = db.Column(db.Double, nullable=True)

  def __init__(self, age):
    self.age = age

db.create_all()

ma = Marshmallow(app)
class InsuranceSchema(ma.Schema):
  class Meta:
    fields = ("id", "age", "charges")


@app.route("/")
def index():
  context = {
    "message": "api v1.0"
  }
  return jsonify(context)

@app.route("/insurance", methods=["POST"])
def set_data():
  age = request.json["age"]
  new_insurance = Insurance(age)

  hmodel = InsuranceModel()
  charges = hmodel.predict(age)
  new_insurance.charges = charges

  db.session.add(new_insurance)
  db.session.commit()

  data_schema = InsuranceSchema()

  context = {
    "status": True,
    "message": "New insurance created!",
    "content": data_schema.dump(new_insurance)
  }
  return jsonify(context)

@app.route('/insurance', methods=["GET"])
def get_data():
  data = Insurance.query.all()
  data_schema = InsuranceSchema(many=True)

  context = {
    "status": True,
    "message": "All the insurance data",
    "content": data_schema.dump(data)
  }

  return context

@app.route('/insurance/<id>')
def get_data_by_id(id):
  data = Insurance.query.get(id)
  data_schema = InsuranceSchema()

  context = {
    "status": True,
    "message": "Requested insurance",
    "content": data_schema.dump(data)
  }

  return context


@app.route("/insurance/<id>", methods=["PUT"])
def update_data(id):
  age = request.json["age"]

  updated_insurance = Insurance.query.get(id)
  updated_insurance.age = age
  hmodel = InsuranceModel()
  charges = hmodel.predict(age)
  updated_insurance.charges = charges
  db.session.commit()

  data_schema = InsuranceSchema()

  context = {
    "status": True,
    "message": "Insurance updated!",
    "content": data_schema.dump(updated_insurance)
  }
  return jsonify(context)

@app.route("/insurance/<id>", methods=["DELETE"])
def delete_data(id):

  deleted_insurance = Insurance.query.get(id)
  db.session.delete(deleted_insurance)
  db.session.commit()

  data_schema = InsuranceSchema()

  context = {
    "status": True,
    "message": "Insurance deleted!",
    "content": data_schema.dump(deleted_insurance)
  }
  return jsonify(context)