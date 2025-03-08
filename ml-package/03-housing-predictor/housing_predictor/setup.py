from setuptools import setup, find_packages

setup(
  name="housing_predictor",
  version="1.0.0",
  description="Librería para predecir el precio de una casa.",
  author="RafoDev",
  author_email="rafaeldavid.dev@gmail.com",
  packages=find_packages(),
  include_package_data=True,
  package_data={
    "housing_predictor":["model/*"]
  },
  install_requires=[
    "joblib==1.4.2",
    "numpy==2.2.3",
    "scikit-learn==1.6.1"
  ]
)