import torch
import numpy as np
import os

from transformers import AutoTokenizer, AutoModelForSequenceClassification

class SentimentAnalyzer:
  def __init__(self):
    model_path = os.path.join(os.path.dirname(__file__), "../model")
    self.tokenizer = AutoTokenizer.from_pretrained(model_path)
    self.model = AutoModelForSequenceClassification.from_pretrained(model_path)
    self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

  def predict_sentiment(self, text):
    self.model = self.model.to(self.device)

    input = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    
    input_ids = input["input_ids"].to(self.device)
    attention_mask = input["attention_mask"].to(self.device)

    with torch.no_grad():
      outputs = self.model(input_ids=input_ids, attention_mask=attention_mask)
    
    probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
    sentiment_labels = {0: "Muy negativo", 1:"Negativo", 2:"Neutral", 3: "Positivo", 4:"Muy positivo"}
    return sentiment_labels[torch.argmax(probabilities, dim=-1).item()]

text = "I absolutely love the new design of this app!"
analyzer = SentimentAnalyzer()
sentiment = analyzer.predict_sentiment(text)
print(f"{text} -> {sentiment}")