import cv2import numpy as npimg = np.zeros((500,500), dtype = np.uint8)img [100:300,50:350]=188ret,thresh = cv2.threshold(img,127,255,0)contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)img1= cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)img =cv2.drawContours(img1, contours, -1, (0,255,0), 3)#c,h = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APROX_SIMPLE)cv2.imshow("zain",img)cv2.waitKey(0)#cv2.destoryAllWindows()cv2.destroyAllWindows()  