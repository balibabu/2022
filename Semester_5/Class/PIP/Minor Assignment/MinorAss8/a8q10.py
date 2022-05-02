'''10. Write a recursive function that takes number n as an
input parameter and prints ndigit strictly increasing numbers.'''
def getnum(arr):
    s=''
    for i in arr:
        s+=str(i)
    return int(s)

def generate(n,p,num):
    if p==n:
        print (getnum(num))
        return
    for i in range(num[p-1],9):
        num[p]=i+1
        generate(n,p+1,num)
        num[p] = i - 1
n=int(input('enter a number of digits:'))
generate(n,0,[0 for i in range(n)])

