import tkinter as tk
import os
root=tk.Tk()
sn=[]

def click(m):
    print(m)
for x in range(1,5):
    b=str(x)
    sn= tk.Button(root,text=b,command=lambda:click(b))
    sn.pack()
root.mainloop()
    
    
