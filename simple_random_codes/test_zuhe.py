a=[1,2,3,4,5,6,7,8,9]
result=[]
for a1 in a:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                for a5 in a:
                    for a6 in a:
                        for a7 in a:
                            for a8 in a:
                                for a9 in a:
                                    list_comb=[a1,a2,a3,a4,a5,a6,a7,a8]
                                    ss=[]
                                    for x in list_comb:
                                        ss.append(x)
                                        if x in ss:
                                            break
                                    else:
                                      result.append(list_comb)
len(result)
