# 💙 SoulCare - Mental Wellness AI Chatbot

**Your safe space to talk and be heard.**

SoulCare is an AI-powered mental wellness chatbot that uses NLP (Natural Language Processing) to detect emotions, provide empathetic responses, and offer mental health support. Built with real machine learning models and designed with care.

---

## 🌟 Features

### 🧠 **Advanced NLP Capabilities**
- **Emotion Detection**: Uses DistilBERT transformer model to detect 6 emotions
  - Sadness
  - Joy
  - Love
  - Anger
  - Fear
  - Surprise
- **Sentiment Analysis**: Analyzes positive, negative, and neutral sentiments
- **Intent Classification**: Understands user intent (greeting, seeking help, sharing feelings, etc.)
- **Crisis Detection**: Automatically detects crisis keywords and provides emergency resources

### 💬 **Conversational Features**
- Natural, empathetic responses
- Multiple response variations for authentic conversation
- Context-aware replies based on emotion and intent
- Casual, supportive tone ("hey love", "babe", etc.)
- Session-based conversation memory

### 🎨 **Beautiful UI**
- Modern gradient design
- Smooth animations
- Typing indicators
- Emotion tags on messages
- Mobile-responsive
- Real-time backend status indicator

### 🔒 **Safety First**
- Crisis keyword detection
- Emergency helpline numbers (India & US)
- Immediate resource provision for at-risk users
- Non-judgmental safe space

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Modern web browser (Chrome, Firefox, Edge)

### Step 1: Clone/Download the Project
```bash
git clone <your-repo-url>
cd SOULCARE
```

### Step 2: Install Backend Dependencies
```bash
cd Backend
pip install -r requirements.txt
```

**Note**: First run will download the DistilBERT model (~250MB) automatically.

### Step 3: Start the Backend Server
```bash
python app.py
```

You should see:
```
🚀 Initializing Mental Wellness Chatbot Backend...
✅ Emotion model loaded successfully
✅ All components loaded!

🌟 Mental Wellness Chatbot Backend Running!
📡 Server: http://localhost:5000
💚 Ready to help and support
```

### Step 4: Open the Frontend
```bash
cd ../Frontend
# Double-click chat.html or open it in your browser
```

Or simply open `soulcare_chat.html` in any browser.

---

## 📁 Project Structure

```
SOULCARE/
├── Backend/
│   ├── app.py              # Main Flask application with NLP models
│   └── requirements.txt    # Python dependencies
│
└── Frontend/
    └── chat.html           # Complete chat interface (HTML + CSS + JS)
```

---

## 🛠️ Tech Stack

### Backend
- **Flask** - Web framework
- **Transformers** - Hugging Face transformers for DistilBERT
- **PyTorch** - Deep learning framework
- **Flask-CORS** - Cross-origin resource sharing

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling with gradients and animations
- **Vanilla JavaScript** - Fetch API for backend communication

### Machine Learning
- **DistilBERT** (`bhadresh-savani/distilbert-base-uncased-emotion`)
  - Pre-trained transformer model
  - Fine-tuned for emotion classification
  - 6 emotion classes with confidence scores

---

## 🔗 API Endpoints

### `POST /chat`
Send a message and get AI response with emotion analysis.

**Request:**
```json
{
  "message": "I'm feeling really anxious today",
  "session_id": "user_123"
}
```

**Response:**
```json
{
  "response": "it's okay to feel scared sometimes. you're safe right now, I promise.",
  "analysis": {
    "emotion": "fear",
    "confidence": 0.87,
    "sentiment": "negative",
    "intent": "sharing_feelings"
  },
  "crisis_detected": false,
  "timestamp": "2026-01-19T10:30:00"
}
```

### `GET /history/<session_id>`
Retrieve conversation history for a session.

### `GET /emotions/<session_id>`
Get emotion analytics and distribution over time.

### `GET /resources`
Get mental health resources and crisis helplines.

### `GET /health`
Health check endpoint to verify backend status.

### `GET /`
API information and available endpoints.

---

## 💡 Usage Examples

### Basic Conversation
```
User: "hey"
Bot: "hey! how's it going? 😊"

User: "I'm feeling stressed about work"
Bot: "I hear you. that sounds really hard. I'm here with you, no judgment at all."
[Emotion detected: fear (78%)]
```

### Crisis Detection
```
User: "I don't want to live anymore"
Bot: [Provides crisis resources immediately]
📞 India: 9152987821 (AASRA)
📞 US: 988 (Suicide & Crisis Lifeline)
💛 You matter. Your life matters. Please reach out.
```

### Positive Interaction
```
User: "I got the job!"
Bot: "omg yesss I'm so happy for you!! keep shining babe ✨"
[Emotion detected: joy (95%)]
```

---

## 🧪 Testing the Backend

### Test with Browser
Navigate to: `http://localhost:5000/health`

Expected response:
```json
{
  "status": "healthy",
  "model_loaded": true,
  "timestamp": "2026-01-19T10:00:00",
  "version": "2.0.0"
}
```

### Test with curl
```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "hello", "session_id": "test_123"}'
```

---

## 🎨 Customization

