'''6. Write a recursive function to calculate the sum of the positive integers of n+(n-2)+(n-
4)... (until n−x ≤ 0). For example, if n=6, then output should be 6+(6-2)+(6-4)+(6-6) = 12'''
def series(n):
    if n==1 or n==0:
        print (n,end=' = ')
        return n
    else:
        print(n,'+',end=' ')
        return n + series(n-2)

n=int(input('enter a number '))
print(series(n))