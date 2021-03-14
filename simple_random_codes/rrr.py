import random
a=[1,3,5]
while True:
	for x in range(4):
		d2=random.choice(a)
		d3=random.choice(a)
		d4=random.choice(a)
		d5=random.choice(a)
		if d2+d3+d4+d5==9:
			print(d2,d3,d4,d5)
			break
