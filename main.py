import time
import threading

from stt import listen
from llm import get_response
from tts import speak
from fallback import get_filler


print("================================")
print("AI Voice Assistant Started")
print("Say 'exit' to quit")
print("================================")
speak("Hello. How can I help you today?")

empty_count = 0

while True:

    start = time.time()

    user_text = listen()

    if not user_text:

        empty_count += 1

        if empty_count >= 3:

            print("No speech detected.")
            speak("I cannot hear you.")

            empty_count = 0

        continue

    empty_count = 0

    if user_text.lower() in [
        "exit",
        "quit",
        "stop",
        "goodbye"
    ]:

        speak("Goodbye")
        print("Assistant stopped.")
        break

    print("Thinking...")

    answer_container = {"answer": None}

    def llm_task():
        answer_container["answer"] = get_response(user_text)

    thread = threading.Thread(target=llm_task)
    thread.start()

    filler_spoken = False

    while thread.is_alive():

        elapsed = time.time() - start

        if elapsed > 2 and not filler_spoken:
            speak(get_filler())
            filler_spoken = True

        time.sleep(0.1)

    answer = answer_container["answer"]

    print("\nAssistant:", answer)

    speak(answer)

    end = time.time()

    print("\n------ Latency Report ------")
    print(f"AI response time {end-start:.2f} sec")
    print("----------------------------\n")