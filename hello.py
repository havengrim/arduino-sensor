import cv2
import controller as cnt
from cvzone.HandTrackingModule import HandDetector

# Initialize hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Capture video from the webcam
video = cv2.VideoCapture(0)

# Dictionary to map finger patterns to text
finger_text = {
    (0, 0, 0, 0, 0): 'Finger count: 0',
    (0, 1, 0, 0, 0): 'Finger count: 1',
    (0, 1, 1, 0, 0): 'Finger count: 2',
    (0, 1, 1, 1, 0): 'Finger count: 3',
    (0, 1, 1, 1, 1): 'Finger count: 4',
    (1, 1, 1, 1, 1): 'Finger count: 5'
}

while True:
    # Read frame from video
    ret, frame = video.read()
    
    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)
    
    # Detect hands
    hands, img = detector.findHands(frame)
    
    # If a hand is detected
    if hands:
        # Get the first hand's landmarks
        lmList = hands[0]
        
        # Get the finger-up status (1 for up, 0 for down)
        fingerUp = detector.fingersUp(lmList)
        
        # Print the finger-up pattern for debugging
        print(fingerUp)
        
        # Call the controller function with the fingerUp data
        cnt.led(fingerUp)
        
        # Display the finger count based on the detected pattern
        text = finger_text.get(tuple(fingerUp), 'Unknown')
        cv2.putText(frame, text, (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)

    # Show the frame in a window
    cv2.imshow("frame", frame)
    
    # Break the loop when 'k' key is pressed
    k = cv2.waitKey(1)
    if k == ord("k"):
        break

# Release the video capture object and close all OpenCV windows
video.release()
cv2.destroyAllWindows()
