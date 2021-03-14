import os,cv2
for a,b,c in os.walk("."):
	for file in c:
            if file.endswith("jpg"):
                  file1=os.path.join(a,file)
                  try:
                          pic=cv2.imread(file1)
                          cv2.imshow("fdfd",pic)
                          cv2.waitKey(100)
                  except:
                          pass
