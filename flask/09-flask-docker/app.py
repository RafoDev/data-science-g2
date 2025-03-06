from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def root():
  return jsonify({"message": "Api de prueba flask-docker"})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port="8000", debug=True)