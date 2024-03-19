import numpy as np
import matplotlib.pyplot as plt
import cv2

colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

image = np.zeros((500,500,3), dtype = "uint8")
image_RGB = image[:,:,::-1]

#cv2.line(image, pt1, pt2, color, thickness)
cv2.line(image, (0,0), (500,500), colors['red'], 3)
cv2.line(image, (500,0), (0,500), colors['blue'], 3)
cv2.line(image, (0,250), (500,250), colors['green'], 10)
cv2.line(image, (250,0), (250,500), colors['magenta'], 10)

#cv2.rectangle(image, pt1, pt2, color, thickness)
cv2.rectangle(image, (10, 50), (60,300), colors['red'], -3)
cv2.rectangle(image, (80, 50), (130,300), colors['blue'], -1)
cv2.rectangle(image, (150, 50), (350,100), colors['green'], -1)
cv2.rectangle(image, (150, 150), (350,300), colors['magenta'], -1)

#cv2.circles(img, center, radius, color, thickness, lineType = 8, shift = 0)
cv2.circle(image, (400,400), 50, colors['red'], 3)
cv2.circle(image, (400,400), 40, colors['blue'], -3)

#Understanding advanced shapes
image2 = np.zeros((300,300,3), dtype = "uint8")
#set backgroundcolor
image2[:] = colors['gray']
image2RGB = image2[:,:,::-1]

#Drawing a clip line
#cv2.clipLine(imgRect, pt1, pt2) -> retval, pt1, pt2                -> imgRect에 절단되는 좌표를 계산하여 pt1, pt2반환한다.
cv2.line(image2, (0,0), (300,300), colors['green'], 3)
cv2.rectangle(image2, (0,0), (100,100), colors['blue'], 3)
retval, p1, p2 = cv2.clipLine((0,0,100,100),(0,0), (300,300))
if retval:
    cv2.line(image2, p1, p2, colors['yellow'],3)

#Drawing arrows     cv2.arrowedLine(작업할 이미지, 시작점, 끝나는점, 색상, 두께, 선의 유형, shift : 소수점이하 비트수, tiplenght: 화살표 끝의 길이)
cv2.arrowedLine(image2, (50,250), (250,250), colors['red'], 3, 8, 0, 0.1)
cv2.arrowedLine(image2, (50,250), (50,50), colors['red'], 3, cv2.LINE_AA, 0, 0.1)

#Drawing ellipses   cv2.ellipse(img, center, axes(가로길이, 세로길이), angle, startAngle, endAngle, color, thickness=1, lineType=8, shift =0)
cv2.ellipse(image2, (150,150), (80,80), 0, 0, 360, colors['magenta'], -1)
cv2.ellipse(image2, (150,200), (40,80), 20, 0, 360, colors['red'], -1)
cv2.ellipse(image2, (115,200), (40,80), -20, 0, 360, colors['red'], -1)

#Drawing Polygons   cv2.polylines(img, pts, isClosed, color, thickness-1, lineType = 8, shift)
image3 = np.zeros((600,600,3), dtype="uint8")
image3RGB = image3[:,:,::-1]
image3[:] = colors['gray']
points = np.array([[300,300], [300,200], [200,100], [150,100], [100,200], [300,500], [200,100], [100,150], [100,200],[200,300]]).reshape(1,-1,2)
cv2.polylines(image3, points, True, colors['blue'], 3)


plt.figure(1)
#plt.subplot(121)
plt.imshow(image)
plt.title('my_BGRdrawing')
plt.figure(2)
#plt.subplot(122)
plt.imshow(image_RGB)
plt.title('my_RGBdrawing')
plt.figure(3)
plt.imshow(image2)
plt.title('my_BGRdrawing2')
plt.figure(4)
plt.imshow(image2RGB)
plt.title('my_RGBdrawing2')
plt.figure(5)
plt.imshow(image3)
plt.title('my_BGRdrawing3')
plt.figure(6)
plt.imshow(image3RGB)
plt.title('my_RGBdrawing3')
plt.show()
