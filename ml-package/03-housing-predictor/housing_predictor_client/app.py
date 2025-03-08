from housing_predictor.housing_predictor import HousingModel
from insurance_predictor.insurance_predictor import InsuranceModel

h_model = HousingModel()
rooms = 5
price = h_model.predict(rooms)

print(f"Para {rooms} cuartos el precio es: {price}")


i_model = InsuranceModel()
age = 12
costs = i_model.predict(age)

print(f"Para {age} años el costo es: {costs}")

