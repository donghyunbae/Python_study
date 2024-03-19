import cv2

#rtsp : 영상 스트리밍 서버..
#인터넷 통신을 통해서 영상을 가져와서 볼 수 있음

#addr = 'rtsp://192.168.0.100/videodevice'
#cap = cv2.VideoCapture(addr)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if cap.isOpened is True:
    while True:
        ret, frame = cap.read()
        if ret:
            b = frame[:,:,0]
            g = frame[:,:,1]
            r = frame[:,:,2]

            roi = frame[:5, :5, :1]                     #480 x 640중에서 5x5 만 꺼내기
            #0으로 갈수록 어두워지고 255에 가까워질수록 밝아짐
            print(roi)
            #print(frame.shape)                    #행렬 확인하기              #480, 640, 3 = 480 x 640 3개(B, G, R 순서)
            #cv2.imshow('blue',b)
            cv2.imshow('green', g)
            #cv2.imshow('red', r)
            #cv2.imshow('Capture', frame)

        cv2.waitKey(33)

    else :
        print("cannot connect")


# ex) save and read
