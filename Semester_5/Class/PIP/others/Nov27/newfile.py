def f():
    print('global f')

def g():
    global f
    print('before redefinition of f',id(f))
    def f():
        print('inner f')

    print('after redefinition of f',id(f))
    f()
def h():
    print('inside h',id(f))
    f()
    fprime()

print('in global',id(f))
fprime=f
f()
g()
print('in global',id(f))
fprime()
h()

