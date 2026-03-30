import cv2

# Load the pre-trained Haar cascade classifiers for face and eye detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Initialize the webcam
vid = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame from the webcam
    ret, frame = vid.read()
    
    # Convert the captured frame to grayscale (needed for detection)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    
    # Loop through each detected face
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Define the region of interest (ROI) in the frame for eye detection (inside the face)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        # Detect eyes within the face ROI
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        # Loop through each detected eye and draw a rectangle around it
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)
    
    # Display the resulting frame with face and eye rectangles
    cv2.imshow("Webcam", frame)
    
    # Exit the loop if the spacebar (key 32) is pressed
    if cv2.waitKey(25) == 32:
        break

# Release the webcam and close all OpenCV windows
vid.release()
cv2.destroyAllWindows()
