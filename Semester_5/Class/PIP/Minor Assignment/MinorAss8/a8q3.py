'''3. Write a recursive function to calculate the value of ’a’ to the power ’b’.'''
def power(a,b):
    if b==0:
        return 1
    else:
        return a*power(a,b-1)

a=int(input('enter value of a:'))
b=int(input('enter value of b:'))
num=power(a,b)
print('a**b =',num)

