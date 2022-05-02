def multiply(a,b):
    if b==0:
        return 0
    elif b==1:
        return a
    else:
        return a+multiply(a,b-1)

print(multiply(5,4))