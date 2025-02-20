import joblib
import numpy as np
import sklearn
import os

class InsuranceModel: 
  def __init__(self):
    model_path = os.path.dirname(__file__)
    self.model = joblib.load(os.path.join(model_path,"insurance.pkl"))
    self.scaler_x = joblib.load(os.path.join(model_path,"scaler_x.pkl"))
    self.scaler_y = joblib.load(os.path.join(model_path,"scaler_y.pkl"))

  def predict(self, edad):
    edad_scaled = self.scaler_x.transform(np.array([edad]).reshape(-1,1))
    prediction_scaled = self.model.predict(edad_scaled)
    prediction = round(self.scaler_y.inverse_transform(prediction_scaled).item(),2)
    return prediction