# hand_gesture_tracker

This project utilizes OpenCV, MediaPipe, and NumPy to implement hand tracking in real-time video. It detects hands in the video stream from a webcam and draws landmarks and connections on the detected hands.

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