### Change Response Style
Edit `SOFT_RESPONSES` and `GREETING_RESPONSES` in `app.py`:
```python
GREETING_RESPONSES = [
    "hey! how's it going? 😊",
    "hii! what's up? how are you feeling today?",
    # Add your own responses here
]
```

### Modify Emotion Detection
The emotion model detects 6 emotions by default. To add custom emotion keywords for fallback mode, edit the `_fallback_predict` method in the `EmotionModel` class.

### Customize UI Colors
Edit the CSS gradient in `chat.html`:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Change Port
In `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Change 5000 to your port
```

In `chat.html`:
```javascript
const API_URL = 'http://localhost:5000';  // Update port here too
```

---

## 📊 NLP Model Details

### Emotion Detection Model
- **Name**: `bhadresh-savani/distilbert-base-uncased-emotion`
- **Architecture**: DistilBERT (Distilled BERT)
- **Training**: Fine-tuned on emotion classification dataset
- **Classes**: sadness, joy, love, anger, fear, surprise
- **Accuracy**: High confidence scores (0.0 - 1.0)
- **Fallback**: Keyword-based detection if model fails to load

### How It Works
1. User message is tokenized using DistilBERT tokenizer
2. Tokens are passed through the transformer model
3. Model outputs logits for each emotion class
4. Softmax converts logits to probabilities
5. Highest probability emotion is selected
6. Confidence score is returned

---

## 🔒 Privacy & Safety

### Data Handling
- Conversations stored in memory only (not persisted to disk)
- No user data is logged or saved permanently
- Session IDs are randomly generated client-side
- No personal information is collected

### Crisis Resources Included
**India:**
- AASRA: 9152987821
- Vandrevala Foundation: 1860-2662-345
- iCall: 9152987821

**United States:**
- Suicide & Crisis Lifeline: 988
- Crisis Text Line: Text HOME to 741741

**International:**
- Links to country-specific resources provided

---

## 🚨 Troubleshooting

### Backend won't start
**Problem**: `ModuleNotFoundError: No module named 'flask'`
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### Model download fails
**Problem**: Can't download DistilBERT model
**Solution**: Check internet connection, or model will use keyword fallback automatically

### CORS errors in browser
**Problem**: `Access to fetch blocked by CORS policy`
**Solution**: Ensure `Flask-CORS` is installed
```bash
pip install Flask-CORS
```

### Frontend can't connect
**Problem**: Status shows "Backend Offline"
**Solution**: 
1. Make sure backend is running (`python app.py`)
2. Check URL matches: `http://localhost:5000`
3. Try accessing `http://localhost:5000/health` directly in browser

### "hi is not defined" error
**Problem**: Old HTML file without JavaScript
**Solution**: Use the complete `chat.html` file provided, not old template

---

## 🌐 Deployment

### Development (Current Setup)
```bash
python app.py
```

### Production with Gunicorn
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Docker (Optional)
Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY Backend/requirements.txt .
RUN pip install -r requirements.txt
COPY Backend/ .
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

Build and run:
```bash
docker build -t soulcare .
docker run -p 5000:5000 soulcare
```

### Environment Variables
Create `.env` file:
```
FLASK_ENV=production
SECRET_KEY=your-secret-key
PORT=5000
```

---

## 🎯 Future Enhancements

### Planned Features
- [ ] Database integration (PostgreSQL/MongoDB)
- [ ] User authentication & profiles
- [ ] Multi-language support
- [ ] Voice input/output
- [ ] Mood tracking over time
- [ ] Personalized coping strategies
- [ ] Integration with professional therapist directory
- [ ] Mobile app (React Native)
- [ ] Advanced sentiment analysis
- [ ] Contextual follow-up questions

### Model Improvements
- [ ] Fine-tune on mental health specific dataset
- [ ] Multi-label emotion detection
- [ ] Emotion intensity scoring
- [ ] Conversation history context awareness
- [ ] Personalized response generation

---

## 📝 License

This project is created for educational and mental health support purposes. Feel free to use, modify, and distribute with attribution.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve SoulCare:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

## ⚠️ Disclaimer

**SoulCare is NOT a replacement for professional mental health care.**

This chatbot is designed to provide supportive conversation and emotional support, but it is not a substitute for therapy, counseling, or medical treatment. 

**If you or someone you know is in crisis:**
- Call emergency services (911 in US)
- Contact a crisis helpline immediately
- Reach out to a mental health professional
- Go to the nearest emergency room

SoulCare aims to be a supportive tool but cannot provide clinical diagnosis or treatment.

---

## 💖 Acknowledgments

- **Hugging Face** - For the transformers library and pre-trained models
- **Bhadresh Savani** - For the emotion classification model
- **Mental health community** - For inspiration and feedback
- **You** - For caring about mental wellness

---

## 📧 Contact & Support

For questions, issues, or feedback:
- Open an issue on GitHub
- Reach out to the development team
- Join our community discussions

---

## 🌟 Show Your Support

If SoulCare helped you or someone you know, please:
- ⭐ Star this repository
- 🔄 Share with others who might benefit
- 💬 Provide feedback for improvements
- 🤝 Contribute to make it better

**Together, we can make mental health support more accessible. 💙**

---

*Built with love for mental wellness* 💜

*Version 2.0.0 | Last Updated: January 2026*
