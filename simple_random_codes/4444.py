import random
a=[1,2,3]
f=[]

while True:
    while True:
        c=[]
        b=random.choice(a)
        if b not in c:
              c.append(b)
              if len(c)==3 and c not in f:
                f.append(c)
                print(f,len(f))
                    
    
     

            
     
