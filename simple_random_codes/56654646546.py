from tkinter.filedialog import *
from tkinter import *

def FileOpen():
    r = askopenfile(title = 'Python Tkinter')
    print (r)
root = Tk()
button1 = Button(root,text = 'File Open',command = FileOpen)
button1.pack(side = 'left')

root.mainloop()
 
