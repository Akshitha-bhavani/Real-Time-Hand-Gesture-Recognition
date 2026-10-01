import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hand model
mp_hands = mp.solutions.hands #
mp_drawing = mp.solutions.drawing_utils

# Define the hands function
hands = mp_hands.Hands(
    static_image_mode=False, 
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
)

# Gesture recognition function
def recognize_gesture(landmarks):
    # Extract y-coordinates of tips of fingers
    tips = [4, 8, 12, 16, 20]
    fingers = []

    # Thumb
    if landmarks[tips[0]].x < landmarks[tips[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other four fingers
    for tip in tips[1:]:
        if landmarks[tip].y < landmarks[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    # Classify gestures
    if fingers == [0, 1, 1, 0, 0]:
        return "Peace ✌"
    elif fingers == [0, 1, 0, 0, 0]:
        return "Point ☝"
    elif fingers == [0, 0, 0, 0, 0]:
        return "Fist ✊"
    elif fingers == [1, 1, 1, 1, 1]:
        return "Open Palm 🖐"
    elif fingers == [1, 0, 0, 0, 0]:
        return "Thumbs Up 👍"
    else:
        return "Unknown"

# Start webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty frame.")
        continue

    # Flip image for mirror view
    image = cv2.flip(image, 1)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_image)

    gesture = "No Hand"

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = recognize_gesture(hand_landmarks.landmark)

    # Display gesture text
    cv2.putText(image, gesture, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)
    cv2.imshow('Hand Gesture Recognition', image)

    if cv2.waitKey(5) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()