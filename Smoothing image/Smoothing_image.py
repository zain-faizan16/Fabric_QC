import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("img1.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB )
fig, ax= plt.subplots(1,figsize=(12,8))
plt.imshow(img)
kernel= np.ones((3,3), np.float32)/9
img1 = cv2.filter2D(img, -1 , kernel)
kernel1 = np.array([[0,-1,0],
                   [-1,5,-1],
                   [0,-1,0]])
img2 = cv2.filter2D(img, -1 , kernel1)
img3 = cv2.GaussianBlur(img,(3,3),50)
img4= cv2.medianBlur(img,3)
img5=cv2.blur(img,(5,5))
cv2.imshow("zain",img)
cv2.imshow("zain1",img1)
cv2.imshow("zain2",img2)
cv2.imshow("zain3",img3)
cv2.imshow("zain5",img4)
cv2.imshow("zain6",img5)
cv2.waitKey(0)
cv2.destroyAllWindows()
