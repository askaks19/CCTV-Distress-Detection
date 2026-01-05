# 🚨 CCTV Distress Detection System

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red?style=flat-square)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-green?style=flat-square)](https://mediapipe.dev/)
[![Twilio](https://img.shields.io/badge/Twilio-WhatsApp%20API-orange?style=flat-square)](https://www.twilio.com/)

> A **real-time computer vision system** that detects standardized distress hand gestures from live CCTV footage and automatically sends emergency WhatsApp alerts with image evidence and GPS location coordinates.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

This intelligent surveillance system uses **MediaPipe hand landmark detection** and **OpenCV** to recognize distress signals in real-time, integrating seamlessly with **Twilio WhatsApp API** for instant emergency notifications. Image snapshots are uploaded to **Cloudinary** for secure cloud hosting and WhatsApp delivery.

### Perfect for:
- 🏫 Campus security
- 🏢 Hostels and residential facilities
- 🅿️ Parking areas
- 👥 Public surveillance
- 🚨 Automated emergency response systems
- 🎭 Event venues and crowded spaces

---

## ✨ Key Features

| Feature | Description | Status |
|---------|-------------|--------|
| 🎥 **Real-time Processing** | Live CCTV/webcam feed analysis | ✅ |
| 🤚 **Gesture Recognition** | Detects 4-finger distress signal (both hands) | ✅ |
| ✅ **Smart Validation** | 2-second hold time reduces false positives | ✅ |
| 📲 **WhatsApp Alerts** | Instant emergency notifications via Twilio | ✅ |
| 📸 **Evidence Capture** | Automatic snapshot with distress moment | ✅ |
| ☁️ **Cloud Hosting** | Images uploaded to Cloudinary | ✅ |
| 📍 **GPS Integration** | Google Maps location link in alert | ✅ |
| 🔔 **Multi-recipient** | Alert multiple WhatsApp numbers | ✅ |
| 🎨 **Visual Feedback** | Real-time hand landmark visualization | ✅ |
| ⚡ **Low Latency** | Optimized for real-time performance | ✅ |

---

## 🛠 Tech Stack

### Core Technologies
- **Python 3.10+** - Backend programming language
- **OpenCV** - Computer vision library
- **MediaPipe** - Hand landmark detection
- **Twilio** - WhatsApp API integration
- **Cloudinary** - Cloud image hosting

### Supporting Libraries
- `numpy` - Numerical computations
- `requests` - HTTP requests
- `python-dotenv` - Environment variable management
- `geopy` - GPS location handling

---

## 📦 Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Webcam or CCTV feed access
- Active internet connection

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/askaks19/CCTV-Distress-Detection.git
   cd CCTV-Distress-Detection
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables** (see [Configuration](#-configuration))
   ```bash
   cp .env.example .env
   ```

---

## ⚙️ Configuration

### Twilio Setup
1. Sign up at [Twilio](https://www.twilio.com/)
2. Get your Account SID and Auth Token
3. Set up WhatsApp Sender (sandbox or production)
4. Configure recipient WhatsApp number

```bash
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_FROM=whatsapp:+1234567890
TWILIO_WHATSAPP_TO=whatsapp:+0987654321
```

### Cloudinary Setup
1. Sign up at [Cloudinary](https://cloudinary.com/)
2. Get your Cloud Name, API Key, and API Secret

```bash
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

### Camera Location
Edit `config.py` to set your camera's GPS coordinates:

```python
CAMERA_NAME = "Parking Area North"
CAMERA_LAT = 40.7128
CAMERA_LON = -74.0060
```

Images will auto-delete locally after cloud upload

---

## 🚀 Usage

### Run the Application

```bash
python main.py
```

### With Command-line Options

```bash
# Using webcam (default)
python main.py --source 0

# Using video file
python main.py --source path/to/video.mp4

# Using RTSP stream (IP camera)
python main.py --source "rtsp://camera_ip:port/stream"

# Display confidence threshold
python main.py --threshold 0.8
```

### Keyboard Controls
- `q` - Quit application
- `s` - Save current frame
- `r` - Reset detection timer
- `d` - Toggle debug mode

---

## 🔧 How It Works

```
┌─────────────────┐
│  CCTV Feed Input│
└────────┬────────┘
         │
         ▼
┌──────────────────────────┐
│  MediaPipe Hand Tracking │
│  (Landmark Detection)    │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│   Gesture Recognition    │
│  (4-finger distress)     │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│   Smart Validation       │
│  (2-second hold timer)   │
└────────┬─────────────────┘
         │
         ▼
    ┌────┴────┐
    │Confirmed?│
    └────┬────┘
         │ YES
         ▼
┌──────────────────────────┐
│  Capture Screenshot      │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│  Upload to Cloudinary    │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│  Send WhatsApp Alert     │
│  (via Twilio + GPS)      │
└──────────────────────────┘
```

### Detection Algorithm

1. **Hand Landmark Detection**: MediaPipe detects 21 hand landmarks per hand
2. **Gesture Classification**: Analyzes finger positions and angles
3. **Distress Signal**: Detects when all 4 fingers are raised (thumbs down gesture)
4. **Temporal Validation**: Requires 2-second continuous detection to prevent false positives
5. **Alert Trigger**: Upon confirmation, captures image and sends WhatsApp notification

---

## 📁 Project Structure

```
CCTV-Distress-Detection/
├── main.py                 # Main application entry point
├── config.py              # Configuration settings
├── requirements.txt        # Python dependencies
├── .env.example           # Example environment variables
│
├── src/
│   ├── detector.py        # MediaPipe hand detection
│   ├── gesture.py         # Gesture recognition logic
│   ├── alert.py           # Twilio WhatsApp integration
│   ├── cloud.py           # Cloudinary image upload
│   └── utils.py           # Utility functions
│
├── models/
│   └── hand_landmark.pb   # Exported MediaPipe model
│
├── tests/
│   ├── test_detector.py
│   ├── test_gesture.py
│   └── test_alert.py
│
├── docs/
│   ├── SETUP.md           # Detailed setup guide
│   ├── API.md             # API documentation
│   └── TROUBLESHOOTING.md # Common issues & solutions
│
└── README.md              # This file
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest

# Run linter
pylint src/

# Format code
black src/
```

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🆘 Support & Issues

If you encounter any issues:

1. Check [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)
2. Review [open issues](https://github.com/askaks19/CCTV-Distress-Detection/issues)
3. Create a [new issue](https://github.com/askaks19/CCTV-Distress-Detection/issues/new) with detailed information

---

## 🙏 Acknowledgments

- [MediaPipe](https://mediapipe.dev/) for hand landmark detection
- [Twilio](https://www.twilio.com/) for WhatsApp API
- [Cloudinary](https://cloudinary.com/) for cloud hosting
- [OpenCV](https://opencv.org/) for computer vision capabilities

---

**⭐ If this project helped you, please consider giving it a star!**

Made with ❤️ by [ayushhhks](https://github.com/ayushhhks)
