import joblib
import numpy as np
import sklearn
import os

class HousingModel: 
  def __init__(self):
    model_path = os.path.dirname(__file__)
    self.model = joblib.load(os.path.join(model_path,"housing_model.pkl"))
    self.scaler_x = joblib.load(os.path.join(model_path,"scaler_x.pkl"))
    self.scaler_y = joblib.load(os.path.join(model_path,"scaler_y.pkl"))

  def predict(self, rooms):
    rooms_scaled = self.scaler_x.transform(np.array([[rooms]]))
    prediction_scaled = self.model.predict(rooms_scaled)
    prediction = self.scaler_y.inverse_transform(prediction_scaled) * 1000
    prediction_result = round(prediction.item(),2)

    return prediction_result