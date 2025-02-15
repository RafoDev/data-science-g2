import joblib
import numpy as np
import sklearn

model = joblib.load("housing_model.pkl")
scaler_x = joblib.load("scaler_x.pkl")
scaler_y = joblib.load("scaler_y.pkl")

rooms = 7

rooms_scaled = scaler_x.transform(np.array([[rooms]]))
prediction_scaled = model.predict(rooms_scaled)
prediction = scaler_y.inverse_transform(prediction_scaled) * 1000

print(prediction)