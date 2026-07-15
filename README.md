# AI Voice Assistant

## Project Overview

This project is a real-time Audio-In, Audio-Out Conversational AI Assistant developed using Python.
My laptop is Hp laptop with 8gm ram only so it takes more time hence i preferred online implementation.
The assistant accepts voice input from the user, converts speech into text, generates intelligent responses using the Groq Llama 3.1 8B Instant model, and provides spoken responses through text-to-speech. The system also supports conversation memory, latency monitoring, and fallback conversational responses to improve user experience.

---

## Features

- Voice Input using Speech Recognition
- Voice Output using Text-to-Speech
- Context-Aware Conversations
- Conversation History Memory
- Latency Monitoring
- Fallback Responses During Delays
- Multiple Exit Commands
- Natural Multi-Turn Conversations
- Modular Python Architecture

---

## Technology Stack

### Programming Language
- Python 3

### Speech-to-Text (STT)
- SpeechRecognition
- sounddevice
- Google Speech Recognition

### Large Language Model (LLM)
- Groq API
- Llama 3.1 8B Instant

### Text-to-Speech (TTS)
- pyttsx3

### Additional Libraries
- python-dotenv
- scipy
- threading
- tempfile

---

## Project Structure

```text
AI-Voice-Assistant/
│
├── main.py
├── llm.py
├── stt.py
├── tts.py
├── fallback.py
├── test_llm.py
├── test_stt.py
├── test_tts.py
├── requirements.txt
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/aditi789soni/AI-Voice-Assistant---XIBOTIX.git
cd AI-Voice-Assistant
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Environment File

Create a `.env` file in the project root directory:

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
DEEPGRAM_API_KEY=YOUR_DEEPGRAM_API_KEY
```

---

## Running the Application

Run the assistant using:

```bash
python main.py
```

The assistant will start listening for voice input and respond with synthesized speech.

---



## User Experience Features

- Natural voice-based interaction
- Context retention for follow-up questions
- Friendly fallback responses during delays
- Graceful handling of unclear or missing speech input
- Voice-based responses for hands-free interaction

---



## Author

** Aditi Soni**  
**Registration Number:**  24BDE0144
