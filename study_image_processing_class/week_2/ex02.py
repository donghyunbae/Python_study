import cv2


file_name = 'image_data/image_0.png'

image = cv2.imread(file_name, cv2.COLOR_BGR2GRAY)
grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)                                 #cvtColor = convertcolor !!! 순서 : BGR
edge = cv2.Canny(grayimage, 50, 150)


cv2.imshow('myimage', image)
cv2.imshow('grayimage', grayimage)
cv2.imshow('edgeimage', edge)

#color와 gray는 numpy array의 shape정보가 다름
print(image.shape)                                                                  #shape정보가 있음 3채널
print(grayimage.shape)
print(grayimage.dtype)

'''
dtype = datatype
#int8 = 8비트짜리의 정수 (0-255) 만약 16진수가 0x100 (256)이면 
#int16 = 16비트(0-65535)
#uint8 = unsigned (-127 ~ 127)
#uint16 = (-32767 ~ 32767)

#실수
float32
float64
'''

cv2.waitKey(0)