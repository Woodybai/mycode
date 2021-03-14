import os
a=9
def c():
    a=8
    print(a)

def d():
    global a
    print(a)
print("global a %s"%a)
print(a)
c()
d()
