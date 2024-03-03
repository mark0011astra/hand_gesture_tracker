import cv2
import mediapipe as mp
import numpy as np

hands = mp.solutions.hands.Hands(
    static_image_mode=False, #動画ではなく静止画像を扱う場合にTrueに設定する。動画の場合はFalseが効果的
    max_num_hands=2, #同時に検出する手の最大数
    min_detection_confidence=0.5, #手が検出されたとみなされる信頼度の閾値
    min_tracking_confidence=0.5) #手の追跡を続けるための信頼度の閾値


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
        
def get_hand_landmarks_coordinates(hand_landmarks):
    # 手のランドマーク座標を取得
    landmarks_coordinates = []
    for lm in hand_landmarks.landmark:
        landmarks_coordinates.append((lm.x, lm.y, lm.z))
    return landmarks_coordinates

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
            
            """
            # ランドマーク座標の描画
            for hand_landmarks in results.multi_hand_landmarks:
                # ランドマーク座標の取得
                landmarks_coordinates = get_hand_landmarks_coordinates(hand_landmarks)
                print(landmarks_coordinates)
            """    
            
            draw_landmarks_and_labels(img, results.multi_hand_landmarks, mp_draw)
        
        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == '__main__':
    main()
