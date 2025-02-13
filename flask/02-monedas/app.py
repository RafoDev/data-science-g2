from flask import Flask,request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
  author = request.args.get("author", "unknown")

  monto_destino = 0

  if request.method == "POST":
    monto_origen = request.form["monto_origen"]
    monto_destino = round(int(monto_origen) / 3.7, 2)

  return render_template(
    "index.html", 
    author=author, 
    monto_destino=monto_destino)

app.run(debug=True)