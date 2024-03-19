'''
This class is showing images with both OpenCV and matplotlib.
'''

import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load image
img = cv2.imread('mydog.png')

# Split the loaded image into its three channels (b,g,r):
b,g,r = cv2.split(img)
print(b,g,r)
# Merge ahain the three chennels but in the RGB format; (Merge : 병합)
img_matplotlib = cv2.merge([r,g,b])             # b,g,r 값을 r,g,b의 값으로 바꾼 것....


# Show both images (img & img_matplotlib) using cv2.imshow()
cv2.imshow('bgr image', img)
cv2.imshow('img_matplotlib', img_matplotlib)

# Show both images (img & img_matplotlib) using matplotlib
# This will show the image in wrong color;
plt.subplot(121)
plt.imshow(img)
plt.title('original_img')

# This will show the image in true color;
plt.subplot(122)
plt.imshow(img_matplotlib)
plt.title('matplot_img')

plt.show()

# ------>>>>>  openCV는 BGR을 사용하고!!! matplotlib는 RGB를 사용한다!!!!!!!!

# Show both images (img & img_matplotlib) unsing cv2.imshow()
cv2.imshow('bgr img', img)
cv2.imshow('rgb_img', img_matplotlib)
cv2.destroyAllWindows()                         # 모든 윈도우 창 종료!

# To stack horizintally (img to the left of tmg_matplotlib);     stack : 쌓다 , concat : 연결하다
# 두개 사진을 수평으로 이어붙힘
img_concats = np.concatenate((img, img_matplotlib), axis = 1)

# Show concatenate image
cv2.imshow('bgr img and rgb image', img_concats)

# Using numpy capabilities to get the channels and two build the RGB image
# Get the three channels (instead of using cv2.split);
B = img[:,:,0]
G = img[:,:,1]
R = img[:,:,2]

# Transform the image BGR to RGB using Numpy capabilities;
# img_RGB = img[:,:,::-1]       #전체를 다 변경하는 것임

# 만약 특정부분의 이미지만 색상을 변경하고 싶다면 ...
# 원하는 특정부분 지정하기 (시작~끝)
x1, y1 = 0, 0
x2, y2 = 700, 700
# 특정 부분에 대해 색상 채널 변경
img_RGB_part = img[y1:y2, x1:x2, ::-1]
# 원본 이미지에 변경된 부분을 다시 삽입
img[y1:y2, x1:x2] = img_RGB_part

# Show the RGB image is transformed;
cv2.imshow('img_RGB(wrong color)', img)
#cv2.imshow('img_RGB(prat_wrong color)', img_RGB_part)


cv2.waitKey(0)
