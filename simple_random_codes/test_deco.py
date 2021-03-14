def a(func):
    print("a")
    def inner():
            #print("b")
            func()
    return inner

@a
def b():
    print("b")
@a
def b():
    print("b")
b()

