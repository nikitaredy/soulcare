CRISIS_KEYWORDS = [
    "hurt myself",
    "kill myself",
    "end my life",
    "suicide",
    "don't want to live",
    "die",
    "self harm"
]

def is_crisis(text):
    text = text.lower()
    return any(word in text for word in CRISIS_KEYWORDS)
