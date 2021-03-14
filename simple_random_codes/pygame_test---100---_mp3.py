import pygame as p
import os
import tkinter as tk
import random
os.chdir(r"c://")
a=[]
b=[]

def choose():
    for mdir,subdir,files in os.walk("."):
        if len(b)>20:
            break
        for file in files:
            if file.endswith(".mp3"):
               s1=os.path.join(mdir,file)
               s2=os.path.abspath(s1)
               #print(s1)
               #a.append(file)
               try:
                   p.mixer.init()
                   play1=p.mixer.music.load(s2)
                   b.append(s2)
                   print(b)
               except:
                    print("problem",s2)
               if len(b)>20:
                  break
                
              
               global sb
               sb=str(b)
               
              
def seei():
    v.set(sb)
    print(b)


               
    
  

def play():
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
bt5=tk.Button(root,text="显示列表",command=seei)
bt5.pack()
bt3=tk.Button(root,text="歌曲列表",command=choose)
bt3.pack()
lb=tk.Label(root,textvariable=s)
lb.pack()
lb1=tk.Message(root,textvariable=v)
lb1.pack()
root.mainloop()
