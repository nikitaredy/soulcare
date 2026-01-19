# 🧠 SoulCare

<div align="center">

**AI-Powered Mental Health Companion**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![NLP](https://img.shields.io/badge/NLP-Powered-green.svg)](https://en.wikipedia.org/wiki/Natural_language_processing)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

*Your compassionate AI companion for mental wellness and emotional support*

</div>

---

## 💙 Overview

**SoulCare** is an intelligent mental health chatbot application that leverages advanced Natural Language Processing (NLP) to provide empathetic, 24/7 emotional support and mental wellness guidance. Built with cutting-edge AI technology, SoulCare offers a safe, judgment-free space for users to express their feelings, manage stress, and improve their mental well-being.

Whether you're dealing with anxiety, stress, depression, or simply need someone to talk to, SoulCare is here to listen, understand, and support you on your mental health journey.

## ✨ Key Features

### 🤖 **Intelligent NLP Chatbot**
- Advanced natural language understanding to interpret emotions and context
- Empathetic, human-like conversational responses

### 🎯 **Mental Health Support**
- **Cognitive Behavioral Therapy (CBT)**: Evidence-based therapeutic approaches
- **Mindfulness & Meditation**: Guided relaxation exercises
- **Crisis Support**: Immediate resources and helpline information

### 🔒 **Privacy & Security**
- End-to-end encrypted conversations
- No personal data storage without consent

### 📊 **Personalized Insights**
- Emotion pattern analysis
- Mental health progress tracking

### 🌍 **Accessibility**
- 24/7 availability
- Multi-language support

## 🏗️ Architecture

```mermaid
graph TB
    A[User Interface] --> B[Chat Interface]
    B --> C[NLP Engine]
    C --> D[Intent Recognition]
    C --> E[Sentiment Analysis]
    C --> F[Entity Extraction]
    D --> G[Response Generator]
    E --> G
    F --> G
    G --> H[Therapeutic Response Module]
    H --> I[Mood Tracker]
    H --> J[Resource Library]
    H --> K[Crisis Detection]
    K --> L[Emergency Protocol]
    G --> M[Conversational AI]
    M --> B
```

## 🛠️ Tech Stack

### **Natural Language Processing**
- **NLP Framework**: spaCy / NLTK / Transformers
- **Sentiment Analysis**: VADER / TextBlob / Custom trained models
- **Intent Classification**: Rasa / Dialogflow / Custom NLU
- **Language Models**: BERT / GPT / BiLSTM networks

### **Backend**
- Python 3.8+
- FastAPI / Flask for REST API
- PostgreSQL / MongoDB for data storage
- Redis for session management

### **Frontend**
- React / Next.js
- TypeScript
- Tailwind CSS
- WebSocket for real-time chat

### **AI/ML Libraries**
- TensorFlow / PyTorch
- scikit-learn
- Hugging Face Transformers
- LangChain for conversation chains

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Node.js 16+ (for frontend)
- PostgreSQL or MongoDB
- pip and npm/yarn

### Installation

#### Backend Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/soulcare.git
   cd soulcare
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLP models:**
   ```bash
   python -m spacy download en_core_web_sm
   python scripts/download_models.py
   ```

5. **Configure environment variables:**
   
   Create a `.env` file in the root directory:
   ```env
   # Database
   DATABASE_URL=postgresql://user:password@localhost:5432/soulcare
   
   # API Keys
   OPENAI_API_KEY=your-openai-key
   
   # Security
   SECRET_KEY=your-secret-key
   JWT_SECRET=your-jwt-secret
   
   # NLP Configuration
   NLP_MODEL=en_core_web_sm
   SENTIMENT_MODEL=cardiffnlp/twitter-roberta-base-sentiment
   ```

6. **Initialize the database:**
   ```bash
   python manage.py migrate
   python manage.py init_db
   ```

7. **Run the backend server:**
   ```bash
   uvicorn main:app --reload
   # OR
   python app.py
   ```

   The API will be available at `http://localhost:8000`

#### Frontend Setup

1. **Navigate to the frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   # OR
   yarn install
   ```

3. **Configure environment:**
   
   Create `.env.local`:
   ```env
   NEXT_PUBLIC_API_URL=http://localhost:8000
   NEXT_PUBLIC_WS_URL=ws://localhost:8000/ws
   ```

4. **Run the development server:**
   ```bash
   npm run dev
   # OR
   yarn dev
   ```

   The app will be available at `http://localhost:3000`

## 💬 Usage

### Starting a Conversation

1. **Open the SoulCare app** in your browser
2. **Create an account** or continue anonymously
3. **Start chatting** with the AI companion
4. Share your feelings, thoughts, or concerns
5. Receive personalized support and guidance

### Example Interactions

```
User: "I've been feeling really anxious lately"
SoulCare: "I'm sorry to hear you're experiencing anxiety. That can be really 
challenging. Would you like to talk about what's been making you feel this way, 
or would you prefer some techniques to help manage the anxiety right now?"

User: "I can't sleep because I'm worried about work"
SoulCare: "Sleep difficulties due to work stress are very common. Let's work 
through this together. First, let's try a quick breathing exercise to help calm 
your mind. Are you in a comfortable position to try this?"
```

### Available Commands

- `/mood` - Track your current mood
- `/breathing` - Start a breathing exercise
- `/meditation` - Access guided meditation
- `/resources` - Get mental health resources
- `/crisis` - Access emergency support
- `/history` - View your conversation history
- `/help` - Get help using SoulCare

## 🧪 NLP Capabilities

### Emotion Detection
The chatbot can identify and respond to:
- Joy, Sadness, Anger, Fear, Surprise, Disgust
- Anxiety, Depression, Stress indicators
- Suicidal ideation (triggers crisis protocol)

### Intent Recognition
- Seeking advice
- Venting emotions
- Learning coping strategies
- Requesting resources
- Emergency situations

### Contextual Understanding
- Remembers conversation history
- Adapts responses based on user's emotional state
- Personalizes recommendations over time
- Detects topic shifts and follows user's lead

## 📊 Features in Detail

### Mood Tracking
- Daily mood check-ins
- Emotion intensity ratings (1-10)
- Visual mood history graphs
- Pattern identification and insights

### Therapeutic Techniques
- **CBT Exercises**: Thought challenging, cognitive restructuring
- **Mindfulness**: Body scans, present moment awareness
- **Breathing Techniques**: 4-7-8 breathing, box breathing
- **Journaling Prompts**: Gratitude, reflection, goal-setting

### Crisis Detection & Support
- Automatic detection of crisis language
- Immediate connection to crisis resources
- National suicide prevention hotline
- Local emergency services information
- Safety planning tools

## 🔐 Privacy & Ethics

SoulCare is committed to user privacy and ethical AI:

- ✅ **Confidential**: All conversations are encrypted and private
- ✅ **Transparent**: Clear about AI limitations and when to seek professional help
- ✅ **Non-diagnostic**: Does not diagnose or replace professional treatment
- ✅ **Consent-based**: Users control their data
- ✅ **Bias-aware**: Trained to be inclusive and culturally sensitive

### Important Disclaimer

**SoulCare is not a replacement for professional mental health care.** If you are experiencing a mental health crisis, please contact:
- **National Suicide Prevention Lifeline**: 988 (US)
- **Crisis Text Line**: Text HOME to 741741
- **International**: Find resources at findahelpline.com

## 📂 Project Structure

```
soulcare/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI application
│   │   ├── models/              # Database models
│   │   ├── api/                 # API routes
│   │   ├── nlp/
│   │   │   ├── intent_classifier.py
│   │   │   ├── sentiment_analyzer.py
│   │   │   ├── entity_extractor.py
│   │   │   └── response_generator.py
│   │   ├── chatbot/
│   │   │   ├── conversation_manager.py
│   │   │   ├── context_handler.py
│   │   │   └── memory.py
│   │   ├── therapy/
│   │   │   ├── mood_tracker.py
│   │   │   ├── cbt_engine.py
│   │   │   ├── mindfulness.py
│   │   │   └── crisis_detector.py
│   │   └── utils/
│   ├── tests/
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatInterface.tsx
│   │   │   ├── MoodTracker.tsx
│   │   │   └── ResourceLibrary.tsx
│   │   ├── pages/
│   │   ├── styles/
│   │   └── utils/
│   ├── package.json
│   └── .env.local
├── models/                       # Trained NLP models
├── data/                        # Training data
├── docs/                        # Documentation
├── scripts/                     # Utility scripts
└── README.md
```

## 🧪 Testing

Run the test suite:

```bash
# Backend tests
pytest tests/ -v

# NLP model evaluation
python scripts/evaluate_models.py

# Integration tests
pytest tests/integration/ -v
```

## 🤝 Contributing

We welcome contributions to make SoulCare better! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and development process.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Mental health professionals who provided guidance
- Open-source NLP community
- Users who trusted us with their mental health journey
- Research in AI ethics and mental health technology

## 📞 Support

- **Email**: support@soulcare.ai
- **Discord**: [Join our community](https://discord.gg/soulcare)
- **Documentation**: [docs.soulcare.ai](https://docs.soulcare.ai)
- **Issues**: [GitHub Issues](https://github.com/yourusername/soulcare/issues)

---

<div align="center">

**Built with ❤️ and compassion for mental wellness**

*Remember: You are not alone. Help is always available.*

🌟 **If SoulCare helped you, please consider starring this repo!** 🌟

</div>
