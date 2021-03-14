a=[0,1]
b=[]
while True:
	import random
	c=[]
	for x in range(8):
	 r=random.choice(a)
	  
	 
	 c.append(r)
	if b.count(c)==0:
	  b.append(c)
	else:
	  print(b,len(b))
