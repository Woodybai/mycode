import tkinter as tk
import time
roots=tk.Tk()
localtime2 = tk.StringVar() # Create the localtime2 string variable
localtime2.set(time.asctime(time.localtime(time.time()))) # Set the variable
tk.Label(roots, font=('arial', 16, 'bold'), textvariable=localtime2, bd=16, anchor="w").grid(row=2, column=0)
roots.mainloop()
