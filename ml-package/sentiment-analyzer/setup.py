from setuptools import setup, find_packages

setup(
  name="sentiment_analyzer",
  version="1.0.0",
  description="Librería para analizar sentimientos en texto.",
  author="RafoDev",
  author_email="rafaeldavid.dev@gmail.com",
  packages=find_packages(),
  include_package_data=True,
  package_data={
    "sentiment_analyzer":["../model/*"]
  },
  install_requires=[
    "transformers==4.49.0",
    "numpy==2.2.3",
    "torch==2.6.0"
  ]
)