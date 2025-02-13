from flask import Flask,request, render_template

app = Flask(__name__)

@app.route("/")
def index():
  author = request.args.get("author", "unknown")
  return render_template("index.html", author=author)

app.run(debug=True)