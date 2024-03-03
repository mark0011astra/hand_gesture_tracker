import cv2
import mediapipe as mp
import numpy as np

def initialize_hand_tracker():
    # ハンドトラッキングの初期化
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    mp_draw = mp.solutions.drawing_utils
    return hands, mp_draw

def draw_landmarks_and_labels(img, hand_landmarks, mp_draw):
    # ランドマークの描画
    for hand_landmarks in hand_landmarks:
        mp_draw.draw_landmarks(img, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

def main():
    cap = cv2.VideoCapture(0)
    hands, mp_draw = initialize_hand_tracker()

    while True:
        success, img = cap.read()
        if not success:
            break

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:
            draw_landmarks_and_labels(img, results.multi_hand_landmarks, mp_draw)
        
        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == '__main__':
    main()
