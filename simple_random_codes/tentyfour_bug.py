while True:
    a=str(input("number\n"))
    b=str(input("number\n"))
    c=str(input("number\n"))
    o=["+","-","*","/"]
    ql="("
    qr=")"
    for o1 in o:
          for o2 in o:
            if eval(a+o1+b+o2+c)==24:
                
              print(a,o1,b,o2,c)
               
            elif eval(b+o1+c+o2+a)==24:
                print(b,o1,c,o2,a)
            elif eval(c+o1+b+o2+a)==24:
                
                print(c,o1,b,o2,a)
            elif eval(ql+a+o1+b+qr+o2+c)==24:
                print(ql,a,o1,b,qr,o2,c)
            elif eval(ql+b+o1+c+qr+o2+a)==24:
                print(ql,b,o1,c,qr,o2,a)
            elif eval(ql+c+o1+a+qr+o2+b)==24:
                print(ql,c,o1,a,qr,o2,b)
            elif eval(a+o1+ql+b+o2+c+qr)==24:
                print(a,o1,ql,b,o2,c,qr)
            elif eval(b+o1+ql+c+o2+a+qr)==24:
                print(b,o1,ql,c,o2,a,qr)
            elif eval(c+o1+ql+b+o2+a+qr)==24:
                
                print(c,o1,ql,b,o2,a,qr)
            
    else:
        print('no match')
          


