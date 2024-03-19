'''# <Reading camera frames>
import cv2

# Create a VideoCapture object
capture = cv2.VideoCapture(0)

# To check connection with camera, Use capture.isOpened() method.
print(capture.isOpened())

# this frame has the same structure as an image OpenCV.
# 이미지와 동일한 방법

#gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# [type:bool] indicates whether the frame gas been correctly read from the capture object.
capture.read()
'''


#<Accessing some properties of the capture object>
import cv2
import argparse

# make object
parser = argparse.ArgumentParser()

# add arguments / dtype 지정
parser.add_argument("index_camera", help = "index of the camera to read from", type = int)
args = parser.parse_args()

# Create Videocapture object.
capture = cv2.VideoCapture(args.index_camera)

# Get some properties of VideoCapture (frame width, frame height and frames per second(fps))
frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)

# Print these values;
print("CV_CAP_PROP_FRAME_WIDTH : '[]'".format(frame_width))
print("CV_CAP_PROP_FRAME_HEIGHT : '[]'".format(frame_height))
print("CV_CAP_PROP_FPS : '[]'".format(fps))

# Check if camera opened successfully
if capture.isOpened() is False:
    print("Error opening the camera")

# Read until video is completed
while capture.isOpened():
    # Capture frame by frame from the camera
    ret, frame = capture.read()

    if ret is True:
        # Display the captured frame:
        cv2.imshow('Input frame from the camera', frame)

        # Convert the frame captured from the camera to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the grayscale frame
        cv2.imshow('Grayscale input camera', gray_frame)

        # Press 'q' on keyboard to exit the program
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break

        else:
            break


capture.release()
cv2.destroyAllWindows()