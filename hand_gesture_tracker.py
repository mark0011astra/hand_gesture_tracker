import cv2
import mediapipe as mp
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import time

def initialize_hand_tracker():
    # ハンドトラッキングの初期化
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    mp_draw = mp.solutions.drawing_utils
    return hands, mp_draw

def convert_landmarks_to_np(hand_landmarks):
    # ランドマークをNumPy配列に変換
    landmarks_array = np.array([[lm.x, lm.y, lm.z] for lm in hand_landmarks.landmark])
    return landmarks_array - landmarks_array[0]

def calculate_cosine_similarity(A, B):
    # コサイン類似度の計算
    similarity = cosine_similarity(A.reshape(1, -1), B.reshape(1, -1))
    return similarity.flatten()[0]

def draw_landmarks_and_labels(img, hand_landmarks, mp_draw, mp_hands):
    # ランドマークとラベルの描画
    for i, lm in enumerate(hand_landmarks.landmark):
        height, width, _ = img.shape
        cx, cy = int(lm.x * width), int(lm.y * height)
        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        cv2.putText(img, str(i+1), (cx+10, cy+10), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
    mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

def main():
    cap = cv2.VideoCapture(0)
    hands, mp_draw = initialize_hand_tracker()
    saved_gestures = [None] * 3
    gesture_scores = [0] * 3
    saved_no = -1
    start_time = -100

    while True:
        success, img = cap.read()
        if not success:
            break

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                draw_landmarks_and_labels(img, hand_landmarks, mp_draw, mp.solutions.hands)
                
                for key, action in zip(['s', 'd', 'f'], range(3)):
                    if cv2.waitKey(1) & 0xFF == ord(key):
                        # ジェスチャーの保存
                        saved_gestures[action] = convert_landmarks_to_np(hand_landmarks)
                        start_time = time.time()
                        saved_no = action + 1
                        print(f'ジェスチャー {saved_no} が保存されました')

                current_gesture = convert_landmarks_to_np(hand_landmarks) if saved_gestures[0] is not None else None
                for i, saved_gesture in enumerate(saved_gestures):
                    if saved_gesture is not None:
                        # 保存されたジェスチャーとの類似度を計算
                        gesture_scores[i] = calculate_cosine_similarity(saved_gesture, current_gesture)

        # ジェスチャー認識情報の表示
        display_gesture_recognition_info(img, start_time, saved_no, gesture_scores)
        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def display_gesture_recognition_info(img, start_time, saved_no, scores):
    # 認識されたジェスチャー情報の表示
    if time.time() - start_time < 3:
        cv2.putText(img, f'ジェスチャー {saved_no} が保存されました', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    for i, score in enumerate(scores):
        if score > 0.99:
            cv2.putText(img, f'ジェスチャー {i+1}', (50, 100 * (i+2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

if __name__ == '__main__':
    main()
