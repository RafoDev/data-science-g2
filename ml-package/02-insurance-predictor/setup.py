from setuptools import setup, find_packages

setup(
  name="insurance_predictor",
  version="1.0.0",
  description="Librería para predecir el costo del seguro dada una cierta edad.",
  author="RafoDev",
  author_email="rafaeldavid.dev@gmail.com",
  packages=find_packages(),
  include_package_data=True,
  package_data={
    "insurance_predictor":["model/*"]
  },
  install_requires=[
    "joblib==1.4.2",
    "numpy==2.2.3",
    "scikit-learn==1.6.1"
  ]
)