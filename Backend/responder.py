import random

SOFT_RESPONSES = {
    "sadness": [
        "hey love… I’m really sorry you're feeling like this. you don’t have to go through it alone.",
        "breathe for a sec babe… I’m right here with you.",
    ],
    "fear": [
        "it’s okay to feel scared sometimes. you’re safe right now, I promise.",
        "I’m here with you… you’re not facing this alone.",
    ],
    "anger": [
        "your feelings are valid, babe. it’s okay to let it out.",
        "I hear you, and I’m not judging at all.",
    ],
    "joy": [
        "omg yesss I’m so happy for you!! keep shining babe ✨",
        "that’s so cute, I’m proud of you!",
    ],
    "love": [
        "aww that’s so wholesome… sending you warm vibes 🤍",
        "you deserve softness, truly.",
    ],
    "surprise": [
        "whoa that sounds intense! want to tell me more?",
        "wait omg?? tell me what happened.",
    ]
}

CRISIS_RESPONSE = """
hey… I’m really sorry you’re in this much pain.  
I’m here with you, but I can’t help in an emergency.  
please reach out to someone who can support you right now:

📞 Suicide Prevention Hotline (India): 9152987821  
💛 You deserve help, love, and safety.
"""

def generate_response(emotion, confidence):
    responses = SOFT_RESPONSES.get(emotion, SOFT_RESPONSES["sadness"])
    return random.choice(responses)
