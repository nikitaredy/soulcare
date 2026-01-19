from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

class EmotionModel:
    def __init__(self):
        self.model_name = "bhadresh-savani/distilbert-base-uncased-emotion"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
        self.labels = ["sadness", "joy", "love", "anger", "fear", "surprise"]

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True)
        outputs = self.model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1)
        label_id = torch.argmax(probs).item()
        confidence = probs[0][label_id].item()
        return self.labels[label_id], confidence
