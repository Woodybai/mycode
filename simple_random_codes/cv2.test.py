import numpy as np
import cv2
while True:
    a=np.random.randint(1,255,(3320,2240,3),np.uint8)
    cv2.imshow("b",a)
    cv2.waitKey(0)
