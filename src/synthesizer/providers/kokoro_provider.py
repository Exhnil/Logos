import sounddevice as sd
from kokoro import KPipeline


class KokoroProvider:
    def __init__(
        self, lang_code: str = "a", voice: str = "am_adam", speed: float = 1.0
    ):
        self.pipieline = KPipeline(lang_code=lang_code)
        self.voice = voice
        self.speed = speed
        self.current_audio_stream = None

    def stop_audio(self):
        if self.current_audio_stream:
            sd.stop()
            self.current_audio_stream = None

    def synthesize_play(self, text: str):
        self.stop_audio()
        generator = self.pipieline(text, voice=self.voice, speed=self.speed)

        for _, _, audio in generator:
            sd.play(audio, 24000)
            self.current_audio_stream = sd.get_stream()
            while self.current_audio_stream.active:
                pass
