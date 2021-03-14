import time
import random
dic={}
for x in range(20):
    ran=random.randint(1,60)
    t=time.localtime()
    m=str(t.tm_min)
    s=str(t.tm_sec)
    time.sleep(1)
    
    dic[" time now is %s min and %s sec"%(m,s)]=ran
