import cv2
import mediapipe as mp
import joblib
import os
import pyttsx3
import pandas as pd
import threading
from collections import deque, Counter

# ------------------------------
# Load Model
# ------------------------------
MODEL_FILE = "gesture_model.pkl"

if not os.path.exists(MODEL_FILE):
    print(" Model not found! Run train_model.py first.")
    exit()

model = joblib.load(MODEL_FILE)
print(" Model Loaded Successfully")

# ------------------------------
# Gesture → Sentence Mapping
# ------------------------------
gesture_map = {
    "HELLO": "Hello",
    "ILOVEYOU": "I Love You",
    "HELP": "I Need Help",
    "YES": "Yes",
    "NO": "No",
    "PLEASE": "Please",
    "THANKYOU": "Thank You"
}

# ------------------------------
# Voice Setup
# ------------------------------
engine = pyttsx3.init()

def speak(text):
    def run():
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=run).start()

last_spoken = ""

# ------------------------------
# Mediapipe Setup
# ------------------------------
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# ------------------------------
# Camera
# ------------------------------
cap = cv2.VideoCapture(0)
print("Camera Started... Press ESC to exit")

# ------------------------------
# Smoothing Buffer
# ------------------------------
buffer = deque(maxlen=10)

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    gesture = "No Hand"
    confidence = 0.0
    lmList = []

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            x_list = [lm.x for lm in handLms.landmark]
            y_list = [lm.y for lm in handLms.landmark]

            # Normalize
            min_x, min_y = min(x_list), min(y_list)
            for x, y in zip(x_list, y_list):
                lmList.extend([x - min_x, y - min_y])

        if len(lmList) == 42:
            df = pd.DataFrame([lmList])
            prediction = model.predict(df)[0]
            proba = model.predict_proba(df).max()
            buffer.append((prediction, proba))

            # Majority voting for stability
            if len(buffer) == buffer.maxlen:
                most_common = Counter([p[0] for p in buffer]).most_common(1)[0][0]
                gesture = most_common
                confidence = max([p[1] for p in buffer if p[0] == most_common])

    # ------------------------------
    # Display Sentence (Text + %)
    # ------------------------------
    if gesture in gesture_map:
        display_text = f"{gesture_map[gesture]} ({confidence*100:.0f}%)"  # shows percentage on screen
        voice_text = gesture_map[gesture]  # only text for voice
    else:
        display_text = gesture
        voice_text = gesture

    # ------------------------------
    # Voice Logic (Text Only)
    # ------------------------------
    if gesture != "No Hand" and gesture != last_spoken:
        speak(voice_text)  # speak only text
        last_spoken = gesture

    if gesture == "No Hand":
        last_spoken = ""

    # ------------------------------
    # Show Frame
    # ------------------------------
    cv2.putText(img, display_text, (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5,
                (0, 255, 0), 2)

    cv2.imshow("Gesture AI System", img)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()