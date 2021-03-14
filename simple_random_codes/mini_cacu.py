import tkinter as tk
root=tk.Tk()
v1=tk.StringVar()
v1.set("answer")


label=tk.Label(root,text="input first number")
label.grid(row=0,column=0)
e1=tk.Entry(root)

#e1.insert(0,"0000")

e1.grid(row=0,column=1)
labe2=tk.Label(root,text="input second number")
labe2.grid(row=1,column=0)
e2=tk.Entry(root)
e2.grid(row=1,column=1)


#e2.insert(0,"0000")
l3=tk.Entry(root,textvariable=v1)
l3.grid(row=4,column=0)

s2=e2.get()

def add1():
    s1=e1.get()
    s2=e2.get()
    
    sum1=s1+s2
    l3.delete(0,tk.END)
    print(sum1)
    l3.insert(0,sum1)
    

b1=tk.Button(root,text="num1+num2",command=add1)
b1.grid(row=2,column=0)
 

root.mainloop()
