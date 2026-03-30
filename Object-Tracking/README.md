# ML-Algorithms(Object Tracking)

# Object Tracking using OpenCV

This Python script uses OpenCV to perform object tracking on a video file. It supports multiple object tracking algorithms (KCF, MOSSE, MedianFlow, and CSRT) by utilizing OpenCV’s built-in tracking API. The default tracker in this code is `CSRT`, which is suitable for objects that may undergo changes in scale and rotation.

## Features

- **Real-Time Object Tracking**: Allows selection of a Region of Interest (ROI) and tracks the object across frames.
- **CSRT Tracker**: By default, the script uses the CSRT (Channel and Spatial Reliability Tracker), which is accurate for complex tracking scenarios.
- **Customizable Tracker Choice**: You can modify the code to experiment with other tracking algorithms like KCF, MOSSE, and MedianFlow.

## Prerequisites

1. **OpenCV**: Make sure you have OpenCV installed. You can install it with:
   ```bash
   pip install opencv-python
   ```

2. **Video File**: Place your video file in the same directory as the script or specify the full path.

## How It Works

1. **Initialize the Video**: The program reads a video file frame-by-frame using OpenCV.
2. **Tracker Selection**: The program initializes a `CSRT` tracker (default). You can switch to other trackers by changing `cv2.TrackerCSRT_create()` to:
   - `cv2.TrackerKCF_create()`
   - `cv2.TrackerMOSSE_create()`
   - `cv2.TrackerMedianFlow_create()`
3. **ROI Selection**: On the first frame, a bounding box is selected by the user to define the object to track.
4. **Tracking Process**:
   - The tracker updates the position of the bounding box in each frame.
   - If the tracker successfully tracks the object, a bounding box is drawn around it.
   - If tracking fails, a "Lost" message appears.
5. **Exit**: Press the space bar to stop tracking and close the window.

## Usage

1. **Replace Video Path**: Set the video file path in the code:
   ```python
   video = cv2.VideoCapture("bb3.mp4")
   ```
   Replace `"bb3.mp4"` with the name or path of your video file.

2. **Run the Program**: Execute the script:
   ```bash
   python object_tracking.py
   ```

3. **Select ROI**: When prompted, select the object to track by drawing a bounding box.

4. **View Results**: The program will display the video with the tracking box. If tracking fails, "Lost" will appear on the frame.

## Code Customization

- **Change Trackers**: To try different algorithms, modify the tracker initialization line:
   ```python
   tracker = cv2.TrackerKCF_create()
   ```

## Example Output

- Successfully tracked objects will display a bounding box.
- If tracking fails, the display will show "Lost" until the object is found or the program ends.

## Notes

- **CSRT** is ideal for cases where the object moves slowly or requires precise tracking.
- **KCF** and **MOSSE** are faster but may be less robust under rotation or scale changes.
- **MedianFlow** works well for smooth movements but may fail if the object moves rapidly.

## License

This project is open for personal and educational use.

