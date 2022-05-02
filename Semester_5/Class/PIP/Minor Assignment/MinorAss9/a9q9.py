'''9. Identify two exceptions that may be raised while executing the following statement:
result = a + b'''
def fun(a, b):
    try:
        result=a+b
        print(result)
    except TypeError:
        print('TypeError')




fun(2,'a') #TypeError
