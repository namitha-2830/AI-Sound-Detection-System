import sounddevice as sd
import numpy as np
import wavio  # For saving WAV files

duration = 5  # seconds
sample_rate = 44100
device_id = 7  # Your microphone device ID

print("Recording...")
audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, device=device_id)
sd.wait()
print("Recording complete")

# Save as WAV file
filename = "recorded_audio.wav"
wavio.write(filename, audio, sample_rate, sampwidth=2)
print(f"Audio saved as {filename}")