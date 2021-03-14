a=[1,2,3,4,5,6]
import random
res=[]
while True:
        b=[]
        while len(b)<6:
                c=random.choice(a)
                if c not in b:
                        b.append(c)
        else:
            if b not in res:
                res.append(b)
                
                print(len(res))
        

