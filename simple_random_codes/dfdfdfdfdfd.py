import tkinter as tk
import sys
root=tk.Tk()
b2=tk.Button(root,text="bai3")
b2.pack()
b1=tk.Button(root,text="bai",command=b2.destroy)
b1.pack()
root.mainloop()
