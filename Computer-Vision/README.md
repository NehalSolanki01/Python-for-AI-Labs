# Computer-Vision

# 1. Face and Eye Detection with OpenCV

This Python program uses OpenCV and Haar Cascade Classifiers to detect faces and eyes in real-time from a webcam feed. It highlights detected faces and eyes with rectangles on the video feed.

## Features

- **Real-time Face Detection**: Detects faces using a pre-trained Haar cascade classifier.
- **Real-time Eye Detection**: Detects eyes within the detected face region.
- **Live Webcam Feed**: Displays the webcam feed with highlighted faces and eyes.
- **Exit**: Press the spacebar to close the webcam feed and exit the program.

## Prerequisites

- **OpenCV**: Make sure OpenCV is installed. You can install it using:
  ```bash
  pip install opencv-python
  ```
- **Haar Cascade Files**: This program uses pre-trained XML files for face and eye detection.
  - `haarcascade_frontalface_default.xml`
  - `haarcascade_eye.xml`
  
  You can download these files from the [OpenCV GitHub repository](https://github.com/opencv/opencv/tree/master/data/haarcascades).

## How It Works

1. **Initialize Haar Cascades**: The program loads pre-trained Haar cascade classifiers for face and eye detection.
2. **Capture Video**: It accesses the webcam and captures video frames.
3. **Detect Faces**: Each frame is converted to grayscale, and faces are detected.
4. **Detect Eyes**: For each detected face, eyes are detected within the face region.
5. **Display Video Feed**: The program displays a real-time video feed with rectangles around faces and eyes.
6. **Exit**: Press the spacebar to stop the video feed and close the program.

## Code Overview

- **Load Haar Cascades**: The `CascadeClassifier` objects are initialized with the face and eye Haar cascades.
- **Video Capture**: The program initializes a webcam feed using `cv2.VideoCapture(0)`.
- **Detection and Drawing**: 
  - `detectMultiScale` is used to detect faces and eyes.
  - `cv2.rectangle` draws rectangles around detected faces and eyes.
- **Exit Condition**: The `while` loop runs until the spacebar is pressed.

## Usage

1. **Save the Code**: Save the code in a Python file, e.g., `face_eye_detection.py`.
2. **Download Haar Cascade Files**: Ensure the Haar cascade XML files are in the same directory as your code or specify their path in the code.
3. **Run the Program**:
   ```bash
   python face_eye_detection.py
   ```
4. **View the Video Feed**: The program will open a webcam window with real-time face and eye detection.
5. **Exit**: Press the spacebar to close the window and end the program.

## Example Output

The program displays a live feed with green rectangles around detected faces and blue rectangles around detected eyes.

___________________________________________________________________________________________________________________________________________________________________

# 2. Pedestrian Detection with OpenCV

This Python program uses the Histogram of Oriented Gradients (HOG) feature descriptor and a pre-trained Support Vector Machine (SVM) detector in OpenCV to detect pedestrians in a video. It processes each frame of a video and highlights detected pedestrians with bounding boxes.

## Features

- **Pedestrian Detection**: Detects pedestrians in each frame of a video using HOG and SVM.
- **Real-time Bounding Box Drawing**: Draws bounding boxes around detected pedestrians in each frame.
- **Video Playback**: Allows for video playback with pedestrian detection.
- **Exit**: Press the "q" key to exit the program.

## Prerequisites

- **OpenCV**: Ensure OpenCV is installed. You can install it using:
  ```bash
  pip install opencv-python
  ```
- **Imutils**: This library is used for easier image resizing. Install it using:
  ```bash
  pip install imutils
  ```
- **Video File**: Ensure you have a video file to test with. Update the file path in the code if necessary.

## How It Works

1. **Initialize HOG Detector**: The program initializes a HOG descriptor configured with a pre-trained SVM for pedestrian detection.
2. **Video Capture**: The program opens a video file for processing.
3. **Frame-by-Frame Detection**:
   - Each frame is resized for efficient processing.
   - Pedestrians are detected using `hog.detectMultiScale`, which returns bounding box coordinates for each detection.
4. **Bounding Boxes**: Bounding boxes are drawn around detected pedestrians in each frame.
5. **Display and Exit**: The program displays each processed frame in a window. Press "q" to stop the video and close the program.

## Code Overview

- **Initialize HOG Detector**: The HOG descriptor is initialized and set with a pre-trained SVM for pedestrian detection.
- **Video Capture**: A video file is opened, and frames are read in a loop.
- **Detection**: `detectMultiScale` is used to detect pedestrians in each frame.
- **Drawing Bounding Boxes**: For each detected pedestrian, a rectangle is drawn.
- **Exit Condition**: The loop runs until the "q" key is pressed or the video ends.

## Usage

1. **Save the Code**: Save the code in a Python file, e.g., `pedestrian_detection.py`.
2. **Update Video Path**: Ensure the video path in the code matches the location of your video file.
3. **Run the Program**:
   ```bash
   python pedestrian_detection.py
   ```
4. **View the Video**: The program will open a window displaying the video with bounding boxes around detected pedestrians.
5. **Exit**: Press the "q" key to close the window and end the program.

## Example Output

The program displays the video with red bounding boxes around detected pedestrians.

This pedestrian detection system can be adapted for different video sources and detection thresholds for optimized performance.

___________________________________________________________________________________________________________________________________________________________________

# 3. Image-to-Video Conversion

This Python program converts a series of images into a video file using OpenCV. Given a list of image filenames, the program reads each image, resizes them to a consistent dimension, and writes them to a video file.

## Features

- **Image-to-Video Conversion**: Combines multiple images into a video.
- **Customizable Frame Rate and Codec**: Allows setting frame rate (currently set to 1 frame per second) and video codec (default: XVID).
- **Image Resizing**: Automatically resizes images to ensure consistent dimensions for smooth video playback.

## Prerequisites

- **OpenCV**: Make sure you have OpenCV installed. Install via pip if needed:
  ```bash
  pip install opencv-python
  ```

- **Image Files**: Place your image files in the same directory as this script, or provide the full paths to each image file.

## How It Works

1. **Define Image List**: The program specifies a list of images to include in the video.

2. **Read Image Dimensions**: The program reads the first image in the list to set the video frame dimensions.

3. **VideoWriter Setup**: A `VideoWriter` object is created with the specified codec (`XVID`) and frame rate.

4. **Image Processing**:
   - Each image in the list is read and resized to match the dimensions of the first image.
   - Each resized image is then written to the video file.

5. **Save and Release**: After writing all images, the program releases the `VideoWriter` and saves the video as `output_video.avi`.

## Usage

1. **Update Image List**: In the code, update the `image_files` list with your own image filenames:
   ```python
   image_files = ['image1.jpg', 'image2.jpg', 'image3.jpg', ...]
   ```

2. **Run the Program**: Execute the script:
   ```bash
   python image_to_video.py
   ```

3. **Output**: The video file, `output_video.avi`, will be saved in the same directory as the script.

4. **Playback**: You can use a media player like VLC to play the generated video.

## Example Output

The program will print:
```
Video created successfully!
```

## Notes

- **Supported Codecs**: The default codec is `XVID`. You can change it to other supported codecs (e.g., `mp4v` for `.mp4` files).
- **Frame Rate**: Currently set to 1 frame per second. Adjust this by changing the frame rate argument in `VideoWriter`.

## License

This project is open for personal and educational use.

