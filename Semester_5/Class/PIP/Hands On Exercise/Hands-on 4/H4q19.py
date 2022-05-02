'''19. Write a python program to determine whether or not a number n is a factorial number.'''
def isfactorial(n):
    fact=1
    c=1
    while fact<=n:
        fact *= c
        if fact==n: return c
        c += 1

    return None

num=int(input("enter a number "))
print("the number is factorial of",isfactorial(num))
