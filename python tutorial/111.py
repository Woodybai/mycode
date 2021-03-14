import random
import time
a=[ x for x in "abcdefg"]
res=[]
 
time3=time.time()
while True:
    b=[]
    while len(b)<7:
             
             c=random.choice(a)
             
             if c not in b:
                        b.append(c)
    
    if  b not in res:
        res.append(b)
        time2=time.time()

        print(len(res))
    
      


        
	 
