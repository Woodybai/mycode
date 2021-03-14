import tkinter
root=tkinter.Tk()
root.geometry("800x800")
root.title("bai")
buttong=[]
engro=[]
labgro=[]
def shoot():
    print("bai")
for x in range(4):
    b=tkinter.Button(root,text="hello"+str(x),bg="red",command=shoot)
    en=tkinter.Entry(root,text="good"+str(x),bg="yellow")
    en.pack()
    l=tkinter.Label(root,text="i am a label")
    l.pack()
    b.pack()
    buttong.append(b)
    engro.append(en)
    labgro.append(l)
    print(engro,labgro,buttong)


    
    
