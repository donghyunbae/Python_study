'''
dtype = datatype
#int8 = 8비트짜리의 정수 (0-255) 만약 16진수가 0x100 (256)이면
#int16 = 16비트(0-65535)
#uint8 = unsigned (-127 ~ 127)
#uint16 = (-32767 ~ 32767)

#실수
float32
float64

8비트와 16비트 / 정수, 실수 부분의 형변환을 잘 할수 있어야 함.

복잡한 데이터들은 소숫점으로 다뤄야할 경우도 있음
이런 경우에는 처음에 소수점들을 스케일링하고 -> 형변환 -> int로
'''
import cv2
import numpy as np

new_image = np.random.randn(480, 640)
img = np.array([[1,2,3], [1,2,257]], dtype=np.float32)
min = np.min(new_image)
max = np.max(new_image)

#new_image scaling
new_image = 255 * (new_image - min) / (max-min)

uint_image = new_image.astype(np.int8)                                      #타입 바꿔주는 함수 (numpy)

cv2.imshow('test', new_image)
cv2.imshow('uint_image', uint_image)
cv2.waitKey(0)

#image slicing/split
a = [1,2,3,4,5,6,7]
print(a[0:5:2])

