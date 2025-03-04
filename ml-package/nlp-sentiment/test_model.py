from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

path = "./model"

tokenizer = AutoTokenizer.from_pretrained(path)
model = AutoModelForSequenceClassification.from_pretrained(path)

def predict_sentiment(texts, model, tokenizer):
  device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
  model = model.to(device)

  inputs = tokenizer(texts, return_tensors="pt", truncation=True, padding=True, max_length=512)
  
  input_ids = inputs["input_ids"].to(device)
  attention_mask = inputs["attention_mask"].to(device)

  with torch.no_grad():
    outputs = model(input_ids=input_ids, attention_mask=attention_mask)
  
  probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
  sentiment_labels = {0: "Muy negativo", 1:"Negativo", 2:"Neutral", 3: "Positivo", 4:"Muy positivo"}
  return [sentiment_labels[p] for p in torch.argmax(probabilities, dim=-1).tolist()]

texts = [ "I absolutely love the new design of this app!"]

for text, sentiment in zip(texts, predict_sentiment(texts, model, tokenizer)):
  print(f"{text} -> {sentiment}")