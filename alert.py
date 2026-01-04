# alert.py

import time
import os
import cv2
import cloudinary
import cloudinary.uploader
from twilio.rest import Client
from config import (
    ACCOUNT_SID, AUTH_TOKEN,
    WHATSAPP_FROM, WHATSAPP_TO,
    CAMERA_NAME, CAMERA_LAT, CAMERA_LON,
    CLOUD_NAME, API_KEY, API_SECRET
)

# Cloudinary setup
cloudinary.config(
    cloud_name=CLOUD_NAME,
    api_key=API_KEY,
    api_secret=API_SECRET
)

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def get_google_maps_link():
    return f"https://www.google.com/maps?q={CAMERA_LAT},{CAMERA_LON}"

def send_whatsapp_alert(frame):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    filename = f"alert_{int(time.time())}.jpg"
    cv2.imwrite(filename, frame)

    upload_result = cloudinary.uploader.upload(filename)
    image_url = upload_result["secure_url"]

    message = f"""
🚨 *EMERGENCY ALERT*
Distress hand signal detected!

📍 Camera: {CAMERA_NAME}
📌 Location: {get_google_maps_link()}
🕒 Time: {timestamp}

⚠️ Immediate attention required.
"""

    client.messages.create(
        body=message,
        from_=WHATSAPP_FROM,
        to=WHATSAPP_TO,
        media_url=[image_url]
    )

    os.remove(filename)
    print("✅ WhatsApp alert sent")
