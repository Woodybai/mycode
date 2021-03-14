import pygame as pg
import os
import pandas as pd
import tkinter as tk
root=tk.Tk()
root.geometry("+28+300")
add=1
row=0


 
def btn1(file):
    pg.mixer.init()
    pg.mixer.music.load(file)
    pg.mixer.music.play()
for x,y,z in os.walk("d://"):
    for file in z:
        if file.endswith(".mp3"):
            row=row+1
            file1=os.path.join(x,file)
         
            btn=tk.Button(root,text=file,command=lambda file1=file1 :btn1(file1))
            btn.pack()
                
                

root.mainloop()
