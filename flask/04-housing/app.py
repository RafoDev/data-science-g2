from flask import Flask, request, render_template
import joblib
import numpy as np
import sklearn

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():

  prediction_result = 0

  if request.method == "POST":
    model = joblib.load("housing_model.pkl")
    scaler_x = joblib.load("scaler_x.pkl")
    scaler_y = joblib.load("scaler_y.pkl")

    rooms = int(request.form['rooms'])

    rooms_scaled = scaler_x.transform(np.array([[rooms]]))
    prediction_scaled = model.predict(rooms_scaled)
    prediction = scaler_y.inverse_transform(prediction_scaled) * 1000
    prediction_result = round(prediction.item(),2)

  return render_template("index.html", prediction=prediction_result)

app.run(debug=True)