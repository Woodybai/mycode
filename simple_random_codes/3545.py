a=[1,2,3,4,5,6,7,8,9]
result=[]
for x in a:
	for y in a:
		list1=[x,y]
		for g in range(len(list1)):
			for h in range(len(list1)):
                            if g!=h and list1[g]!=list1[h]:
                                if list1 not in result:
                                    result.append(list1)
print(len(result))
                                
