import cv2
import numpy as np

colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

image = np.zeros((300,300,3), dtype = "uint8")
cv2.namedWindow('Image_mouse')

#<Dynamic dynamic shapes>       cv2.setMouseCallback(windowName, onMouse, param=None)
# first step : create the callback funtion:

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print("event: EVENT_LBUTTONDBLCLK")
        cv2.circle(image, (x,y), 10, colors['magenta'], -1)

    if event == cv2.EVENT_MOUSEMOVE:
        print("event : EVENT_MOUSEMOVE")

    if event == cv2.EVENT_LBUTTONUP:
        print("event : EVENT_LBUTTONUP")


    if event == cv2.EVENT_LBUTTONDOWN:
        print("event : EVENT_LBUTTONDOWN")

cv2.setMouseCallback('Image_mouse', draw_circle)

while True:
    cv2.imshow('Image_mouse', image)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    # Destroy all generated windows:

cv2.destroyAllWindows()