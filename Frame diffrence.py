
import numpy as np
import cv2

cap = cv2.VideoCapture('test.mp4')

currentFrame = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    gray1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    for i in range(cap.isOpened()): 
        ret, frame1=cap.read()
        gray2 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        sub = gray1 - gray2
        frame = frame1
        cv2.imwrite("frame%d.jpg" % currentFrame, sub)  
        currentFrame += 1  
        cv2.imshow('frame',sub)
        #cv2.waitKey(0)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
