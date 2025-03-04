from analyzer.analyzer import SentimentAnalyzer

analyzer = SentimentAnalyzer()

text = "The product is excellent."

sentiment = analyzer.predict_sentiment(text)
print(f"{text} -> {sentiment}")