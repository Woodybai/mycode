import cv2
import numpy as np
import re
import os
for a,b,c in os.walk("c://"):
    for file1 in c:
        if file1.endswith(".jpg"):
            file2=os.path.join(a,file1)
            x=cv2.imread(file2)
            x1=cv2.resize(x,(1000,1000))
            cv2.imshow("fdfd",x1)
            cv2.waitKey(1000)
