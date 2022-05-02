a=5
def f():
    a=4
    def g():
        global a
        print('in f and g',a)
        a=10
        print('in f and g',a)
    
    print('in f',a)
    g()
    print('in f',a)
f()
print('outside',a)

