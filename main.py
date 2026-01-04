import cv2
import os
import mediapipe as mp
import time
from twilio.rest import Client
import cloudinary
import cloudinary.uploader
cloudinary.config(
    cloud_name="[your cloud name]",
    api_key="[your api key]",
    api_secret="[api secret]"
)


CAMERA_LAT = 12.9716
CAMERA_LON = 77.5946
CAMERA_NAME = " Gate 1 CCTV"

def get_google_maps_link():
    return f"https://www.google.com/maps?q={CAMERA_LAT},{CAMERA_LON}"


# =========================
# TWILIO CONFIG (USE YOURS)
# =========================
ACCOUNT_SID = "[enter your account SID] "
AUTH_TOKEN  = "[enter your account auth] "

WHATSAPP_FROM = "whatsapp:+14....."   # Twilio sandbox
WHATSAPP_TO   = "whatsapp:+91........"  # YOUR WhatsApp number (10 digits)

client = Client(ACCOUNT_SID, AUTH_TOKEN)

# =========================
# MEDIAPIPE SETUP
# =========================
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# =========================
# CAMERA
# =========================
cap = cv2.VideoCapture(0)

# =========================
# STATE VARIABLES
# =========================
gesture_start_time = None
last_alert_time = 0

HOLD_TIME = 2          # seconds gesture must be held
ALERT_COOLDOWN = 15    # seconds between alerts

# =========================
# DISTRESS GESTURE LOGIC
# 4 fingers up + thumb tucked
# =========================
def is_distress_gesture(landmarks, handedness):
    fingers = [
        (8, 6), (12, 10), (16, 14), (20, 18)
    ]

    for tip, joint in fingers:
        if landmarks[tip].y > landmarks[joint].y:
            return False

    thumb_tip = landmarks[4]
    thumb_joint = landmarks[3]

    if handedness == "Right":
        if thumb_tip.x < thumb_joint.x:
            return False
    else:  # Left hand
        if thumb_tip.x > thumb_joint.x:
            return False

    return True


# =========================
# SEND WHATSAPP TEXT ALERT
# =========================
def send_whatsapp_alert(frame):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    # Save snapshot temporarily
    filename = f"alert_{int(time.time())}.jpg"
    cv2.imwrite(filename, frame)

    # Upload to Cloudinary
    upload_result = cloudinary.uploader.upload(filename)
    image_url = upload_result["secure_url"]

    # Google Maps link
    maps_url = get_google_maps_link()

    message = f"""
🚨 *EMERGENCY ALERT*
Distress hand signal detected!

📍 Camera: {CAMERA_NAME}
📌 Location: {maps_url}
🕒 Time: {timestamp}

⚠️ Immediate attention required.
"""

    client.messages.create(
        body=message,
        from_=WHATSAPP_FROM,
        to=WHATSAPP_TO,
        media_url=[image_url]
    )

    print("✅ WhatsApp alert sent with image + GPS")

    # Optional cleanup
    os.remove(filename)


# =========================
# MAIN LOOP
# =========================
while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to read frame")
        break

    frame = cv2.flip(frame, 1)

    # ALWAYS show frame first
    cv2.imshow("CCTV Distress Detection", frame)

    # THEN do MediaPipe
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    current_time = time.time()
    distress_detected = False

    if result.multi_hand_landmarks and result.multi_handedness:
        for idx, hand_landmarks in enumerate(result.multi_hand_landmarks):
            mp_draw.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
            )

            hand_label = result.multi_handedness[idx].classification[0].label

            if is_distress_gesture(hand_landmarks.landmark, hand_label):
                distress_detected = True

                if gesture_start_time is None:
                    gesture_start_time = current_time
                    alert_sent_for_current_gesture = False

                elapsed = current_time - gesture_start_time

                cv2.putText(
                    frame,
                    f"DISTRESS ({hand_label}) {elapsed:.1f}s",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 0, 255),
                    2
                )

                if elapsed >= HOLD_TIME and not alert_sent_for_current_gesture:
                    send_whatsapp_alert(frame)
                    alert_sent_for_current_gesture = True

    if not distress_detected:
        gesture_start_time = None
        alert_sent_for_current_gesture = False

    # SHOW UPDATED FRAME
    cv2.imshow("CCTV Distress Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()

