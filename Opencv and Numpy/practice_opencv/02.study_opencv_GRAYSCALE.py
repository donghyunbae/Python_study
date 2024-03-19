import cv2
'''
What is pixel & Resolution ?
<pixel>
pixel (picture + elements) : 컴퓨터 이미지, 디스플레이를 구성하고 있는 최소 단위.
모든 이미지들은 픽셀이라고 하는 매우 작은 사각형의 점들로 구성되어 있음.

<Resolution>
Resolution : 픽셀들의 조합으로 보여지는 이미지는 픽셀의 객수와 밀도에 따라 이미지 자체의 크기와 품질에 직접적인 영향을 미친다.

'''
img = cv2.imread('mydog.png')
gray_img = cv2.imread('mydog.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('mydog', img)
cv2.imshow('gray_mydog', gray_img)

print(img.shape)
print(gray_img.shape)

#Get height and width of the input grayscale image
(h, w) = gray_img.shape
#print (h,w) values using 'str' fomatting
print("dimensions of the image - Height : {}, Width : {}".format(h,w))
#total_number_of_elements is obtained by img.size;
total_number_of_pixel = gray_img.size
print("total_number_of_elements(pixels) : {}".format(total_number_of_pixel))            #total_number_of_pixel is equal to the multiplication of 'h','w' and 'channel'
#dtype of image
img_dtype = img.dtype
print("Image dtype : {}".format(img_dtype))                                             #Img dtype : (uint8) = char

#Access a pixel value by row and column coordinates.
#For BGR image, it returns an array of (B,G,R) values.
#Get the value of the pixel(x=40, y=6)
i = gray_img[750,750]
print("Pixel at (6,40) - Intensity:{}".format(i))

#Modify the value of the pixel to 'zero'(x=40, y=6)
gray_img[750, 750] = 0
i = gray_img[750, 750]
print("Pixel at (6,40) - Intensity:{}".format(i))
#show the modified image
cv2.imshow('modified_gray_img', img)

# Get the top left corner of the image;
top_left_corner = gray_img[0:750, 0:750]

#We show this ROI
cv2. imshow("top_left_corner", top_left_corner)

gray_img[0:750, 750:1500] = top_left_corner
cv2.imshow("modified top_left_corner", gray_img)

gray_img[0:750,0:750] = 255
cv2.imshow("modified_color_top_left_corner", gray_img)

cv2.waitKey(0)