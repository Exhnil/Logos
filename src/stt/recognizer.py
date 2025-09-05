import whisper
import sounddevice as sd
import soundfile as sf
import numpy as np
import json
from scipy.signal import butter, lfilter
import logging

with open("src/stt/config.json","r") as f:
    CONFIG= json.load(f)

logger = logging.getLogger("LogosSTT")

logger.info(f"Loading Whisper model: {CONFIG['model']}")
model = whisper.load_model(CONFIG["model"])

filename = f"rec_{CONFIG['duration']}.wav"
device_info = sd.query_devices(sd.default.device[0])
CONFIG["samplerate"] = int(device_info["default_samplerate"])
logger.info(f"Samplerate: {CONFIG["samplerate"]} Hz, device: {device_info["name"]}")


def highpass_filter(audio, samplerate, cutoff=80, order=5):
    nyquist = 0.5 * samplerate
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype="high", analog=False)
    return lfilter(b, a, audio)


def preprocess(audio, samplerate):

    if audio.ndim > 1:
        audio = np.mean(audio, axis=1)

    max_val = np.max(np.abs(audio))
    if max_val > 0:
        audio = audio / max_val

    audio = highpass_filter(audio, samplerate)

    return audio.astype(np.float32)


def record_stream():
    frames = []

    def callback(indata, frames_count, time, status):
        if status:
            print("Status :", status)
        frames.append(indata.copy())

    logger.info("Listening...")

    with sd.InputStream(samplerate=CONFIG["samplerate"], channels=CONFIG["channels"], callback=callback):
        sd.sleep(int(CONFIG["duration"]*1000))

    logger.info("Recording done")

    audio = np.concatenate(frames, axis=0)
    audio = preprocess(audio, CONFIG["samplerate"])

    sf.write(filename, audio, CONFIG["samplerate"], subtype=CONFIG["subtype"])
    logger.info(f"{filename} saved")

    return filename


def listen():
    audio = record_stream()
    result = model.transcribe(audio, language=CONFIG["language"])
    logger.info(result["text"])
    return result["text"]
