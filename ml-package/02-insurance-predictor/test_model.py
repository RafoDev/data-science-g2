from insurance_predictor.insurance_predictor import InsuranceModel

ml_insurance = InsuranceModel()
costs = ml_insurance.predict(10)
print(costs)