from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return "<h1>Hola mundo desde Flask! 👽</h2>"

app.run(debug=True)