from flask import Flask, request, render_template
import joblib
import numpy as np
import sklearn

app = Flask(__name__)

model = joblib.load("ml-files/insurance.pkl")
scaler_x = joblib.load("ml-files/scaler_x.pkl")
scaler_y = joblib.load("ml-files/scaler_y.pkl")

@app.route('/', methods=["GET", "POST"])
def index():
  prediction = 0
  edad = 0
  if(request.method == "POST"):
  
    edad = int(request.form["edad"])
    edad_scaled = scaler_x.transform(np.array([edad]).reshape(-1,1))
    prediction_scaled = model.predict(edad_scaled)
    prediction = round(scaler_y.inverse_transform(prediction_scaled).item(),2)
    
  return render_template(
    "index.html", 
    prediction=prediction, 
    edad=edad)

app.run(debug=True)