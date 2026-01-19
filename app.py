from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import random
from datetime import datetime
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

app = Flask(__name__)
CORS(app)

# ==================== ML EMOTION MODEL ====================

class EmotionModel:
    def __init__(self):
        try:
            self.model_name = "bhadresh-savani/distilbert-base-uncased-emotion"
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
            self.labels = ["sadness", "joy", "love", "anger", "fear", "surprise"]
            self.model_loaded = True
            print("✅ Emotion model loaded successfully")
        except Exception as e:
            print(f"⚠️ Could not load emotion model: {e}")
            print("Falling back to keyword-based detection")
            self.model_loaded = False

    def predict(self, text):
        if not self.model_loaded:
            return self._fallback_predict(text)
        
        try:
            inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
            outputs = self.model(**inputs)
            probs = torch.softmax(outputs.logits, dim=1)
            label_id = torch.argmax(probs).item()
            confidence = probs[0][label_id].item()
            return self.labels[label_id], confidence
        except Exception as e:
            print(f"Error in prediction: {e}")
            return self._fallback_predict(text)
    
    def _fallback_predict(self, text):
        """Fallback keyword-based emotion detection"""
        text_lower = text.lower()
        emotions = {
            'sadness': ['sad', 'depressed', 'down', 'unhappy', 'miserable', 'crying'],
            'joy': ['happy', 'excited', 'great', 'awesome', 'amazing', 'wonderful'],
            'anger': ['angry', 'mad', 'furious', 'annoyed', 'frustrated', 'hate'],
            'fear': ['scared', 'afraid', 'anxious', 'worried', 'nervous', 'panic'],
            'love': ['love', 'care', 'adore', 'appreciate', 'grateful', 'thankful'],
            'surprise': ['wow', 'omg', 'shocked', 'surprised', 'unexpected']
        }
        
        for emotion, keywords in emotions.items():
            if any(word in text_lower for word in keywords):
                return emotion, 0.7
        
        return 'sadness', 0.5


# ==================== CRISIS DETECTION ====================

CRISIS_KEYWORDS = [
    "hurt myself", "kill myself", "end my life", "suicide",
    "don't want to live", "die", "self harm", "not worth living",
    "end it all", "give up on life", "better off dead"
]

def is_crisis(text):
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in CRISIS_KEYWORDS)


# ==================== RESPONSE GENERATOR ====================

SOFT_RESPONSES = {
    "sadness": [
        "hey love… I'm really sorry you're feeling like this. you don't have to go through it alone.",
        "breathe for a sec babe… I'm right here with you.",
        "I'm so sorry you're going through this. your feelings are valid and I'm here to listen.",
        "that sounds really hard. I'm here with you, no judgment at all.",
        "sending you so much love right now. you're not alone in this 💙"
    ],
    "fear": [
        "it's okay to feel scared sometimes. you're safe right now, I promise.",
        "I'm here with you… you're not facing this alone.",
        "anxiety can be overwhelming, but you've got this. let's take it one breath at a time.",
        "I hear you. those fears are valid. want to talk about what's worrying you?",
        "you're so brave for sharing this. I'm right here with you 🤍"
    ],
    "anger": [
        "your feelings are valid, babe. it's okay to let it out.",
        "I hear you, and I'm not judging at all.",
        "it's totally okay to feel angry. let's talk through what's bothering you.",
        "you have every right to feel this way. I'm listening.",
        "anger is a valid emotion. what's making you feel this way?"
    ],
    "joy": [
        "omg yesss I'm so happy for you!! keep shining babe ✨",
        "that's so cute, I'm proud of you!",
        "love this energy!! tell me more about what's making you happy!",
        "this is amazing!! you deserve all the good vibes 🌟",
        "yesss!! I'm here for this positive energy! what else is going well?"
    ],
    "love": [
        "aww that's so wholesome… sending you warm vibes 🤍",
        "you deserve softness, truly.",
        "this is so sweet. love seeing you appreciate the good things 💕",
        "your heart is beautiful. thank you for sharing this with me.",
        "gratitude looks good on you babe ✨"
    ],
    "surprise": [
        "whoa that sounds intense! want to tell me more?",
        "wait omg?? tell me what happened.",
        "okay wow!! that's unexpected. how are you feeling about it?",
        "no way!! tell me everything!",
        "that's wild! what's going through your mind right now?"
    ]
}

# Greeting responses for basic conversation
GREETING_RESPONSES = [
    "hey! how's it going? 😊",
    "hii! what's up? how are you feeling today?",
    "hey there! good to see you. how've you been?",
    "heyyy! how are things with you?",
    "hi! I'm here for you. what's on your mind today?",
    "hey! nice to hear from you. how's your day going?",
    "heyy! how are you doing? 💙"
]

