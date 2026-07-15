from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

conversation_history = [
    {
        "role": "system",
        "content": """
You are a friendly voice assistant.
Speak naturally like a human.
Keep answers under 20 words whenever possible.
Use conversational language.
Remember previous context.
Do not sound like a textbook.
Do not give long explanations.
"""
    }
]

def get_response(prompt):

    conversation_history.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=conversation_history,
        max_tokens=40,
    )

    answer = response.choices[0].message.content

    conversation_history.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    if len(conversation_history) > 11:
        conversation_history.pop(1)

    return answer