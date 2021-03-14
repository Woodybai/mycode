import tkinter as tk
root=tk.Tk()
gameon=True
x=1
def gameon():
    gameon=True
                  
    while gameon:
        global x
        x=x+1
        print(x)
        if x>=100:
            gameon=False
button1=tk.Button(root,text="gameon",command=gameon)
button1.pack()
    
root.mainloop()
