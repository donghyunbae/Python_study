import cv2
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("index_camera", help = "index of the camera to read from", type = int)
args = parser.parse_args()

# create a videocapture object to read from the camera (default 0)
capture = cv2.VideoCapture(args.index_camera)

# get some properties of videocapture
frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)

# print values;
print("FRAME WIDTH : {} ".format(frame_width))
print("FRAME HEIGHT : {} ".format(frame_height))
print("FRAME FPS : {} ".format(fps))

# Check if camera is opened successfully
if capture.isOpened is False:
    print("Error opening the camera")

# Index to save current frame
frame_index = 0

# Read until video is completed
while capture.isOpened():
    cv2.imshow("input frame from the camera", frame)

    # convert the frame captured from the camera to grayscale:
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # display the grayscale
    cv2.imshow("grayscaled frame from the camera", gray_frame)

    # Press c on keyboard to save current frame
    if cv2.waitKey(0) & 0xFF == ord('c'):
        frame_name = "camera_frame{}".format(frame_index)
        gray_frame_name = "grayscaled_camera_frame{}".format(frame_index)
        cv2.imwrite(frame_name, name)
        cv2.imwrite(gray_frame_name, gray_frame)
        frame_index += 1

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

    #Break the loop
    else:
        break

# Release everythingL
capture.release()
cv2.destroyAllWindows()
