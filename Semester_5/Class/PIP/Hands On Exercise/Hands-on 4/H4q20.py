'''For some integer n, write a python program to find the largest factorial number present as
factor in n.'''

def isfactorial(n):
    fact=1
    c=1
    largest=1
    while fact<=n:
        fact *= c
        if n%fact==0: largest=fact
        c += 1
    return largest

num=int(input("enter a number "))
print("largest factorial present as factor is",isfactorial(num))
