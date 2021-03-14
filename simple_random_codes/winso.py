import winsound
a=37
while True:
    winsound.Beep(a,333)
    a=a+50
    if a>32767:
        break
