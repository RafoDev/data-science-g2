from insurance_predictor.insurance_predictor import InsuranceModel

model = InsuranceModel()
costs = model.predict(10)

print(costs)