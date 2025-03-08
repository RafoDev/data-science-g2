from insurance_predictor_model import InsuranceModel

ml_insurance = InsuranceModel()
costs = ml_insurance.predict(12)
print(costs)