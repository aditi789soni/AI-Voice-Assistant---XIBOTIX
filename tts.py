import pyttsx3

def speak(text):

    engine = pyttsx3.init()

    engine.setProperty("rate", 170)

    print("SPEAKING:", text)

    engine.say(text)

    engine.runAndWait()

    engine.stop()