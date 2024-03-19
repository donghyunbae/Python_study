import cv2
import numpy as np
#from numpy import *                                    -> 내가 패키지를 만들때 이름들이 충돌할 경우가 있음 그렇기 때문에 권장 XXXX!!

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)                #camera ID 0 : 노트북, 1: 개인 카메라 #DSHOW : direct show -> 바로 카메라를 다이렉트로 읽음
count = 0
while True:
    ret, image = cap.read()                             #ret = return   image읽고 ok이면 ret을 true한다.
    if ret:
        cv2.imshow("Myimage", image)            #"이미지 이름"
    key = cv2.waitKey(33)
    print(key)

    if (key & 0xff) == ord('q'):                                #ascii값 ~ 255중에 q값(113)이 일치하면 break.

        break                                                   #ord = ordinary 10진수 #0xFF : 비트연산과 관련되어있음 (16진수)
                                                                #16진수 : 0~9다음 10이 아니라, ABCDEF 총 16까지

                                                                #비트연산 (+쉬프트 연산)
                                                                #ex) 0x3f & 0x0f == 0011 1111 & 0000 1111 -> 0000 1111
    elif (key & 0xff) == ord('c'):
        file_name = '../image_data/image_{}.png'.format(count)     #경로에 저장 "../ 는 한단계 위쪽 폴더로 이동"
        cv2.imwrite(file_name, image)                                           #image save
        count = count + 1