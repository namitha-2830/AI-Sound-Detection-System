import os
import numpy as np
import librosa

DATA_PATH = "data"

features = []
labels = []

for label, folder in enumerate(os.listdir(DATA_PATH)):
    folder_path = os.path.join(DATA_PATH, folder)

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        audio, sr = librosa.load(file_path, sr=None)

        mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
        mfcc_mean = np.mean(mfcc.T, axis=0)

        features.append(mfcc_mean)
        labels.append(label)

X = np.array(features)
y = np.array(labels)

np.save("X.npy", X)
np.save("y.npy", y)

print("Features extracted successfully!")