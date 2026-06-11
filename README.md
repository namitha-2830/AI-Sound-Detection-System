# AI-Sound-Detection-System
AI-powered environmental sound classification using MFCC and Neural Networks.
# 🔊 AI-Based Smart Wearable Alert System for Hearing-Impaired Users

> AI-powered environmental sound classification using MFCC feature extraction and Neural Networks.

---

## 📖 Overview

The AI-Based Smart Wearable Alert System is designed to assist hearing-impaired individuals by detecting important environmental sounds and providing alerts.

The system uses Artificial Intelligence (AI) and Machine Learning (ML) techniques to classify sounds such as:

- 🚨 Alarm
- 🔔 Doorbell
- 👏 Clap

In this prototype, a laptop microphone is used as a simulated wearable sensor to capture environmental sounds. The captured audio is processed using MFCC (Mel Frequency Cepstral Coefficients) feature extraction and classified using a trained Neural Network model.

---

## 🎯 Problem Statement

People with hearing impairments may miss important environmental sounds such as alarms, doorbells, and emergency alerts.

This project aims to provide a smart solution that automatically detects such sounds and generates alerts to improve awareness and safety.

---

## ✨ Features

- AI-based environmental sound detection
- Alarm detection
- Doorbell detection
- Clap detection
- MFCC feature extraction
- Neural Network sound classification
- Real-time microphone monitoring
- Google Sheets event logging
- HTML alert dashboard
- Support for future custom sound training

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core Programming Language |
| TensorFlow / Keras | Neural Network Development |
| TensorFlow Hub | Audio Classification |
| Librosa | Audio Processing |
| NumPy | Numerical Computation |
| SoundDevice | Audio Recording |
| Wavio | WAV File Handling |
| Requests | API Communication |
| Google Sheets API | Event Logging |

---

## 🔄 Project Workflow

```text
Audio Input
     │
     ▼
MFCC Feature Extraction
     │
     ▼
Neural Network Model
     │
     ▼
Sound Classification
     │
     ▼
Alert Generation
     │
     ▼
Google Sheets Logging
```

---

## 📂 Project Structure

```text
AI-Sound-Detection-System/
│
├── README.md
├── requirements.txt
│
├── codes/
│   ├── train_model.py
│   ├── record_audio.py
│   ├── predict.py
│   ├── live_detection.py
│   └── google_sheets_logger.py
│
├── saved_model/
│   └── my_model.h5
│
└── screenshots/
    ├── environment_setup_and_model_loading.png
    ├── running_predict2_single_prediction.png
    ├── multiple_predictions_doorbell_clap.png
    ├── event_logging_to_googlesheets.png
    └── html_alert_dashboard.png
```

---

## 🧠 Machine Learning Model

### Architecture

```text
Input Layer (MFCC Features)
          │
          ▼
Dense Layer (128, ReLU)
          │
          ▼
Dropout (0.3)
          │
          ▼
Dense Layer (64, ReLU)
          │
          ▼
Output Layer (Softmax)
```

---

## 🔊 Supported Sound Categories

| Sound | Description |
|--------|-------------|
| 🚨 Alarm | Emergency alert detection |
| 🔔 Doorbell | Visitor notification |
| 👏 Clap | Sound event detection |

---

## 📊 Google Sheets Integration

Detected sound events are automatically logged with:

- Timestamp
- Detected Sound
- Alert Type

---

## 🖼️ Project Screenshots

- Environment Setup and Model Loading
- Single Sound Prediction
- Multiple Sound Predictions
- Event Logging to Google Sheets
- HTML Alert Dashboard

---

## 🚀 Applications

- Assistive technology for hearing-impaired individuals
- Smart home monitoring
- Safety alert systems
- Environmental sound awareness
- IoT-based monitoring solutions

---

## 🔮 Future Enhancements

- Wearable hardware integration
- Mobile application support
- Vibration-based notifications
- Additional sound categories
- Cloud dashboard integration
- Real-time deployment

---

## 👩‍💻 Author

**Namitha B M**

Electronics and Communication Engineering Student
