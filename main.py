# main.py

import cv2
import mediapipe as mp
import time
from gesture import is_distress_gesture
from alert import send_whatsapp_alert
from config import HOLD_TIME

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

gesture_start_time = None
alert_sent_for_current_gesture = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    current_time = time.time()
    distress_detected = False

    if result.multi_hand_landmarks and result.multi_handedness:
        for i, hand_landmarks in enumerate(result.multi_hand_landmarks):
            mp_draw.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
            )

            hand_label = result.multi_handedness[i].classification[0].label

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

    cv2.imshow("CCTV Distress Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
