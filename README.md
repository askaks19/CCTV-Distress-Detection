# 🚨 CCTV Distress Detection System

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red?style=flat-square)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-green?style=flat-square)](https://mediapipe.dev/)
[![Twilio](https://img.shields.io/badge/Twilio-WhatsApp%20API-orange?style=flat-square)](https://www.twilio.com/)

A **real-time computer vision system** that detects standardized distress hand gestures from live CCTV footage and automatically sends emergency WhatsApp alerts with image evidence and GPS location coordinates.

---

## 🎯 Overview

This intelligent surveillance system uses **MediaPipe hand landmark detection** and **OpenCV** to recognize distress signals in real-time, integrating seamlessly with **Twilio WhatsApp API** for instant emergency notifications. Image snapshots are uploaded to **Cloudinary** for secure cloud hosting and WhatsApp delivery.

**Perfect for**: Campus security, hostels, parking areas, public surveillance, and automated emergency response systems.

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🎥 **Real-time Processing** | Live CCTV/webcam feed analysis |
| 🤚 **Gesture Recognition** | Detects 4-finger distress signal (both hands) |
| ✅ **Smart Validation** | 2-second hold time reduces false positives |
| 📲 **WhatsApp Alerts** | Instant emergency notifications via Twilio |
| 📸 **Evidence Capture** | Automatic snapshot with distress moment |
| ☁️ **Cloud Hosting** | Images uploaded to Cloudinary |
| 📍 **GPS Integration** | Google Maps location link in alert |
| 🔐 **Secure Setup** | Environment variables for all credentials |

---

## 🛠️ Tech Stack

┌─────────────────────────────────────┐
│ CCTV Distress Detection System │
├─────────────────────────────────────┤
│ - Python 3.10+ │
│ - OpenCV (Video Processing) │
│ - MediaPipe (Hand Detection) │
│ - Twilio API (WhatsApp) │
│ - Cloudinary (Image Hosting) │
│ - Rule-based Gesture Logic │
└─────────────────────────────────────┘


---

## 📸 Distress Gesture Definition

The system triggers an alert **ONLY** when:

✋ **Index, Middle, Ring, Pinky fingers** → Extended  
👍 **Thumb** → Tucked inside palm  
⏱️ **Hold Duration** → Minimum 2 seconds continuous

This standardized signal works for both left and right hands, reducing accidental triggers.

---

## 📁 Project Structure
cctv-distress-detection/
├── 📄 main.py # Entry point - run this first
├── 🤚 gesture.py # Hand gesture detection logic
├── 📲 alert.py # WhatsApp + Cloudinary integration
├── ⚙️ config.py # Configuration & constants
├── 📦 requirements.txt # Project dependencies
├── 📋 .env.example # Environment variables template
└── 📖 README.md # This file


---

## 🚀 Quick Start Guide

### Step 1: Clone Repository

```bash
git clone https://github.com/askaks19/CCTV-Distress-Detection.git
cd CCTV-Distress-Detection
```
### Step 2: Set Up Virtual Environment
```
python -m venv mp_env
mp_env\Scripts\activate
```
### Step 3: Install Dependencies
```
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
Create a .env file in the project root:
```
cp .env.example .env
```
## Fill in your credentials:
# Twilio WhatsApp Configuration
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_FROM=+1234567890
TWILIO_WHATSAPP_TO=+9876543210

# Cloudinary Image Hosting
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

# CCTV Location (Coordinates)
CAMERA_NAME=Hostel Gate
CAMERA_LAT=12.9716
CAMERA_LON=77.5946

⚠️ Important: Never commit .env - it contains secrets!

### Step 5: Run the System
```python main.py```
A window will open showing the live CCTV feed. Show the distress gesture for 2+ seconds to trigger a WhatsApp alert.

## 🔧 Configuration
Twilio Setup
Create a Twilio account

Get your Account SID and Auth Token

Set up WhatsApp Sender (Twilio sandbox or production)

Configure recipient WhatsApp number

### Cloudinary Setup
Sign up at Cloudinary

Get your Cloud Name, API Key, and API Secret

Images will auto-delete locally after cloud upload

### CCTV Location
Edit config.py to set your camera's GPS coordinates:

```
CAMERA_NAME = "Parking Area North"
CAMERA_LAT = 40.7128
CAMERA_LON = -74.0060
```
### 📖 How It Works

┌────────────────────┐
│  CCTV Feed Input   │
└──────────┬─────────┘
           │
           ▼
┌─────────────────────────────────┐
│ MediaPipe Hand Detection        │
│ (Extract 21 hand landmarks)     │
└──────────┬─────────────────────┘
           │
           ▼
┌─────────────────────────────────┐
│ Gesture Recognition             │
│ (Check finger & thumb status)   │
└──────────┬─────────────────────┘
           │
           ▼
┌─────────────────────────────────┐
│ Validation Check                │
│ (2 second hold time?)           │
└──────────┬─────────────────────┘
           │
          YES
           │
           ▼
┌─────────────────────────────────┐
│ Capture Snapshot                │
│ Upload to Cloudinary            │
└──────────┬─────────────────────┘
           │
           ▼
┌─────────────────────────────────┐
│ Send WhatsApp Alert             │
│ (Image + GPS Location)          │
└─────────────────────────────────┘

## 💡 Design Principles
✅ Gesture detection uses hand landmark geometry (no ML model needed)
✅ State tracking prevents alert spamming from continuous gestures
✅ Cloudinary integration enables secure cloud image storage
✅ Fire-and-forget alerts don't block the video processing loop
✅ Easy to extend with multi-camera support or ML models

## 🎯 Use Cases
### 🏫 Campus Security - Student emergency signaling in classrooms

### 🏨 Hostels & Residences - Guest distress detection in common areas

### 🚗 Parking Areas - Suspicious activity or theft alerts

### 👁️ Public Surveillance - Mall, airport, railway station monitoring

### 🚨 Emergency Response - Auto-triggering security protocols

## 🔒 Security Best Practices
✅ Secrets loaded via environment variables only
✅ .env and virtual environments excluded from Git
✅ Image snapshots auto-deleted locally after upload
✅ Fire-and-forget mechanism prevents video feed blocking
✅ No sensitive data in logs or version control

## 📝 Environment Variables Reference
Variable	Purpose	Example
TWILIO_ACCOUNT_SID	Twilio account identifier	ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN	Twilio authentication token	auth_token_here
TWILIO_WHATSAPP_FROM	Twilio WhatsApp sender	+1234567890
TWILIO_WHATSAPP_TO	Alert recipient number	+919876543210


## 🛑 Troubleshooting
Issue: Camera feed not opening
→ Check camera permissions and try webcam index 0 or 1 in config.py

Issue: Gesture not detected
→ Ensure good lighting and hand is fully visible. Test gesture hold for 2+ seconds.

Issue: WhatsApp alert not sending
→ Verify Twilio credentials and WhatsApp phone numbers are correct (include country code)

Issue: Image upload fails
→ Check Cloudinary API credentials and internet connection

## 📚 Dependencies
text
opencv-python>=4.5.0
mediapipe>=0.8.0
twilio>=8.0.0
cloudinary>=1.30.0
python-dotenv>=0.19.0
Install with: pip install -r requirements.txt

## 🚀 Future Enhancements
 Multi-camera support with central dashboard

 Machine learning gesture classification

 Historical event logging and analytics

 Mobile app for alert management

 Video recording on distress detection

 Sound alarm integration

 Database-backed configuration

## 📄 License
MIT License - Feel free to use, modify, and distribute

## 👤 Author
Ayush Kumar Singh
B.Tech Computer Science (AI) - MIT Bengaluru

## 🙏 Acknowledgments
MediaPipe for hand detection models

OpenCV for computer vision utilities

Twilio for WhatsApp API integration

Cloudinary for reliable image hosting


