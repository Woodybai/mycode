import time
import tkinter as tk
import winsound as ws
root=tk.Tk()
v=tk.StringVar()
t=time.asctime()
v.set(t)
label1=tk.Label(root,textvariable=v)
label1.pack()

def showdate():
    t1=time.localtime()
    v.set(t1)
    if t1.tm_hour==22 and t1.tm_min==11:
        ws.Beep(1000,1000)
        
    root.after(100,showdate)
showdate()
root.mainloop()
