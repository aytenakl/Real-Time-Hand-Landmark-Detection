# 🖐️ Real-Time Hand Landmark & Index Finger Tracking

A real-time computer vision project using **MediaPipe** and **OpenCV** to detect and track hand landmarks through a webcam.

The application detects up to **two hands**, identifies all **21 landmarks** on each detected hand, and specifically tracks the position of the **index finger tip** in real time.

---

## 🚀 Features

* 🖐️ Real-time hand landmark detection
* 🤚 Support for up to **2 hands**
* 📍 Detection of **21 landmarks per hand**
* ☝️ Index finger tip tracking
* 📐 Conversion of normalized landmark coordinates into pixel coordinates
* 🟢 Visualization of all hand landmarks
* 🔵 Highlighting of the index finger tip
* 📷 Real-time webcam processing

---

## 🛠️ Technologies

* **Python**
* **OpenCV**
* **MediaPipe**
* **Computer Vision**

---

## 🧠 How It Works

The project captures frames from the webcam and processes them using MediaPipe's **Hand Landmarker** model.

### Processing Pipeline

```text
Webcam
   ↓
OpenCV
   ↓
BGR → RGB Conversion
   ↓
MediaPipe Hand Landmarker
   ↓
21 Hand Landmarks
   ↓
Pixel Coordinate Conversion
   ↓
Index Finger Tip Tracking
   ↓
Visual Output
```

---

## 📍 Hand Landmarks

MediaPipe detects **21 key landmarks** for every detected hand.

Each landmark contains normalized coordinates:

```text
X → 0.0 to 1.0
Y → 0.0 to 1.0
```

The project converts these normalized coordinates into actual pixel positions:

```python
cx = int(landmark.x * w)
cy = int(landmark.y * h)
```

This allows the landmarks to be drawn directly on the webcam frame.

---

## ☝️ Index Finger Tracking

The index finger tip corresponds to **landmark #8**.

The project extracts it using:

```python
index_tip = hand[8]
```

Its normalized coordinates are then converted to pixels:

```python
tip_x = int(index_tip.x * w)
tip_y = int(index_tip.y * h)
```

The coordinates are printed to the terminal:

```text
Index Finger Tip -> X: 320, Y: 180
```

The index finger tip is also highlighted with a larger circle on the webcam feed.

---

## 📂 Project Structure

```text
Real-Time-Hand-Landmark-and-Index-Finger-Tracking/
│
├── hand_landmark.py
├── hand_landmarker.task
└── README.md
```

> Make sure the `hand_landmarker.task` model file is available in the project directory.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/aytenakl/Real-Time-Hand-Landmark-and-Index-Finger-Tracking.git
```

### 2. Navigate to the project

```bash
cd Real-Time-Hand-Landmark-and-Index-Finger-Tracking
```

### 3. Install dependencies

```bash
pip install opencv-python mediapipe
```

---

## 📦 MediaPipe Model

This project requires the MediaPipe Hand Landmarker model:

```text
hand_landmarker.task
```

Place the model file in the same directory as the Python script.

The model is loaded using:

```python
model_path = 'hand_landmarker.task'
```

---

## ▶️ Usage

Run the Python script:

```bash
python hand_landmark.py
```

A webcam window will open automatically.

Move your hand in front of the camera to see the detected landmarks.

The **index finger tip** will be highlighted separately.

To stop the program, press:

```text
Q
```

---

## 🎯 Example Output

The webcam displays the detected hand landmarks and highlights the index finger tip.

The terminal prints its current position:

```text
Index Finger Tip -> X: 315, Y: 172
Index Finger Tip -> X: 318, Y: 169
Index Finger Tip -> X: 322, Y: 165
```

As the hand moves, the coordinates change in real time.

---

## 💡 Applications

Hand landmark tracking can be used as a foundation for:

* 👋 Gesture recognition
* 🖱️ Virtual mouse control
* 🎮 Gesture-based gaming
* 🖥️ Touchless interfaces
* 🤖 Robotics control
* 💡 Smart home control
* 🥽 Human-Computer Interaction
* ✋ Sign language recognition
* 🎯 Object selection using hand gestures

---

## 🔮 Future Improvements

Possible improvements include:

* Track specific individual fingers
* Calculate finger movement
* Detect hand gestures
* Track hand movement direction
* Calculate distances between landmarks
* Implement virtual mouse control
* Add gesture-based commands
* Integrate with Arduino and robotics projects
* Use MediaPipe video/live-stream mode for more efficient real-time tracking

