from vosk import Model, KaldiRecognizer
import sounddevice as sd
import json

model = Model(r"C:\vosk-model-en-us-0.22")
rec = KaldiRecognizer(model, 16000)

def callback(indata, frames, time, status):
    if rec.AcceptWaveform(indata):
        result = json.loads(rec.Result())
        text = result["text"]
        print(" Heard:", text)
        with open("command.txt", "w") as f:
            f.write(text)

with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    print("Sync completed")
    while True:
        pass

