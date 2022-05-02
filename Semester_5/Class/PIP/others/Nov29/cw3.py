a=4
def f():
    a=5
    def g():
        b=a #a is not global variable so we cant access a
        print(b)
        a=5
    g()
f()
