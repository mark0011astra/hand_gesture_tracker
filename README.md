# hand_gesture_tracker


OpenCV、MediaPipe、およびNumPyを使用してリアルタイムビデオでのハンドトラッキングを実装します。ウェブカメラからのビデオストリーム内の手を検出し、検出された手にランドマークと接続を描画します。

## 特徴

- ウェブカメラを使用したリアルタイムの手追跡。
- 2つの手を同時に検出。
- 手のランドマークと接続を描画。

## 必要条件

- Python 3.x
- OpenCV
- MediaPipe
- NumPy

## インストール

1. pipを使用して必要なライブラリをインストールします：

```
pip install opencv-python mediapipe numpy
```

2. このリポジトリをクローンするか、スクリプトをダウンロードします。

## 使用方法

ハンドトラッキングアプリケーションを実行するには、スクリプト内の`main`関数を実行します。これにより、検出された手にランドマークが描画されたウェブカメラからのビデオを表示するウィンドウが開きます。

アプリケーションを終了するには 'q' を押します。

## 動作原理

- スクリプトはMediaPipeの`Hands`ソリューションを使用してハンドトラッカーを初期化します。
- ウェブカメラからのビデオをキャプチャし、各フレームを処理して手のランドマークを検出します。
- 手が検出された場合、MediaPipeの描画ユーティリティを使用して手にランドマークと接続を描画します。

### 主要コンポーネント

- `initialize_hand_tracker`: ハンドトラッキングを初期化します。
- `draw_landmarks_and_labels`: 手にランドマークと接続を描画します。
- `get_hand_landmarks_coordinates`: 手のランドマークの座標を取得します。

## 注意

手の検出モデルは、背景がクリアで照明が良い状態で最もよく機能します。

## 貢献

ハンドトラッキングプロジェクトの改善への貢献を歓迎します。リポジトリをフォークして変更を加え、プルリクエストを送信してください。

## ライセンス

このプロジェクトはオープンソースであり、MITライセンスの下で利用可能です。

---------------

OpenCV, MediaPipe, and NumPy to implement hand tracking in real-time video. It detects hands in the video stream from a webcam and draws landmarks and connections on the detected hands.

## Features

- Real-time hand tracking using a webcam.
- Detection of up to two hands simultaneously.
- Drawing of hand landmarks and connections.

## Requirements

- Python 3.x
- OpenCV
- MediaPipe
- NumPy

## Installation

1. Install the required libraries using pip:

```
pip install opencv-python mediapipe numpy
```

2. Clone this repository or download the script.

## Usage

To run the hand tracking application, execute the `main` function in the script. This will open up a window displaying the video from your webcam with hand landmarks drawn on detected hands.

Press 'q' to quit the application.

## How It Works

- The script initializes a hand tracker using MediaPipe's `Hands` solution.
- It captures video from the webcam and processes each frame to detect hand landmarks.
- If hands are detected, it draws landmarks and connections on the hands using MediaPipe's drawing utilities.

### Key Components

- `initialize_hand_tracker`: Initializes hand tracking.
- `draw_landmarks_and_labels`: Draws landmarks and connections on the hands.
- `get_hand_landmarks_coordinates`: Retrieves the coordinates of hand landmarks.

## Note

The hand detection model works best with a clear background and good lighting.

## Contributing

Contributions to improve the hand tracking project are welcome. Please feel free to fork the repository, make changes, and submit a pull request.

## License

This project is open-source and available under the MIT License.