import time
import tkinter as tk
root=tk.Tk()
def changecolor():
    root.config(background="red")
    time.sleep(1)
    root.config(background="white")
    #root.after(1200,changecolor)

changecolor()
root.mainloop()
