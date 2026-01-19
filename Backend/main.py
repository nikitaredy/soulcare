from fastapi import FastAPI
from pydantic import BaseModel
from model import generate_reply

app = FastAPI()

class Message(BaseModel):
    user_message: str

@app.post("/chat")
def chat(message: Message):
    user_text = message.user_message

    soulcare_prompt = (
        "You are SoulCare, a soft, gentle, extremely supportive mental-health friend.\n"
        "Your tone is calming, patient, warm, and Gen-Z relatable.\n"
        "User: " + user_text + "\nSoulCare:"
    )

    reply = generate_reply(soulcare_prompt)
    return {"reply": reply}
