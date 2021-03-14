import pygame as p
import os
import tkinter as tk
import random
os.chdir(r"d://")
a=[]
b=[]
n=True
z=0

def choose():
    for mdir,subdir,files in os.walk("."):
        for file in files:
            if file.endswith(".mp3"):
               s1=os.path.join(mdir,file)
               s2=os.path.abspath(s1)
               #print(s1)
               #a.append(file)
               b.append(s2)
               sb=str(b)
               v.set(sb)
               if len(b)>100:
                   break
def ne():
 
 global n,z
 if n==False:
     p.init()
     p.mixer.init()
     musicfile1=b[z]
     s.set(b[z]+"...."+"now playing")
 
     z=z+1
     if z>len(b)-1:
         z=0
     p.mixer.music.load(musicfile1)
     p.mixer.music.play()
     
     
 
      
             
             
    
    
     
 else:
     for x ,y in enumerate(b):

         
         
       if y==musicfile:
         
         z=x+1
         p.mixer.init()
          
         s.set(b[z]+"...."+"now playing")
         #musicfile=musicfile1
         
         n=False
         
         p.mixer.music.load(b[z])
         
         
         p.mixer.music.play()
         
         
   
         
         
        
        

  
print(b)
def play():
 global musicfile
 musicfile=random.choice(b)
 p.mixer.init()
 p.mixer.music.load(musicfile)
 s.set(musicfile+"...."+"now playing")
 p.mixer.music.play()
def pause():
    p.mixer.music.stop()
def volumnup():
    #global a
    
    p.mixer.music.set_volume(a)
    a=a+10
    
root=tk.Tk()
s=tk.StringVar()
v=tk.StringVar()

root.geometry("1600x1200")
root.title("我的播放器")
bt1=tk.Button(root,text="随机播放歌曲",command=play)
bt1.pack()
 
bt2=tk.Button(root,text="暂停",command=pause)
bt2.pack()
bt3=tk.Button(root,text="歌曲列表",command=choose)
bt3.pack()

bt4=tk.Button(root,text="下一曲",command=ne)
bt4.pack()

lb=tk.Label(root,textvariable=s)
lb.pack()
lb1=tk.Message(root,textvariable=v)
lb1.pack()
root.mainloop()
