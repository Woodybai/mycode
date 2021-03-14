import os,tkinter
root=tkinter.Tk()
l1=tkinter.Label(root,text="tempture",bg="red")
l1.pack()

e1=tkinter.Entry(root)
e1.pack()
b=e1.get()
print(b)
l2=tkinter.Label(root,text=b)
l2.pack()
root.mainloop()
tkinter.mainloop()

