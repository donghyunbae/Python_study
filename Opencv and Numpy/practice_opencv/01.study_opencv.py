'''
RAW

- 최소한으로 처리한 데이터를 포함하고 있다. Raw 파일들은 영어 낱말의 뜻 그대로 전혀 가공되지 않은 상태

JPEG / JPG(Joint Photographic Coding  Experts Group)
- 손실 압축 기법을 사용, 여러번 편집하고 저장할 경우 퀄리티가 점점 떨어진다, 1677 만 7216 색과 256 색 그레이로 저장 가능

GIF(Graphics Interchange Format)
- 무손실 압축 기술의 사용, 움직이는 이미지에 최적화, 8 bit 256 가지 색상만 가능

PNG(Portable Network Graphics)
- 비손실 그래픽 파일, PNG파일은 8 비트(투명도옵션이 존재), 24 비트 트루컬러(1600 만 색), 알파채널이 옵션인 48 비트 트루컬러를 지원

BMP(Bit Map)
- 무손실 무압축 포맷이기 때문에 이미지 크기가 크다.그렇기 때문에 화질도 좋다. 24 bit 컬러 지원
'''
import numpy
import cv2
img = cv2.imread('mydog.png')
print(img)
print(img.shape)                    #(168, 300, 3) = rows, columns, channel
print(img.size)                     # 151200 = 168*300*3
print(img.dtype)                    # uint8 = 0~255
cv2.imshow('test_image', img)
cv2.waitKey(0)

#To access (read) a pixel value, need to provide the row ans column of the desired pixel
# In case of BGR image, it returns an array of (B, G, R) values
# Get the value of the pixel (x=40, y=6)
(b, g, r) = img[6, 40]
print("Pixel at (6,40) - Red : {}, Green : {}, Blue : {}".format(r, g, b))


b = img[6,40,0]
g = img[6,40,1]
r = img[6,40,2]


img[6,40] = (0, 0, 255)
(b, g, r) = img[6,40]
print("Pixel at (6,40) - Red : {}, Green : {}, Blue : {}".format(r, g, b))

#play with certain region of images rather than one pixel at a time
#get the top left corner of the image;
top_left_corner = img[0:50, 0:50]
cv2.imshow("top_left_corner", top_left_corner)
cv2.waitKey(0)

# Copy this ROI(Region of Interst) into another region of the image;
img[20:70, 20:70] = top_left_corner
cv2.imshow("modified image", img)
cv2.waitKey(0)

# Set top left corner of the image to blue
img[0:50,0:50] = (255,0,0)
cv2.imshow("modified image", img)
cv2.waitKey(0)
