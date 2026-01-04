# CCTV-Distress-Detection
This project implements a real-time CCTV-based safety system that detects a distress hand signal using computer vision and triggers immediate emergency alerts.
Using OpenCV and MediaPipe, the system tracks hand landmarks and identifies a standardized distress gesture (four fingers up, thumb tucked) for both left and right hands. Upon detection, the system captures a snapshot, uploads it to the cloud, and sends a WhatsApp alert with image evidence and a Google Maps location link via Twilio.

Designed with false-positive reduction, gesture state tracking, and real-world deployment considerations, this project demonstrates the practical application of AI for public safety and surveillance systems.
