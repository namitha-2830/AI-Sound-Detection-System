import sounddevice as sd
import numpy as np
import librosa
from tensorflow.keras.models import load_model

model = load_model("saved_model/my_model.h5")

classes = ["alarm", "clap", "doorbell"]

fs = 44100
duration = 3

while True:
    print("Listening...")

    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()

    audio = audio.flatten()

    mfcc = librosa.feature.mfcc(y=audio, sr=fs, n_mfcc=13)
    mfcc = np.mean(mfcc.T, axis=0)
    mfcc = mfcc.reshape(1, -1)

    prediction = model.predict(mfcc)

    predicted_class = classes[np.argmax(prediction)]

    print("Detected:", predicted_class)