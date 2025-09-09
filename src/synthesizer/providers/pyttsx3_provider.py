import pyttsx3

_engine = None


def init_tts(rate=150, volume=1.0):
    global _engine
    _engine = pyttsx3.init()
    voices = _engine.getProperty("voices")

    _engine.setProperty("rate", rate)
    _engine.setProperty("volume", volume)
    _engine.setProperty("voice", voices[1].id)


def speak(text: str):
    if _engine is None:
        init_tts()
    _engine.say(text)
    _engine.runAndWait()
