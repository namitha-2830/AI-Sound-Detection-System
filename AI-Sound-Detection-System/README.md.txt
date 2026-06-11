AI-Based Smart Wearable Alert System for Hearing-Impaired Users
Overview

This project is a prototype AI-powered sound detection system designed to assist hearing-impaired individuals by recognizing important environmental sounds and generating alerts.

The system uses Machine Learning and Audio Signal Processing techniques to classify sounds such as:

Alarm
Doorbell
Clap

For demonstration purposes, a laptop microphone was used as the sound sensor, simulating how a microphone embedded in a wearable device would capture environmental audio.

Problem Statement

Hearing-impaired individuals may miss important environmental sounds such as alarms, doorbells, or warning signals.

The objective of this project is to develop an intelligent sound recognition system that can identify such sounds and provide alerts to the user.

Features
Environmental sound classification using AI
MFCC-based audio feature extraction
Neural Network sound recognition model
Live audio recording through microphone
Event logging with timestamps
Dashboard display of detected sounds
User-trainable custom sound categories
System Workflow
Collect audio samples.
Extract MFCC features from audio files.
Train a neural network model.
Record or load audio input.
Extract features from the input sound.
Predict the sound category.
Display and log the detected sound.
Project Structure

AI-Sound-Detection-System

├── extract_features.py

├── train_model.py

├── record_audio.py

├── predict_sound.py

├── requirements.txt

├── screenshots/

└── README.md

Technologies Used
Python
TensorFlow / Keras
Librosa
NumPy
SoundDevice
WAVIO
Google Sheets (Event Logging)
HTML Dashboard
Machine Learning Approach

The project uses MFCC (Mel Frequency Cepstral Coefficients) to represent audio signals as numerical feature vectors.

A Neural Network model was trained on extracted audio features to classify sounds into predefined categories.

Model Architecture:

Input Layer

↓

Dense Layer (128 Neurons)

↓

Dropout Layer (0.3)

↓

Dense Layer (64 Neurons)

↓

Softmax Output Layer

Custom Sound Training

One of the key features of this project is the ability to add custom sounds.

Users can:

Record their own sound samples
Add them to the dataset
Retrain the model
Detect personalized sounds such as custom doorbells, horns, or knock patterns
Applications
Smart Wearable Devices
Hearing Assistance Systems
Home Automation
Safety Monitoring
Smart Alert Systems
Future Improvements
Deploy on embedded wearable hardware
Add vibration-based alerts
Real-time audio streaming
Mobile application integration
Larger training dataset for improved accuracy
Author

Namitha B M

Electronics and Communication Engineering