FAREWELL_RESPONSES = [
    "take care babe! I'm always here if you need me 💜",
    "bye! remember to be kind to yourself today ✨",
    "see you! you've got this 💪",
    "later! come back anytime you need to talk 🤍",
    "goodbye! sending you good vibes 🌟"
]

CRISIS_RESPONSE = """hey… I'm really sorry you're in this much pain.  
I'm here with you, but I need you to reach out to someone who can help right now.

📞 India: 9152987821 (AASRA)
📞 US: 988 (Suicide & Crisis Lifeline)
📞 Text HOME to 741741 (Crisis Text Line)

💛 You matter. Your life matters. Please reach out.
You deserve help, love, and safety."""

def generate_response(emotion, confidence, is_crisis_msg=False, intent=None):
    if is_crisis_msg:
        return CRISIS_RESPONSE
    
    # Handle greetings
    if intent == 'greeting':
        return random.choice(GREETING_RESPONSES)
    
    # Handle farewells
    if intent == 'farewell':
        return random.choice(FAREWELL_RESPONSES)
    
    # Emotion-based responses
    responses = SOFT_RESPONSES.get(emotion, SOFT_RESPONSES["sadness"])
    return random.choice(responses)


# ==================== SENTIMENT ANALYZER ====================

class SentimentAnalyzer:
    def analyze(self, text):
        text_lower = text.lower()
        
        positive_words = {'happy', 'joy', 'excited', 'great', 'good', 'wonderful', 
                         'amazing', 'love', 'excellent', 'better', 'proud'}
        negative_words = {'sad', 'depressed', 'anxious', 'worried', 'scared', 
                         'angry', 'hurt', 'pain', 'terrible', 'awful'}
        
        words = set(re.findall(r'\b\w+\b', text_lower))
        pos = len(words & positive_words)
        neg = len(words & negative_words)
        
        total = pos + neg
        if total == 0:
            return {'sentiment': 'neutral', 'score': 0.0}
        
        score = (pos - neg) / total
        
        if score > 0.3:
            sentiment = 'positive'
        elif score < -0.3:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        
        return {'sentiment': sentiment, 'score': score}


# ==================== INTENT CLASSIFIER ====================

class IntentClassifier:
    def __init__(self):
        self.intents = {
            'greeting': ['hello', 'hi', 'hey', 'good morning', 'good evening', 'sup', 'yo'],
            'farewell': ['bye', 'goodbye', 'see you', 'take care', 'gotta go', 'later'],
            'gratitude': ['thank', 'thanks', 'grateful', 'appreciate'],
            'seeking_help': ['help', 'need', 'don\'t know', 'struggling', 'difficult'],
            'sharing_feelings': ['feel', 'feeling', 'emotion', 'mood'],
        }
    
    def classify(self, text):
        text_lower = text.lower()
        scores = {}
        
        for intent, keywords in self.intents.items():
            score = sum(1 for keyword in keywords if keyword in text_lower)
            if score > 0:
                scores[intent] = score
        
        return max(scores, key=scores.get) if scores else 'general'


# ==================== CONVERSATION MEMORY ====================

class ConversationMemory:
    def __init__(self):
        self.conversations = {}
    
    def add_message(self, session_id, role, message, analysis=None):
        if session_id not in self.conversations:
            self.conversations[session_id] = {
                'messages': [],
                'started_at': datetime.now().isoformat(),
                'emotion_timeline': []
            }
        
        entry = {
            'role': role,
            'message': message,
            'timestamp': datetime.now().isoformat()
        }
        
        if analysis:
            entry['analysis'] = analysis
            if 'emotion' in analysis:
                self.conversations[session_id]['emotion_timeline'].append(analysis['emotion'])
        
        self.conversations[session_id]['messages'].append(entry)
    
    def get_history(self, session_id, limit=10):
        if session_id not in self.conversations:
            return []
        return self.conversations[session_id]['messages'][-limit:]
    
    def get_emotion_pattern(self, session_id):
        if session_id not in self.conversations:
            return []
        return self.conversations[session_id]['emotion_timeline']


# ==================== INITIALIZE COMPONENTS ====================

print("🚀 Initializing Mental Wellness Chatbot Backend...")
emotion_model = EmotionModel()
sentiment_analyzer = SentimentAnalyzer()
intent_classifier = IntentClassifier()
conversation_memory = ConversationMemory()
print("✅ All components loaded!")


