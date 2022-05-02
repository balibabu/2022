def series(n):
    if n==1 or n==0:
        return n
    else:
        return n + series(n-2)

n=int(input('enter a number '))
print(series(n))
