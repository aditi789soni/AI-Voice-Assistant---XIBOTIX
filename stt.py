import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import tempfile

def listen():

    fs = 16000
    duration = 3

    print("\nListening... Speak now.")

    recording = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=1,
        dtype='int16'
    )

    sd.wait()

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:

        write(f.name, fs, recording)

        recognizer = sr.Recognizer()

        with sr.AudioFile(f.name) as source:
            audio = recognizer.record(source)

    try:

        text = recognizer.recognize_google(audio)

        print("You said:", text)

        return text

    except sr.UnknownValueError:

        print("Didn't catch that.")

        return ""

    except Exception as e:

        print("Recognition error:", e)

        return ""