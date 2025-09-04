import time
import speech_recognition as sr
import whisper
import sounddevice as sd
import soundfile as sf

model = whisper.load_model("small")

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I did not understand that."
        except sr.RequestError as e:
            return f"Could not request results; {e}"
    return

def record():

    samplerate = 16000
    channels=1
    frames=1024
    filename= "test.wav"
    duration=10

    print("Listening...")
    
    with sf.SoundFile(filename,mode="w",samplerate=samplerate,channels=channels) as file :
        with sd.InputStream(samplerate=samplerate,channels=channels) as stream:
            
            start_time=time.time()
            while time.time()-start_time<duration:
                data,overflowed = stream.read(frames)
                file.write(data)
            print("audio recorded")

    return filename

def listenWhisper():
    audio_path=record()
    result = model.transcribe(audio_path,language="fr")
    print(result["text"])
    return result["text"]