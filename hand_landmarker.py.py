import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

WIDTH = 640
HEIGHT = 360

# 1. Setup the detector
model_path = 'hand_landmarker.task'
base_options = python.BaseOptions(model_asset_path=model_path)
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.IMAGE, # Simple synchronous mode, the model will wait till the results is calculated.
    num_hands=2
)

detector = vision.HandLandmarker.create_from_options(options)

# 2. Open webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)     # Set frame width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)   # Set frame height
cap.set(cv2.CAP_PROP_FRAME_COUNT, 30)        # Set frame rate

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        continue

    # Flip horizontally for mirror view & convert BGR to RGB
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Get frame dimensions to convert normalized (0-1) coordinates to pixels
    h, w = HEIGHT, WIDTH

    # Wrap OpenCV image into MediaPipe Image format
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    # 3. Detect hands synchronously
    detection_result = detector.detect(mp_image) # Contains hand_landmarks, and the handeness

    # 4. Check if any hands were detected
    if detection_result.hand_landmarks:
        for hand in detection_result.hand_landmarks:
            
            # Loop through all 21 keypoint dots on the hand
            # It returns pairs in the form (index, element).
            for idx, landmark in enumerate(hand): # Landmark is an object holding 21 landmarks
                cx = int(landmark.x * w)
                cy = int(landmark.y * h)

                # Draw a small circle on every landmark dot (Green)
                cv2.circle(frame, (cx, cy), 5, (0, 255, 0), cv2.FILLED)

            # Example: Inspect landmark #8 (Index Finger Tip)
            index_tip = hand[8]
            tip_x, tip_y = int(index_tip.x * w), int(index_tip.y * h)

            # Print to terminal
            print(f"Index Finger Tip -> X: {tip_x}, Y: {tip_y}")

            # Highlight the index finger tip with a larger circle (Blue)
            cv2.circle(frame, (tip_x, tip_y), 10, (255, 0, 0), cv2.FILLED)

    # 5. Display the result
    cv2.imshow("Hand Landmarker", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
