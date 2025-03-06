from flask import Flask, request, jsonify
from sentiment_analyzer.sentiment_analyzer import SentimentAnalyzer

analyzer = SentimentAnalyzer()

app = Flask(__name__)

@app.route("/")
def index():
  context = {"message": "Sentiment Analysis API v1.0"}
  return jsonify(context)

@app.route("/sentiment", methods=["POST"])
def sentiment_analyzer():
  text = request.json['text']
  sentiment = analyzer.predict_sentiment(text)
  context = {"text": text, "sentiment": sentiment}

  return jsonify(context)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port="8000", debug=True)
