# gesture.py

def is_distress_gesture(landmarks, handedness):
    """
    Distress gesture:
    - Index, Middle, Ring, Pinky extended
    - Thumb tucked (hand-aware)
    """

    fingers = [(8, 6), (12, 10), (16, 14), (20, 18)]

    # Check 4 fingers extended
    for tip, joint in fingers:
        if landmarks[tip].y > landmarks[joint].y:
            return False

    thumb_tip = landmarks[4]
    thumb_joint = landmarks[3]

    if handedness == "Right":
        return thumb_tip.x > thumb_joint.x
    else:  # Left hand
        return thumb_tip.x < thumb_joint.x
