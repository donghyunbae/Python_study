import argparse
import cv2

#Creat parser object
parser = argparse.ArgumentParser()

#결국 2개의 arguments를 만들면 2개의 arguments를 넣어주어야함.
#Add arguments of input(original) image
parser.add_argument("path input images", help = "path to input image to be displayed")
#Add arguments of output(processed) image
parser.add_argument("path output images", help = "path of the processed image to be saved")

#Parse the argument and store it in a dictionaty
# vars() : 파이썬 기본 내장함수로서 모듈, 클래스, 클래스 인스턴스의 객체(__dict__속성을 갖는 객체)에 대해 __dict__ 형태로 return해주는 함수
args = vars(parser.parse_args())

#load image
image_input = cv2.imread(args["path input images"])
cv2.imshow("loaded image", image_input)

gray_img = cv2.cvtColor(image_input, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image", gray_img)

# Save the processed image to disk !!!
# gray_img 를 "path output images" 경로에 저장
cv2.imwrite(args["path output images"], gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

