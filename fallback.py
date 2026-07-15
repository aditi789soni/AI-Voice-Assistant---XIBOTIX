import random
from tts import speak
last_filler = ""

FILLERS = [
    "Hmm Let me think about that please Aditi.",
    "Thats a good question.I'm looking into that now Aditi",
    "Let me gather my thoughts.","That's a good question Aditi",
    "One moment Aditi please.","I'm working on it.",
    "Let me check that for you mate","Thinking through it now.",
    " I have an idea Aditi ","just a moment.",
    "Gotta Analyze the information Aditi.Let me find the best answer for you.",
    "Processing your request.Working on it now Aditi"
]


def get_filler():

    global last_filler

    available = [f for f in FILLERS if f != last_filler]

    filler = random.choice(available)

    last_filler = filler

    return filler