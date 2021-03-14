import cv2
import os
for mdir,sdir,files in os.walk("c://"):
    for file in files:
        if file.endswith(".jpg"):
            try:
                p=os.path.join(mdir,file)
                p1=os.path.abspath(p)
                print(p1)
                a=cv2.imread(p1)
                cv2.imshow("bai",a)
                cv2.waitKey(120)
            except:
                print(p1,"have problem")
           
