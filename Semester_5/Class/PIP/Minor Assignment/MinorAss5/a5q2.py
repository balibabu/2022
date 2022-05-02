globalVar=10
def test():
    localVar=20
    globalVar=30
    print('inside function test: globalVar=',globalVar)
    print('inside function test: localVar=',localVar)

test()
print('outside function test: globalVar=',globalVar)
