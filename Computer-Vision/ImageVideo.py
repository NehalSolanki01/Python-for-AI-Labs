import cv2
import os

# List of image filenames
image_files = ['robo1.jpeg', 'robo3.jpg', 'robo5.jpg', 'robo6.jpg', 'robo7.jpeg', 'robo8.jpg']

# Read the first image to get the shape for video dimensions
first_image = cv2.imread(image_files[0])

# Get the dimensions from the first image
height, width, channels = first_image.shape

# Set up the VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # You can change codec as needed
output_video = cv2.VideoWriter('output_video.avi', fourcc, 1, (width, height))  # 1 fps in this case

# Loop through all image files and write them to the video
for image_file in image_files:
    img = cv2.imread(image_file)
    
    # Make sure the image is the correct size (in case of mismatches)
    img_resized = cv2.resize(img, (width, height))
    
    # Write the image to the video
    output_video.write(img_resized)

# Release the VideoWriter object
output_video.release()

# Optionally, close any OpenCV windows
cv2.destroyAllWindows()

print("Video created successfully!")
