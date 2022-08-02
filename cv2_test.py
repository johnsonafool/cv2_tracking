import cv2
import imutils
import matplotlib.pyplot as plt
import numpy as np

frameWidth = 1280
frameHeight = 960
cap = cv2.VideoCapture(1)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)


firstFrame = None
while True:
    success, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.GaussianBlur(img, (21, 21), 0)
    
    if firstFrame is None:
        firstFrame = img
        continue
    
    frameDelta = cv2.absdiff(firstFrame, img)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
    # print(thresh, "[thres]")
    
    thresh = cv2.dilate(thresh, None, iterations=2)
    
    cnts = cv2.findContours(thresh.astype(np.uint8).copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    # print(cnts, "[cnts]")
    
    for c in cnts:
        # if cv2.contourArea(c) < 500:
        #     continue
        print(c)
        # print(type(c))
        (x, y, w, h) = cv2.boundingRect(c)
        # (x, y, w, h) = cv2.boundingRect(c)
        
        
        # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("webcam", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()
