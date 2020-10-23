import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("image.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )
#img = cv2.cvtColor(img, cv2.COLOR__BRG2RGB)
cv2.imshow("zain",img)
cv2.waitkey(0)
cv2.destroyAllWindows()
