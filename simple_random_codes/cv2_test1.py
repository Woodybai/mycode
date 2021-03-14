import cv2,os,re
import numpy as np
os.chdir("d://back_picture")


for a,b,c in os.walk("."):
    for file in c:
        if re.search("\w*.jpg$", file) :
            file_path=os.path.join(a,file)
            img = cv2.imdecode(np.fromfile(file_path ,dtype=np.uint8),-1)
             
            print(file_path)
            
    
            cv2.imshow("fdfd",img)
            cv2.waitKey(0)
    
    
