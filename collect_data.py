import cv2
import mediapipe as mp
import csv
import os

file_name = "data.csv"

if not os.path.exists(file_name):
    with open(file_name, mode='w', newline='') as f:
        pass

gesture_name = input("Enter gesture name: ").upper()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

print("📸 Collecting Data... Press ESC to stop")

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            x_list = []
            y_list = []
            lmList = []

            for lm in handLms.landmark:
                x_list.append(lm.x)
                y_list.append(lm.y)

            min_x = min(x_list)
            min_y = min(y_list)

            for x, y in zip(x_list, y_list):
                lmList.extend([x - min_x, y - min_y])

            if len(lmList) == 42:
                lmList.append(gesture_name)

                with open(file_name, mode='a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(lmList)

    cv2.imshow("Collecting Data", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()