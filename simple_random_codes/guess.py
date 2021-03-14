import random
a=random.randint(1,50)
count=0
while True:
        i=int(input('inu a number?'))
        if i==a:
         print("you win")
        elif i<a:
              print("too small")
        else:
              print('too large')
        count=count+1
        if count>10:
              print("you lose ,the random number is",a)
              break
