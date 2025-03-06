from flask import Flask, request, jsonify
from ml_model import HousingModel

app = Flask(__name__)

@app.route('/')
def index():

  context = {"message": "Api v1.0"}

  return jsonify(context)

@app.route('/housing', methods=["POST"])
def predict_price():
  hmodel = HousingModel() 
  rooms = request.json['rooms']
  price = hmodel.predict(rooms)
  validated_price = 0 if price < 0 else price

  context = {"rooms": rooms, "price": validated_price}

  return jsonify(context)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port="8000", debug=True)