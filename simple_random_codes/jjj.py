a={"bai":"12345","zhuang":"23456"}
name=input("your name")
passw=input("password")
for x in a:
    if x==name and a[x]==passw:
        print("welcome")
        break
else:
     print("something wrong")
