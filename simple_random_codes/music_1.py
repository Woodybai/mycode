import winsound
import random
import time
def a(x):
    winsound.Beep(2000,x)
def b(y):
    winsound.Beep(200,y)
def c(z):
    winsound.Beep(1000,z)

while True:
    x=random.randint(20,1200)
    y=random.randint(20,1200)
    z=random.randint(20,1200)
    list2=[x,y,z]
    if random.choice(list2)==x:
        a(x)
        #time.sleep(1)
    elif random.choice(list2)==y:
        b(y)
        #time.sleep(1)
    else:
        c(z)
        #time.sleep(1)
    
