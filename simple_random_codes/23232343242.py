from tkinter import *
def close_window():
    global entry
    entry = E.get()
    print(entry)
    root.destroy()

root = Tk()
E = Entry(root)
E.pack(anchor = CENTER)
B = Button(root, text = "OK", command = close_window)
B.pack(anchor = S)
root.mainloop()
    
