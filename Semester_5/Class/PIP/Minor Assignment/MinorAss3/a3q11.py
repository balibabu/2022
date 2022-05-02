def isCoprime(a, b):
    if a % b == 0: return False
    for i in range(2, a + 1):
        if a % i == 0 and b % i == 0:
            return False

    return True


n1 = int(input('enter a number '))
n2 = int(input('enter 2nd number '))

print('is co-prime?', isCoprime(n1, n2))