# ==================== API ENDPOINTS ====================

@app.route('/chat', methods=['POST'])
def chat():
    """Main chat endpoint with ML emotion detection"""
    try:
        data = request.json
        user_message = data.get('message', '')
        session_id = data.get('session_id', 'default')
        
        if not user_message.strip():
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        # Crisis check first
        crisis_detected = is_crisis(user_message)
        
        if crisis_detected:
            response = CRISIS_RESPONSE
            analysis = {
                'emotion': 'crisis',
                'confidence': 1.0,
                'sentiment': 'crisis',
                'intent': 'seeking_help'
            }
        else:
            # Run all analysis
            emotion, confidence = emotion_model.predict(user_message)
            sentiment = sentiment_analyzer.analyze(user_message)
            intent = intent_classifier.classify(user_message)
            
            # Generate response with intent awareness
            response = generate_response(emotion, confidence, crisis_detected, intent)
            
            analysis = {
                'emotion': emotion,
                'confidence': round(confidence, 2),
                'sentiment': sentiment['sentiment'],
                'intent': intent
            }
        
        # Store in memory
        conversation_memory.add_message(session_id, 'user', user_message, analysis)
        conversation_memory.add_message(session_id, 'bot', response)
        
        return jsonify({
            'response': response,
            'analysis': analysis,
            'crisis_detected': crisis_detected,
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        print(f"Error in /chat: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/history/<session_id>', methods=['GET'])
def get_history(session_id):
    """Get conversation history"""
    limit = request.args.get('limit', 10, type=int)
    history = conversation_memory.get_history(session_id, limit)
    return jsonify({'history': history})


@app.route('/emotions/<session_id>', methods=['GET'])
def get_emotion_pattern(session_id):
    """Get emotion timeline for analytics"""
    emotions = conversation_memory.get_emotion_pattern(session_id)
    
    emotion_counts = {}
    for emotion in emotions:
        emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1
    
    return jsonify({
        'emotion_timeline': emotions,
        'emotion_distribution': emotion_counts
    })


@app.route('/resources', methods=['GET'])
def get_resources():
    """Mental health resources"""
    resources = {
        'crisis_lines': {
            'india': [
                {'name': 'AASRA', 'number': '9152987821', 'available': '24/7'},
                {'name': 'Vandrevala Foundation', 'number': '1860-2662-345', 'available': '24/7'},
                {'name': 'iCall', 'number': '9152987821', 'available': 'Mon-Sat 8am-10pm'}
            ],
            'us': [
                {'name': 'Suicide & Crisis Lifeline', 'number': '988', 'available': '24/7'},
                {'name': 'Crisis Text Line', 'text': 'HOME to 741741', 'available': '24/7'}
            ]
        },
        'coping_techniques': [
            '🌬️ 4-4-4 Breathing: Inhale 4 sec, hold 4 sec, exhale 4 sec',
            '🖐️ 5-4-3-2-1 Grounding: Name 5 things you see, 4 you touch, 3 you hear, 2 you smell, 1 you taste',
            '📝 Journal your thoughts without judgment',
            '🚶 Take a mindful walk, focus on each step',
            '💧 Drink cold water slowly and mindfully',
            '🎵 Listen to calming music or nature sounds'
        ],
        'self_care': [
            '😴 Maintain regular sleep (7-9 hours)',
            '🥗 Eat nutritious meals, stay hydrated',
            '🏃 Move your body daily, even just 10 min',
            '📱 Take social media breaks',
            '💙 Set healthy boundaries with others',
            '🙏 Practice daily gratitude'
        ]
    }
    return jsonify(resources)


@app.route('/health', methods=['GET'])
def health():
    """Health check"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': emotion_model.model_loaded,
        'timestamp': datetime.now().isoformat(),
        'version': '2.0.0'
    })


@app.route('/', methods=['GET'])
def home():
    """Home endpoint"""
    return jsonify({
        'message': 'Mental Wellness Chatbot API',
        'version': '2.0.0',
        'endpoints': {
            'POST /chat': 'Send a message',
            'GET /history/<session_id>': 'Get chat history',
            'GET /emotions/<session_id>': 'Get emotion analytics',
            'GET /resources': 'Get mental health resources',
            'GET /health': 'Health check'
        }
    })


# ==================== RUN SERVER ====================

if __name__ == '__main__':
    print("\n🌟 Mental Wellness Chatbot Backend Running!")
    print("📡 Server: http://localhost:5000")
    print("💚 Ready to help and support\n")
    app.run(debug=True, host='0.0.0.0', port=5000)