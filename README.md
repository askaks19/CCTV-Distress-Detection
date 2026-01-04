# 🚨 CCTV Distress Detection System (WhatsApp Alerts)

A real-time computer vision system that detects a standardized distress hand gesture from live CCTV footage and automatically sends an emergency WhatsApp alert with image evidence and GPS location.

The system uses **MediaPipe hand landmark detection** and **OpenCV** to recognize a distress signal (four fingers raised with the thumb tucked) and integrates with **Twilio WhatsApp API** for alert delivery. Image snapshots are uploaded to **Cloudinary** to generate public URLs for WhatsApp media delivery.

This project is designed to run locally and can be easily cloned from GitHub.  
Environment variables are required for Twilio and Cloudinary configuration.

---

## ✨ Features

- Real-time CCTV / webcam feed processing
- Distress gesture detection (4 fingers up, thumb tucked)
- Works for **both left and right hands**
- Gesture hold-time validation to reduce false positives
- WhatsApp emergency alerts using Twilio
- Automatic image snapshot capture
- Cloud image hosting using Cloudinary
- Google Maps GPS location link (hardcoded CCTV location)
- GitHub-safe setup with environment variables

---

## 🛠️ Tech Stack

- Python 3.10+
- OpenCV
- MediaPipe
- Twilio WhatsApp API
- Cloudinary
- Computer Vision (rule-based gesture detection)

---

## 📸 Distress Gesture Definition

The alert is triggered **only when**:
- Index, Middle, Ring, Pinky fingers are **extended**
- Thumb is **tucked inside the palm**
- Gesture is held continuously for **2 seconds**

This follows a standardized distress hand signal and works for both hands.

---

## 📁 Folder Structure (High-level)
├── app.py # Main CCTV + detection + alert logic
├── .env.example # Environment variable template
├── .env # NOT committed (contains secrets)
├── README.md
├── requirements.txt
└── alerts/ # Temporary snapshots (ignored in Git)

---

## 🚀 Getting Started (Local Development)

### 1. Clone the repository

git clone <REPO_URL>
cd cctv-distress-detection

### 2. Create and activate virtual environment

Copy code
python -m venv mp_env
mp_env\Scripts\activate

### 3. Install dependencies

Copy code
pip install -r requirements.txt

### 4. Create your environment file
Duplicate .env.example and rename it to .env:


Copy code
cp .env.example .env
Fill in your Twilio and Cloudinary credentials.

⚠️ Never commit .env — it contains secrets.

### 5. Run the application

Copy code
python app.py
The CCTV feed will open in a window.
Show the distress gesture for 2 seconds to trigger a WhatsApp alert.
---

## Environment Variables

Required environment variables (see .env.example):

TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
TWILIO_WHATSAPP_FROM=
TWILIO_WHATSAPP_TO=

CLOUDINARY_CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=
---

## 📍 CCTV Location Configuration

The CCTV camera is assumed to be fixed.
GPS coordinates are hardcoded inside app.py:

CAMERA_NAME = "Hostel Gate CCTV"
CAMERA_LAT = 12.9716
CAMERA_LON = 77.5946


These values are used to generate a clickable Google Maps link in the WhatsApp alert.
---

## 🧠 Design Notes

Gesture detection uses hand landmark geometry, not ML classification

State-based gesture tracking prevents alert spamming

Cloudinary is used instead of local hosting or tunneling tools

Designed for real-world CCTV deployment scenarios

Easy to extend with ML models or multi-camera support
---
## 🎯 Use Cases

Campus security systems

Hostels and residential buildings

Parking areas

Public surveillance setups

Emergency response automation
---

## 🔒 Security Notes

Secrets are loaded via environment variables

.env and virtual environments are excluded from Git

Image snapshots are deleted locally after upload

Fire-and-forget alert mechanism to avoid blocking video feed
---

### 👤 Author

Ayush Kumar Singh








