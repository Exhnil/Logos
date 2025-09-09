from synthesizer.providers import pyttsx3_provider
from synthesizer.providers.kokoro_provider import KokoroProvider
import logging

logger = logging.getLogger("LogosSynthetizer")


class Synthesizer:

    def __init__(self, voice: str, speed: float):
        self.kokoro = KokoroProvider(voice=voice, speed=speed)

    def speak(self, text: str):
        self.kokoro.synthesize_play(text)

    def stop(self):
        self.kokoro.stop_audio()
