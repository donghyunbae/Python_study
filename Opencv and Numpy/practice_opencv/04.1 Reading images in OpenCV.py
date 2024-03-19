'''
커맨드라인을 통해 이미지 파일의 경로를 입력받아 해당 이미지를 불러오고 화면에 표시하는 것

argparse library를 이용하여 커맨드 라인 인자를 parsing, cv2를 이용하여 이미지를 처리
'''
import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("path_image", help = 'path to input image to be displayed')

args = parser.parse_args()
image = cv2.imread(args.path_image)

args = vars(parser.parse_args())

image2 = cv2.imread(args["path_image"])

cv2.imshow("loaded image", image)
cv2.waitKey(0)
cv2.imshow("loaded image2", image2)
cv2.waitKey(0)

cv2.destroyAllWindows()