import tkinter as tk
import cv2
import os
import json
import random
"""
pic=[]
for a,b,c in os.walk("c://"):
    if len(pic)>50:
        break
    for file in c:
        
        if file.endswith(".jpg"):
            img=os.path.join(a,file)
            pic.append(img)
with open("kantu.json","w") as f:
    json.dump(pic,f)

"""
root=tk.Tk()

with open("kantu.json") as ff:
    im1=json.load(ff)


def func1():
    global a
    a=random.randint(0,len(im1))
    
    
    pic=cv2.imread(im1[a])
    cv2.imshow("kantu",pic)
    cv2.waitKey(500)
def next1():
    global a
    a=a+1
    pic=cv2.imread(im1[a])
    cv2.imshow("kantu",pic)
    cv2.waitKey(500)

def prev():
    global a
    a=a-1
    pic=cv2.imread(im1[a])
    cv2.imshow("kantu",pic)
    cv2.waitKey(500)
   

b1=tk.Button(root,text="next",command=next1)
b1.pack()
b1=tk.Button(root,text="prev",command=prev)
b1.pack()
b1=tk.Button(root,text="random",command=func1)
b1.pack()
b1=tk.Button(root,text="exit",command=func1)
b1.pack()
