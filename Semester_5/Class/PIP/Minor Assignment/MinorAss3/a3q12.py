def multiply(a,b):
    product=0
    for i in range(b):
        product+=a
    return product

n1 = int(input('enter a number '))
n2 = int(input('enter 2nd number '))

print('product of numbers is',multiply(n1,n2))