import os
import cv2
import winsound
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
 
print(os.getcwd())
for a,b,c in os.walk("d://"):
    for file in c:
        if file.endswith(".jpg"):
            try:
                file1=os.path.join(a,file)
                print(file1)
                img=cv2.imread(file1)
                img2=cv2.resize(img,(200,200))
                
                rects = face_cascade.detectMultiScale(img, 1.3,5)
                                 
                                 
                print(len(rects))
                if len(rects)==1:
                    winsound.Beep(300,200)
            
                    cv2.imshow("fdfd",img2)
                    cv2.waitKey(200)
                        
            except:
                print("cant open")


                
                    
            
