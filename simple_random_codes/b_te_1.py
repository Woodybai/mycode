import os
import tkinter as t
import sys
def changev():
    v.set("xiaowu")
root=t.Tk()
button1=t.Button(root,text="click me",command=root.destroy)
button1.pack()
button2=t.Button(root,text="destoy button1",command=changev)
button2.pack()
e1=t.Entry(root)
e1.pack()
v=t.StringVar()
v.set("bai")

l1=t.Label(root,textvariable=v)
l1.pack()
root.mainloop()
