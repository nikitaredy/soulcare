from fastapi import FastAPI
from pydantic import BaseModel
from model import EmotionModel
from crisis import is_crisis
from responder import generate_response, CRISIS_RESPONSE

app = FastAPI()
emotion_model = EmotionModel()

class Message(BaseModel):
    text: str

@app.post("/chat")
def chat(msg: Message):
    text = msg.text

    # Crisis Check
    if is_crisis(text):
        return {"reply": CRISIS_RESPONSE}

    # Emotion Detection
    emotion, confidence = emotion_model.predict(text)

    # Soft Response
    reply = generate_response(emotion, confidence)

    return {
        "emotion": emotion,
        "confidence": confidence,
        "reply": reply
    }
